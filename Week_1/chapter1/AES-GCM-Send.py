# Chương trình nhập dữ liệu 
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hashlib import sha256
import os

plaintext = input("Nhập dữ liệu cần mã hóa: ").encode("utf-8")
key_input = input("Nhập khóa bí mật (có thể là tiếng Việt): ")

# === TẠO KHÓA từ chuỗi tiếng Việt ===
key = sha256(key_input.encode("utf-8")).digest()  # sinh khóa 32 bytes (AES-256)
aesgcm = AESGCM(key)

# === TẠO NONCE NGẪU NHIÊN ===
nonce = os.urandom(12)  # 96-bit, đúng chuẩn GCM

# === MÃ HÓA ===
ciphertext = aesgcm.encrypt(nonce, plaintext, None)

# === IN KẾT QUẢ ===
print("\n====== KẾT QUẢ ======")
print(f"Nonce (hex):      {nonce.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print("======================")

# Gợi ý: có thể copy 2 giá trị trên để dùng cho chương trình giải mã
