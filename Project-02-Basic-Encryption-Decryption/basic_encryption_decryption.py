def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # For decryption, we reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Convert to 0-25 range, shift, modulo 26, convert back to ASCII
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave punctuation and spaces unchanged
            result += char
    return result

# --- Execution ---
plaintext = input("Enter the message to encrypt: ")
try:
    key = int(input("Enter the shift key (integer): "))

    # Encryption
    encrypted_text = caesar_cipher(plaintext, key, mode='encrypt')
    
    # Decryption
    decrypted_text = caesar_cipher(encrypted_text, key, mode='decrypt')

    # Output
    print(f"\nOriginal:  {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

except ValueError:
    print("Error: The shift key must be an integer.")