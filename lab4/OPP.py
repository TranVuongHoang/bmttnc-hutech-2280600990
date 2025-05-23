# SinhVien.py
class SinhVien:
    auto_id = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.id = SinhVien.auto_id
        SinhVien.auto_id += 1
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb

    def hoc_luc(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"{self.id} - {self.ten} - {self.gioi_tinh} - {self.chuyen_nganh} - {self.diem_tb} - {self.hoc_luc()}"

# QuanLySinhVien.py
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them(self, sv):
        self.danh_sach.append(sv)

    def cap_nhat(self, id_sv, **kwargs):
        for sv in self.danh_sach:
            if sv.id == id_sv:
                sv.ten = kwargs.get("ten", sv.ten)
                sv.gioi_tinh = kwargs.get("gioi_tinh", sv.gioi_tinh)
                sv.chuyen_nganh = kwargs.get("chuyen_nganh", sv.chuyen_nganh)
                sv.diem_tb = kwargs.get("diem_tb", sv.diem_tb)
                break

    def xoa(self, id_sv):
        self.danh_sach = [sv for sv in self.danh_sach if sv.id != id_sv]

    def tim_kiem(self, keyword):
        return [sv for sv in self.danh_sach if keyword.lower() in sv.ten.lower()]

    def sap_xep_diem(self):
        self.danh_sach.sort(key=lambda x: x.diem_tb, reverse=True)

    def sap_xep_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda x: x.chuyen_nganh)

    def hien_thi(self):
        for sv in self.danh_sach:
            print(sv)

# Main.py
def main():
    qlsv = QuanLySinhVien()

    while True:
        print("\n1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp theo điểm trung bình")
        print("6. Sắp xếp theo chuyên ngành")
        print("7. Hiển thị danh sách")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            ten = input("Tên: ")
            gt = input("Giới tính: ")
            cn = input("Chuyên ngành: ")
            dtb = float(input("Điểm TB: "))
            sv = SinhVien(ten, gt, cn, dtb)
            qlsv.them(sv)
        elif chon == "2":
            id_sv = int(input("Nhập ID: "))
            ten = input("Tên mới: ")
            gt = input("Giới tính mới: ")
            cn = input("Chuyên ngành mới: ")
            dtb = float(input("Điểm TB mới: "))
            qlsv.cap_nhat(id_sv, ten=ten, gioi_tinh=gt, chuyen_nganh=cn, diem_tb=dtb)
        elif chon == "3":
            id_sv = int(input("Nhập ID cần xoá: "))
            qlsv.xoa(id_sv)
        elif chon == "4":
            keyword = input("Nhập tên: ")
            for sv in qlsv.tim_kiem(keyword):
                print(sv)
        elif chon == "5":
            qlsv.sap_xep_diem()
        elif chon == "6":
            qlsv.sap_xep_chuyen_nganh()
        elif chon == "7":
            qlsv.hien_thi()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
