import os
import base64

INPUT_FILE = "configs/all_configs.txt"
OUTPUT_SUB = "configs/subscription.txt"
PUBLIC_HTML = "public/index.html"

# 👇 این دو خط را با نام واقعی خود عوض کن
GITHUB_USER = "bc95game-art"
GITHUB_REPO = "Vip3434"

def generate_sub():
    if not os.path.exists(INPUT_FILE):
        print("all_configs.txt not found")
        return False
    with open(INPUT_FILE, 'r') as f:
        data = f.read().strip()
    if not data:
        return False
    encoded = base64.b64encode(data.encode()).decode()
    with open(OUTPUT_SUB, 'w') as f:
        f.write(encoded)
    return True

def update_html():
    sub_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/configs/subscription.txt"
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>V2Ray Subscription Panel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <h1>🎯 لینک اشتراک دائمی V2Ray</h1>
    <p>لینک خود را کپی کرده و در اپلیکیشن وارد کنید:</p>
    <div class="url-box">
        <input type="text" id="sub-url" value="{sub_url}" readonly>
        <button onclick="copyToClipboard()">📋 کپی لینک</button>
    </div>
    <p class="note">🔄 این لینک هر ۴ ساعت یکبار به‌روز می‌شود.</p>
    <p class="note">✅ کاملاً رایگان و دائمی</p>
</div>
<script src="script.js"></script>
</body>
</html>"""
    os.makedirs("public", exist_ok=True)
    with open(PUBLIC_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated")

if __name__ == "__main__":
    if generate_sub():
        update_html()
        print("✅ Done")
    else:
        print("❌ Failed: no configs found")
