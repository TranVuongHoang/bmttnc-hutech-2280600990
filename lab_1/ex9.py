# Câu 09: Kiểm tra số nguyên tố
num = int(input("Nhập một số: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "không phải là số nguyên tố.")
            break
    else:
        print(num, "là số nguyên tố.")
else:
    print(num, "không phải là số nguyên tố.")
