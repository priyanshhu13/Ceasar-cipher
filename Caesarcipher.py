def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset) #Applying here the Shift Value 
        else:
            result += char

    return result

def encrypt():
    plaintext = input("plaintext: ")
    shift = int(input("what should be the shift value? "))

    ciphertext = caesar_cipher(plaintext, shift)

    print("Encrypted Text:", ciphertext)

def decrypt():
    plaintext= input("text:")
    shift = int(input("shift value?"))

    ciphertext = caesar_cipher(plaintext, -shift)

    print("decrypted text:", ciphertext)

mode=input("you want to encrypt(e) or decrypt(d)?")
if mode == "e":
    encrypt()
elif mode == "d":
    decrypt()
else:
    print("incorrect input...")