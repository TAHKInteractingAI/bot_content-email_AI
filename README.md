# Viết email và content sử dụng API của OpenAI

Một chương trình Python dùng để viết Email và nội dung sử dụng API của OpenAI

<img src="https://github.com/botsamqntdata/tahk_interacting_AI/blob/main/Screenshot%202023-05-22%20151030.png">

## Cách chạy chương trình

Download project về máy

```bash
git clone https://github.com/botsamqntdata/tahk_interacting_AI.git
```
Cài đặt thư viện
``` bash
pip install -r requirements.txt
```
Chạy chương trình
``` bash
python email_ai.py
```
## Viết email
Nhập các thông tin cần thiết trên giao diện
Nhập các thông số
``` bash
max_tokens, n, temperature, API Key
```
Giải thích các thông số:

"max_tokens": Tham số này xác định số lượng tối đa các từ (tokens) trong câu trả lời được tạo ra bởi mô hình. Số lượng từ nhập tùy vào mục đích.

"n": số lượng câu trả lời được tạo ra. Có thể đặt là 1

"stop": Giá trị này không cần nhập

"temperature": Tham số này điều chỉnh mức độ đa dạng của câu trả lời. Khi giá trị này cao, mô hình sẽ tạo ra các câu trả lời mang tính đa dạng và sáng tạo. Các từ được chọn có thể không liên quan hoặc có sự sáng tạo hơn, tạo nên các câu trả lời độc đáo. Khi giá trị này thấp, mô hình sẽ tạo ra các câu trả lời chính xác và cố định hơn. Các từ được chọn sẽ theo xu hướng phổ biến hơn và câu trả lời sẽ ít đa dạng hơn. Giá trị này nên đặt từ 0.3 đến 0.5

"API Key": nhập API keey của Open AI, https://platform.openai.com/account/api-keys
