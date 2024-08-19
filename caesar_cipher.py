def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

plaintext = input("Enter the text to be Encrypted: ")
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Encrypted Text: {ciphertext}")
i=1
while i>0:
    con=input("Do you want to decrypt the text?? (y/n)")
    if con=='y':
        decrypted = caesar_decrypt(ciphertext, shift)
        print("Thankyou, Your text is Decrypted Successfully!!!")
        print(f"Decrypted Text: {decrypted}")
        break
    elif con=='n':
        print("\nThankyou, Your text is Encrypted Successfully!!!")
        break
    else:
        print("\nChoose the correct option!")
