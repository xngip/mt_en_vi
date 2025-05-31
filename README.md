# 🌐 Dịch Máy Anh - Việt

> Hệ thống dịch máy tiếng Anh → tiếng Việt sử dụng mô hình Transformer tùy chỉnh bằng TensorFlow.

![language icon](https://img.shields.io/badge/lang-Vietnamese-blue)
![tensorflow](https://img.shields.io/badge/framework-TensorFlow-orange)
![status](https://img.shields.io/badge/status-dev-yellow)

---

## 📌 Giới thiệu

Đây là một ứng dụng dịch máy đơn giản từ tiếng Anh sang tiếng Việt, sử dụng mô hình Transformer được huấn luyện từ đầu. Hệ thống bao gồm:

* ✨ Mô hình dịch Anh-Việt huấn luyện tùy chỉnh bằng TensorFlow
* 💻 Giao diện web frontend viết bằng HTML/CSS/JavaScript
* 🔁 Backend Flask để xử lý yêu cầu dịch
* 🔊 Hỗ trợ đọc văn bản (text-to-speech), sao chép, chia sẻ nội dung

---

## 🚀 Cài đặt & Chạy thử

### 1. Cài môi trường Python

```bash
git clone https://github.com/xngip/mt_en_vi.git
cd mt_en_vi
python -m venv venv
source venv/bin/activate  # hoặc .\venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

### 2. Khởi động backend Flask

```bash
python app.py
```

Mặc định sẽ chạy ở `http://127.0.0.1:5000`.

### 3. Mở giao diện web

Mở `templates/index.html` trực tiếp bằng trình duyệt (hoặc dùng Live Server nếu dùng VSCode).

---

## 🧠 Mô hình dịch

* **Kiến trúc:** Transformer (Encoder-Decoder)
* **Framework:** TensorFlow
* **Cách huấn luyện:**

  ```bash
  cd train_model
  python 'train_model/mt_en_vi.py'
  ```

  Hoặc chạy các cell ở file `train_model\mt_en_vi.ipynb`. Có thể up lên colab để chạy nhanh hơn. Ưu tiên cách này hơn


* **Dữ liệu:** Hơn 200 nghing câu Anh-Việt

Mô hình huấn luyện xong được lưu trong `weight_model`.

---

## 📊 API Endpoint

| Method | Endpoint     | Mô tả                                        |
| ------ | ------------ | -------------------------------------------- |
| POST   | `/translate` | Trả về bản dịch tiếng Việt cho câu tiếng Anh |

**Body:**

```json
{ "sentence": "Hello world!" }
```

---

## 📦 Yêu cầu hệ thống

* Python 3.8+
* TensorFlow 2.18.0
* Flask 2.3.3
* NumPy 2.0.2, SubwordTextEncoder (nếu dùng TensorFlow tokenizer)

---

## 👨‍💼 Nhóm phát triển

* Trưởng nhóm: A45240 - Nguyễn Xuân Giáp
* Thành viên: A49651 - DƯƠNG THỊ THÙY LINH, a46330 - Nguyễn Thị Huyền Trang
* Trường Đại Học Thăng Long

---

## 📈 Gợi ý mở rộng

* Tự động phát hiện ngôn ngữ nguồn
* Dịch hai chiều (Anh ↔ Việt)
* Tích hợp Docker hoặc Streamlit
* Tạo ứng dụng desktop/mobile

---

## 📄 License

MIT License © 2025 Nhóm 1 - Dự án Dịch Máy Anh-Việt
