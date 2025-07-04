# 2_verify.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Nhập public key
print("🔓 Dán public key PEM (kết thúc bằng dòng trắng):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
public_key_pem = "\n".join(lines).encode()

public_key = serialization.load_pem_public_key(public_key_pem)

# Nhập dữ liệu và chữ ký
message = input("Nhập nội dung gốc: ").encode('utf-8')
signature_hex = input("Nhập chữ ký (hex): ")
signature = bytes.fromhex(signature_hex)

# Kiểm tra chữ ký
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n✅ CHỮ KÝ HỢP LỆ!")
except Exception:
    print("\n❌ CHỮ KÝ KHÔNG HỢP LỆ!")
