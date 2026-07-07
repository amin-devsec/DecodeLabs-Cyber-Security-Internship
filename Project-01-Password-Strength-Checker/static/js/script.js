const input = document.getElementById('passwordInput');
const progress = document.getElementById('progress');
const results = document.getElementById('results');

input.addEventListener('input', async () => {
    const val = input.value;
    if (!val) {
        progress.style.width = '0%';
        document.getElementById('strengthLabel').innerText = '-';
        document.getElementById('stats').innerHTML = '';
        return;
    }

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({password: val})
    });
    const data = await response.json();
    
    // Update Progress Bar
    progress.style.width = data.score + '%';
    
    // Determine Label and Color
    let label = "Weak";
    let color = "#ff4d4d";
    if (data.score >= 80) { label = "Very Strong"; color = "#2ecc71"; }
    else if (data.score >= 60) { label = "Strong"; color = "#27ae60"; }
    else if (data.score >= 40) { label = "Medium"; color = "#f1c40f"; }
    
    const labelEl = document.getElementById('strengthLabel');
    labelEl.innerText = label;
    labelEl.style.color = color;
    progress.style.backgroundColor = color;

    // Update Stats
    document.getElementById('stats').innerHTML = `
        <p>Entropy: ${data.entropy} bits</p>
        <p>Est. Crack Time: ${data.crack_time}</p>
        ${data.is_common ? '<p style="color:red">Warning: Common password detected!</p>' : ''}
    `;
});

document.getElementById('toggleBtn').onclick = () => {
    input.type = input.type === 'password' ? 'text' : 'password';
};

document.getElementById('generateBtn').onclick = async () => {
    const res = await fetch('/generate');
    const data = await res.json();
    input.value = data.password;
    input.dispatchEvent(new Event('input'));
};