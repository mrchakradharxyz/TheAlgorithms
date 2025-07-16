# E(K,m) = K XOR m = c
# D(K,c) = K XOR c = m

import os

def otp_encrypt(plaintext: str) -> tuple[bytes, bytes]:
    plaintext_bytes = plaintext.encode()
    key = os.urandom(len(plaintext_bytes))  # True one-time pad: same length, random
    ciphertext = bytes([p ^ k for p, k in zip(plaintext_bytes, key)])
    return ciphertext, key

def otp_decrypt(ciphertext: bytes, key: bytes) -> str:
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext, key)])
    return plaintext_bytes.decode()

plaintext = "My name is Chakradhar Reddy"
ciphertext, key = otp_encrypt(plaintext)
decrypted_text = otp_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Key (hex): {key.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Decrypted: {decrypted_text}")
