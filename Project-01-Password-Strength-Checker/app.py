from flask import Flask, render_template, request, jsonify
from password_utils import calculate_entropy, get_crack_time, generate_secure_password

app = Flask(__name__)

# Load common passwords
with open('wordlists/common_passwords.txt', 'r') as f:
    COMMON_PASSWORDS = set(line.strip().lower() for line in f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.json.get('password', '')
    
    # Analysis logic
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_sym = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    score = 0
    if length >= 8: score += 25
    if has_upper and has_lower: score += 25
    if has_digit: score += 25
    if has_sym: score += 25
    
    is_common = password.lower() in COMMON_PASSWORDS
    if is_common: score = min(score, 20)
    
    entropy = calculate_entropy(password)
    crack_time = get_crack_time(entropy)
    
    return jsonify({
        'score': score,
        'entropy': entropy,
        'crack_time': crack_time,
        'is_common': is_common
    })

@app.route('/generate', methods=['GET'])
def generate():
    return jsonify({'password': generate_secure_password()})

if __name__ == '__main__':
    app.run(debug=True)