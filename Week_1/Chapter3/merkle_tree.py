import hashlib

# Băm dữ liệu bằng SHA-256
def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# Xây dựng cây Merkle từ list dữ liệu
def merkle_tree(data_blocks):
    # Tạo danh sách các hash (lá)
    hashes = [sha256(d) for d in data_blocks]

    if len(hashes) % 2 == 1:
        hashes.append(hashes[-1])  # Nhân đôi phần tử cuối nếu lẻ

    tree = [hashes]  # tầng đầu tiên là leaf hashes

    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i+1]
            temp.append(sha256(combined))
        if len(temp) % 2 == 1 and len(temp) != 1:
            temp.append(temp[-1])
        tree.append(temp)
        hashes = temp

    return tree

# In cây Merkle ra màn hình
def print_merkle_tree(tree):
    for level, hashes in enumerate(tree):
        print(f"Level {level}:")
        for h in hashes:
            print(" ", h)

# Kiểm tra xem dữ liệu có trong cây hay không
def check_data_in_merkle(data, tree):
    data_hash = sha256(data)
    return data_hash in tree[0]  # Tầng đầu tiên là các hash lá

# ==== DEMO ====
if __name__ == "__main__":
    data_blocks = ["A", "B", "C", "D", "E"]
    tree = merkle_tree(data_blocks)

    print("\n🌲 Cây Merkle được tạo:")
    print_merkle_tree(tree)

    data_check = input("\n🔍 Nhập dữ liệu cần kiểm tra: ")
    if check_data_in_merkle(data_check, tree):
        print("✅ Dữ liệu tồn tại trong cây Merkle (nằm trong các lá).")
    else:
        print("❌ Dữ liệu không có trong cây.")
