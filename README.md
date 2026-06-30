# INFOTECH_CS_01
Python program to encrypt and decrypt text using the Caesar Cipher algorithm. Task-01 of Prodigy InfoTech Software Engineering Internship.
# PRODIGY_CS_01

Caesar Cipher encryption and decryption implementation in Python - Prodigy InfoTech Cyber Security Internship Task 01

## Description

A Python program that encrypts and decrypts text using the Caesar Cipher algorithm.

## Features

- Encrypts plaintext using a shift value.
- Decrypts ciphertext back to the original message.
- Supports both uppercase and lowercase letters.
- Preserves spaces, numbers, and special characters.

## How It Works

- `encrypt()` function shifts each alphabet character forward by the given shift value.
- `decrypt()` function shifts the characters backward to retrieve the original message.
- Uppercase and lowercase letters are handled separately.
- Non-alphabetic characters remain unchanged.

## Code Explanation

- `ord(char)` converts a character into its ASCII value.
- `% 26` ensures circular shifting (after Z comes A).
- `chr()` converts the ASCII value back into a character.

## Technologies Used

- Python 3

## How to Run

python caesar_cipher.py

## Example

**Input**

Enter message: Maha
Enter shift value: 3

**Output**

Encrypted text: Pdkd
Decrypted text: Maha
