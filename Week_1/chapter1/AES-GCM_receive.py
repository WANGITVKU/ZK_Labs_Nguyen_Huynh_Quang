# decryptor.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hashlib import sha256

# === NHẬP DỮ LIỆU ===
key_input = input("Nhập khóa bí mật (phải giống lúc mã hóa): ")
nonce_hex = input("Nhập Nonce (hex): ")
ciphertext_hex = input("Nhập Ciphertext (hex): ")

# === CHUYỂN DỮ LIỆU VỀ DẠNG BYTE ===
key = sha256(key_input.encode("utf-8")).digest()
nonce = bytes.fromhex(nonce_hex)
ciphertext = bytes.fromhex(ciphertext_hex)

aesgcm = AESGCM(key)

# === GIẢI MÃ ===
try:
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    print("\n✅ Giải mã thành công:")
    print(plaintext.decode("utf-8"))
except Exception as e:
    print("\n❌ Giải mã thất bại. Có thể sai khóa hoặc sai dữ liệu.")
