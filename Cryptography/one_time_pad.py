# E(K,m) = K XOR m = c
# D(K,c) = K XOR c = m

import os

def xor_encrypt(plaintext: str, key: bytes) -> bytes:
    plaintext_bytes = plaintext.encode()
    ciphertext = bytes([b ^ key[i] for i, b in enumerate(plaintext_bytes)])
    return ciphertext

def xor_decrypt(ciphertext: bytes, key: bytes) -> str:
    decrypted_bytes = bytes([b ^ key[i] for i, b in enumerate(ciphertext)])
    return decrypted_bytes.decode()

# Example Usage
plaintext = "1234"
key = "1234".encode()
ciphertext = xor_encrypt(plaintext, key)
decrypted_text = xor_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted: {decrypted_text}")
