# Caesar Cipher Tool

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force(ciphertext):
    print("Brute force results:")
    for shift in range(26):
        print(f"Shift {shift}: {decrypt(ciphertext, shift)}")

# Example usage
if __name__ == "__main__":
    message = "HELLO WORLD"
    shift = 3

    encrypted = encrypt(message, shift)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shift)
    print("Decrypted:", decrypted)

    brute_force(encrypted)
