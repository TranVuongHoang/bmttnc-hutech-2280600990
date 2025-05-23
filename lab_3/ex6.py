# Câu 06: Xóa phần tử trong dictionary theo key
d = {"a": 1, "b": 2, "c": 3}
key_to_delete = input("Nhập key cần xóa: ")
if key_to_delete in d:
    del d[key_to_delete]
    print("Cập nhật dictionary:", d)
else:
    print("Key không tồn tại!")