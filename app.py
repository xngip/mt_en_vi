from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import pickle
import tensorflow as tf
from model.transformer import Transformer, translation, create_masks, CustomSchedule

# Constants
ENCODER_LEN = 100 # max length of encoder input
DECODER_LEN = 100 # max length of decoder input
BATCH_SIZE = 64 # batch size
BUFFER_SIZE = BATCH_SIZE * 8 # buffer size for shuffling

app = Flask(__name__)
CORS(app)

# Load mô hình và tokenizer
def build_model_for_restore(transformer, optimizer):
    dummy_inp = tf.ones((1, ENCODER_LEN), dtype=tf.int32)
    dummy_tar = tf.ones((1, DECODER_LEN), dtype=tf.int32)

    _ = transformer(
        inp=dummy_inp,
        tar=dummy_tar,
        training=False,
        enc_padding_mask=None,
        look_ahead_mask=None,
        dec_padding_mask=None
    )
    
    dummy_grads = [tf.zeros_like(v) for v in transformer.trainable_variables]
    optimizer.apply_gradients(zip(dummy_grads, transformer.trainable_variables))

def load_model_and_tokenizer(checkpoint_path='./weight_model'):
    global transformer, optimizer, en_tokenizer, vi_tokenizer

    with open(os.path.join(checkpoint_path, 'en_tokenizer.pkl'), 'rb') as f:
        en_tokenizer = pickle.load(f)
    with open(os.path.join(checkpoint_path, 'vi_tokenizer.pkl'), 'rb') as f:
        vi_tokenizer = pickle.load(f)

    transformer = Transformer(
        num_layers=6,
        d_model=128,
        num_heads=4,
        dff=512,
        input_vocab_size=len(en_tokenizer.word_index) + 1,
        target_vocab_size=len(vi_tokenizer.word_index) + 1,
        pe_input=ENCODER_LEN,
        pe_target=DECODER_LEN,
        rate=0.15
    )
    learning_rate = CustomSchedule(128)
    optimizer = tf.keras.optimizers.Adam(learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

    build_model_for_restore(transformer, optimizer)

    ckpt = tf.train.Checkpoint(transformer=transformer, optimizer=optimizer)
    ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=3)

    if ckpt_manager.latest_checkpoint:
        ckpt.restore(ckpt_manager.latest_checkpoint).expect_partial()
        print(f"✅ Restored from {ckpt_manager.latest_checkpoint}")
    else:
        print("❌ No checkpoint found.")

load_model_and_tokenizer()

# API dịch
@app.route("/translate", methods=["POST"])
def translate_api():
    data = request.get_json()
    sentence = data.get("sentence", "")

    if not sentence:
        return jsonify({"translation": ""})

    result = translation(sentence, transformer, en_tokenizer, vi_tokenizer, ENCODER_LEN, DECODER_LEN)
    return jsonify({"translation": result})


# Route trang chính (nếu dùng HTML frontend)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
