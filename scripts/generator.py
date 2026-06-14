import os
import base64

INPUT_FILE = "configs/all_configs.txt"
OUTPUT_SUBSCRIPTION = "configs/subscription.txt"
PUBLIC_INDEX = "public/index.html"

# 👇 مقادیر واقعی خود را اینجا وارد کنید
GITHUB_USERNAME = "bc95game-art"
GITHUB_REPO = "Vip3434"

def generate_subscription():
    if not os.path.exists(INPUT_FILE):
        return False
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        configs = f.read().strip()
    if not configs:
        return False
    encoded = base64.b64encode(configs.encode('utf-8')).decode('utf-8')
    with open(OUTPUT_SUBSCRIPTION, 'w', encoding='utf-8') as f:
        f.write(encoded)
    return True

def update_html():
    # ساخت لینک صحیح با استفاده از متغیرهای واقعی
    subscription_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/main/configs/subscription.txt"
    html_content = f"""<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>پنل اشتراک V2Ray</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>🎯 پنل تولید لینک اشتراک V2Ray</h1>
        <p>لینک دائمی اشتراک شما (کپی کنید و در کلاینت V2Ray خود وارد کنید):</p>
        <div class="url-box">
            <input type="text" id="sub-url" value="{subscription_url}" readonly>
            <button onclick="copyToClipboard()">📋 کپی لینک</button>
        </div>
        <p class="note">🔄 این لینک هر ۴ ساعت یکبار به‌طور خودکار به‌روز می‌شود.</p>
        <p class="note">✨ کانفیگ‌ها از منابع معتبر جمع‌آوری و تست می‌شوند.</p>
        <div id="status">✅ سیستم فعال است - لینک شما دائمی می‌باشد.</div>
    </div>
    <script src="script.js"></script>
</body>
</html>"""
    os.makedirs("public", exist_ok=True)
    with open(PUBLIC_INDEX, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("HTML updated")

if __name__ == "__main__":
    if generate_subscription():
        update_html()
        print("Done")
    else:
        print("Failed")
