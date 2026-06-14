function copyToClipboard() {
    let input = document.getElementById('sub-url');
    input.select();
    input.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(input.value);
    let btn = event.target;
    let oldText = btn.innerText;
    btn.innerText = '✅ کپی شد!';
    setTimeout(() => btn.innerText = oldText, 2000);
}
