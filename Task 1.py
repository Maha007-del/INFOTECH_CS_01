def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isupper():
            start = ord('A')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        elif char.islower():
            start = ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char  # leave non-letters unchanged
    return result

def main():
    print("Caesar Cipher Program")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Encrypt or Decrypt? (e/d): ").lower()

    if mode == 'e':
        output = caesar_cipher(message, shift, mode)
        print("Encrypted message:", output)
    elif mode == 'd':
        output = caesar_cipher(message, -shift, mode)
        print("Decrypted message:", output)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()