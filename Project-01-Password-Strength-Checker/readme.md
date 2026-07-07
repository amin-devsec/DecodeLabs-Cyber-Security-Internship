# Password Strength Checker

A secure, real-time password analysis tool designed to educate users on password hygiene. Built for a Cybersecurity internship program, this application utilizes entropy calculation and frequency analysis to assess password security.

## 🚀 Features
- **Real-time Analysis:** Instant feedback via JavaScript without page reloads.
- **Entropy Calculation:** Mathematically calculates password complexity in bits.
- **Crack Time Estimation:** Provides an estimate of how long a brute-force attack would take to crack the password.
- **Common Password Detection:** Cross-references input against a blacklist of leaked/common passwords.
- **Secure Generation:** Uses Python's `secrets` module for cryptographically strong password generation.
- **Responsive UI:** Dark-mode interface optimized for desktop and mobile.

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Security:** `secrets` module (CSPRNG)

## 📋 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/amin-devsec/DecodeLabs-Cyber-Security-Internship.git](https://github.com/amin-devsec/DecodeLabs-Cyber-Security-Internship.git)
   cd password-strength-checker
