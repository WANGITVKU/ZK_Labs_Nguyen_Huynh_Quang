# 2_encrypt.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Nhập public key PEM từ màn hình
print("🔓 Dán public key PEM (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
public_pem_str = "\n".join(lines).encode()

public_key = serialization.load_pem_public_key(public_pem_str)

# Nhập dữ liệu cần mã hóa
plaintext = input("Nhập dữ liệu cần mã hóa: ").encode("utf-8")

# Mã hóa
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# In kết quả
print("\n🔐 Dữ liệu đã mã hóa (hex):")
print(ciphertext.hex())
