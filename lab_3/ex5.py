# Câu 02:# Đếm số lần xuất hiện của phần tử trong list và lưu vào dictionary
lst = [1, 2, 2, 3, 3, 3, 4]
d = {}
for item in lst:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
print("Tần suất:", d)