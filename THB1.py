#TranVuongHoang-2280600990
#khai báo biến trong py
age=21 #10.5 thi se la so thuc => 
name="bao" #kieu string
student=True #kieu boolean
#chuong trinh tu dinh dang kieu du lieu cho bạn bang gia tri bien do 
print(age,name,"co phai la hoc sinh khong: ",student)
#Toán tử
#1.cộng
a=3
b=5
sum=a+b
print (sum) #output= 8 
#2.trừ
a=8
b=4
minus=a-b
print(minus) #output= 4
#3.nhân
a=3
b=9
multipli=a*b
print(multipli) #output= 27
#4.chia
a=27
b=3
divide=a/b
print(divide) #output= 9
#5.chia lấy phần nguyên
a=27
b=4
result=a//b
print(result) #output= 6 
#6. chia lấy dư
a=27
b=4
result=a%b
print(result) #output= 3 (27/4=6 dư 3)
#7. luỹ thừa
a=3
b=2
result=a**b
print(result) #output= 9 (3^2=9)


#toán tử logic
#1. phép AND
if age<18 and student: 
    print("chưa đủ điều kiện lái xe")
else: print("đủ điều kiện lái xe")
#output= đủ điều kiện lái xe .Phép "and" yêu cầu phải đủ 2 điều kiện mới thực thi
#khai báo biến trong py
age=21 #10.5 thi se la so thuc => 
name="bao" #kieu string
student=True #kieu boolean
#chuong trinh tu dinh dang kieu du lieu cho bạn bang gia tri bien do 
print(age,name,"co phai la hoc sinh khong: ",student)
#Toán tử
#1.cộng
a=3
b=5
sum=a+b
print (sum) #output= 8 
#2.trừ
a=8
b=4
minus=a-b
print(minus) #output= 4
#3.nhân
a=3
b=9
multipli=a*b
print(multipli) #output= 27
#4.chia
a=27
b=3
divide=a/b
print(divide) #output= 9
#5.chia lấy phần nguyên
a=27
b=4
result=a//b
print(result) #output= 6 
#6. chia lấy dư
a=27
b=4
result=a%b
print(result) #output= 3 (27/4=6 dư 3)
#7. luỹ thừa
a=3
b=2
result=a**b
print(result) #output= 9 (3^2=9)


#------------------------------------------------------------------
#toán tử logic
#1. phép AND
if age<18 and student: 
    print("chưa đủ điều kiện lái xe")
else: print("đủ điều kiện lái xe")
#output= đủ điều kiện lái xe .Phép "and" yêu cầu phải đủ 2 điều kiện mới thực thi
#2. phép OR
a=5 
b=2
result=(a>3) or (b>10)
print(result) #output= true .Phép OR trả về true nếu ít nhất 1 trong 2 đúng
#3.Phép NOT 
a=10
result=not(a==1)
print(result) #output= true. Phép NOT trả về true nếu điều kiện là false và ngược lại
#4.Phép so sánh bằng
a=100
result=(a==100)
print(result) #output= true. Phép so sánh bằng(==) trả về true khi so sánh 2 giá trị có bằng nhau hay không 
#5.Phép so sánh không bằng
a=100
result=(a!=50)
print(result) #output= true. Phép so sánh không bằng (!=) trả về true khi so sánh 2 giá trị có khác nhau hay không
#6.phép so sánh lớn,nhỏ
a=10
b=20
result1=(a>b)
result2=(a<b)
print(result1) #output= false. 
print(result2) #output= true
#">" so sánh phần từ bên trái có lớn hơn bên phải không
#"<" so sánh phần từ bên trái có nhỏ hơn bên phải không
#7.Phép so sánh lớn hơn hoặc bằng
x=5
result=(x>=5)  #output= true
print(result2) #output= false
result2(x<=5)

#------------------------------------------------------------------
#Nhập xuất dữ liệu 
# Hàm input(): nhập dữ liệu từ bàn phím (luôn là kiểu chuỗi)
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

# Hàm print(): xuất dữ liệu ra màn hình, có thể dùng f-string để định dạng
tuoi = 21
print(f"{name} năm nay {tuoi} tuổi.")

# 1.2.6 Cấu trúc điều khiển
# Câu lệnh điều kiện if - elif - else
diem = float(input("Nhập điểm của bạn: "))
if diem >= 8:
    print("Loại Giỏi")
elif diem >= 6.5:
    print("Loại Khá")
elif diem >= 5:
    print("Loại Trung bình")
else:
    print("Loại Yếu")
# Vòng lặp for
print("In các số từ 1 đến 5:")
for i in range(1, 6):
    print(i)

# Vòng lặp while
n = 5
while n > 0:
    print("Số:", n)
    n -= 1

# Lệnh break, continue, pass
for i in range(10):
    if i == 5:
        break  # thoát vòng lặp
    print("break loop:", i)

for i in range(10):
    if i % 2 == 0:
        continue  # bỏ qua bước lặp nếu chẵn
    print("continue loop:", i)

for i in range(3):
    pass  # không làm gì cả
# 1.2.7 Chuỗi

# Khai báo chuỗi
chuoi1 = 'Hello'
chuoi2 = "World"
chuoi3 = '''Đây là
chuỗi nhiều dòng'''

# Truy cập ký tự chuỗi
print(chuoi1[0])  # H

# Cắt chuỗi
print(chuoi2[1:4])  # orl

# Ghép chuỗi
print(chuoi1 + " " + chuoi2)

# Độ dài chuỗi
print(len(chuoi1))  # 5

# Một số hàm xử lý chuỗi
text = "  Python Is Great!  "
print(text.upper())       # chữ hoa
print(text.lower())       # chữ thường
print(text.strip())       # xoá khoảng trắng đầu/cuối
print(text.split())       # tách chuỗi thành list
print(text.replace("Great", "Awesome"))  # thay thế

# 1.2.8 Hàm (Function)

# Hàm có trả về giá trị
def tinh_tong(a, b):
    return a + b

tong = tinh_tong(3, 4)
print("Tổng là:", tong)

# Hàm không trả về giá trị
def chao_hoi(ten):
    print("Chào bạn", ten)

chao_hoi("Nam")
# 1.3 Kiểu dữ liệu có cấu trúc
from array import array

# Mảng (Array)
arr = array('i', [1, 2, 3, 4])
print(arr[0])
arr.append(5)
print(arr)

# Danh sách (List)
ds = [1, 2, 3]
ds.append(4)
print(ds)
ds.remove(2)
print(ds)
ds[0] = 10
for x in ds:
    print(x)

# Tuple
t = (10, 20, 30)
print(t[1])
print(t.count(20))

# Dictionary
d = {"ten": "An", "tuoi": 21}
print(d["ten"])
d["lop"] = "CNTT"
del d["tuoi"]
print(d)

# 1.4 OOP trong Python

# Class và Object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Vios")
print(my_car.get_info())

# Kế thừa
class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

a = Dog()
a.make_sound()

# Đa hình
def animal_sound(animal):
    animal.make_sound()

animal_sound(Dog())

# Trừu tượng hoá
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

cat = Cat()
cat.make_sound()