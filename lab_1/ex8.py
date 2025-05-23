# Câu 08: Kiểm tra số chia hết cho 5
values = input("Nhập các số, cách nhau bởi dấu phẩy: ")
nums = values.split(",")
result = [x for x in nums if int(x) % 5 == 0]
print(",".join(result))