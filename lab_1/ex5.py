# Câu 05: Tính lương nhân viên
hours = float(input("Nhập số giờ làm việc mỗi tuần: "))
rate = float(input("Nhập mức lương mỗi giờ: "))
if hours > 44:
    overtime = hours - 44
    salary = 44 * rate + overtime * rate * 1.5
else:
    salary = hours * rate
print("Lương thực nhận là:", salary)