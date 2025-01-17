def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption")
    
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        encrypted_message = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()