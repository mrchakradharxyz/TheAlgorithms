# E(K,m) = K XOR m = c
# D(K,c) = K XOR c = m

import os

def otp_encrypt(plaintext: str) -> tuple[bytes, bytes]:
    plaintext_bytes = plaintext.encode()
    key = os.urandom(len(plaintext_bytes))  # truly random, same length
    ciphertext = bytes([b ^ k for b, k in zip(plaintext_bytes, key)])
    return ciphertext, key

def otp_decrypt(ciphertext: bytes, key: bytes) -> str:
    return bytes([c ^ k for c, k in zip(ciphertext, key)]).decode()

plaintext = "My name is Chakradhar Reddy"
ciphertext, key = otp_encrypt(plaintext)
decrypted = otp_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Key (hex): {key.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Decrypted: {decrypted}")
