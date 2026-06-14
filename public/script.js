function copyToClipboard() {
    const urlInput = document.getElementById('sub-url');
    urlInput.select();
    urlInput.setSelectionRange(0, 99999);
    try {
        navigator.clipboard.writeText(urlInput.value);
        const button = document.querySelector('.url-box button');
        const originalText = button.textContent;
        button.textContent = '✅ کپی شد!';
        setTimeout(() => {
            button.textContent = originalText;
        }, 2000);
    } catch (err) {
        alert('خطا در کپی کردن لینک');
    }
}
