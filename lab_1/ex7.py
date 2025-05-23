# Câu 07: In hoa các dòng nhập vào
lines = []
print("Nhập các dòng (nhập dòng trống để kết thúc):")
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
for line in lines:
    print(line)