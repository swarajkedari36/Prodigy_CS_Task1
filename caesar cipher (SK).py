def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shifted = (ord(char) - shift_base + (shift if mode == 'encrypt' else -shift)) % 26
            result += chr(shifted + shift_base)
        else:
            result += char
    return result

while True:
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '3':
        print("Exiting. Goodbye!")
        break
    elif choice in ('1', '2'):
        mode = 'encrypt' if choice == '1' else 'decrypt'
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        result = caesar_cipher(message, shift, mode)
        print(f"Result ({mode}ed): {result}")
    else:
        print("Invalid choice. Please try again.")
