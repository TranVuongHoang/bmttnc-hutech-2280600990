# Câu 06: Tạo ma trận i*j
X = int(input("Nhập số hàng: "))
Y = int(input("Nhập số cột: "))
matrix = [[i * j for j in range(Y)] for i in range(X)]
print(matrix)