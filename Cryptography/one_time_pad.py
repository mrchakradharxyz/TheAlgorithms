# E(K,m) = K XOR m = c
# D(K,c) = K XOR c = m

def xor_encrypt(plaintext: str, key: bytes) -> bytes:
    plaintext_bytes = plaintext.encode()
    key_repeated = (key * (len(plaintext_bytes) // len(key) + 1))[:len(plaintext_bytes)]
    ciphertext = bytes([b ^ k for b, k in zip(plaintext_bytes, key_repeated)])
    return ciphertext

def xor_decrypt(ciphertext: bytes, key: bytes) -> str:
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decrypted_bytes = bytes([b ^ k for b, k in zip(ciphertext, key_repeated)])
    return decrypted_bytes.decode()

# Example usage
plaintext = "My name is Chakradhar Reddy"
key = b"mykey123"
ciphertext = xor_encrypt(plaintext, key)
decrypted_text = xor_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Decrypted: {decrypted_text}")
