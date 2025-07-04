# 3_decrypt.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Nhập private key PEM từ màn hình
print("🔐 Dán private key PEM (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
private_pem_str = "\n".join(lines).encode()

private_key = serialization.load_pem_private_key(private_pem_str, password=None)

# Nhập ciphertext (hex)
ciphertext_hex = input("Nhập ciphertext (hex): ")
ciphertext = bytes.fromhex(ciphertext_hex)

# Giải mã
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# In kết quả
print("\n✅ Dữ liệu đã giải mã:")
print(plaintext.decode("utf-8"))
