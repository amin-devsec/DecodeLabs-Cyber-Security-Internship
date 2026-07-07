import math
import secrets
import string

def calculate_entropy(password):
    """Calculates the Shannon entropy of the password."""
    if not password:
        return 0
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in string.punctuation for c in password): charset_size += 32
    
    if charset_size == 0: return 0
    return round(len(password) * math.log2(charset_size), 2)

def get_crack_time(entropy):
    """Estimates crack time based on entropy (guesses per second: 10^10)."""
    if entropy == 0: return "Instant"
    guesses = 2**entropy
    seconds = guesses / 10000000000
    
    if seconds < 60: return "Instant"
    minutes = seconds / 60
    if minutes < 60: return f"{int(minutes)} minutes"
    hours = minutes / 60
    if hours < 24: return f"{int(hours)} hours"
    days = hours / 24
    if days < 365: return f"{int(days)} days"
    return f"{int(days/365)} years"

def generate_secure_password(length=16):
    """Generates a cryptographically secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))