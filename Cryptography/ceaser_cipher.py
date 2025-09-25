import string

def ceaser_cipher(plain_text: str, key: int) -> str:
    cipher = ''
    for text in plain_text:
        if text.islower():
            index = string.ascii_lowercase.index(text)
            cipher += string.ascii_lowercase[(index + key) % 26]
        elif text.isupper():
            index = string.ascii_uppercase.index(text)
            cipher += string.ascii_uppercase[(index + key) % 26]
        else:
            cipher += text
    return cipher

def decrypt(cipher: str, key: int) -> str:
    plain_text = ''
    for text in cipher:
        if text.islower():
            index = string.ascii_lowercase.index(text)
            plain_text += string.ascii_lowercase[(index - key) % 26]
        elif text.isupper():
            index = string.ascii_uppercase.index(text)
            plain_text += string.ascii_uppercase[(index - key) % 26]
        else:
            plain_text += text
    return plain_text

msg = "I'm Batman"
key = 5

encrypted = ceaser_cipher(msg, key)
decrypted = decrypt(encrypted, key)

print("Original :", msg)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
