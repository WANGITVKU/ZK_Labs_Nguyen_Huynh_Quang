# 1_generate_keys.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Nhập chuỗi tiếng Việt làm khóa gốc
text_key = input("Nhập chuỗi bất kỳ (dùng làm 'bí danh'): ")

# Sinh khóa RSA mới
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Chuyển sang định dạng PEM (text)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# In ra màn hình
print("\n🔐 PRIVATE KEY (PEM):\n")
print(private_pem.decode())

print("🔓 PUBLIC KEY (PEM):\n")
print(public_pem.decode())
