class NhanVien:
    def __init__(self, ho_ten, tuoi, he_so_luong):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.he_so_luong = he_so_luong

    def tien_luong(self):
        return self.he_so_luong * 3000000


class CongTy:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_nhan_vien = {}
        self.id = 1

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien[self.id] = nhan_vien
        self.id += 1

    def xoa_nhan_vien(self, id):
        if id in self.danh_sach_nhan_vien:
            del self.danh_sach_nhan_vien[id]
        else:
            print("Nhan vien khong ton tai")

    def hien_thi_danh_sach(self):
        for id, nhan_vien in self.danh_sach_nhan_vien.items():
            print(f"ID: {id}, Ho ten: {nhan_vien.ho_ten}, Tuoi: {nhan_vien.tuoi}")

    def thong_ke_tuoi_lon_nhat(self):
        if not self.danh_sach_nhan_vien:
            return []
        max_tuoi = max(nhan_vien.tuoi for nhan_vien in self.danh_sach_nhan_vien.values())
        return [nhan_vien.ho_ten for nhan_vien in self.danh_sach_nhan_vien.values() if nhan_vien.tuoi == max_tuoi]

    def thong_ke_luong_trung_binh(self):
        if not self.danh_sach_nhan_vien:
            return 0
        tong_luong = sum(nhan_vien.tien_luong() for nhan_vien in self.danh_sach_nhan_vien.values())
        return tong_luong / len(self.danh_sach_nhan_vien)


# Test
vu = NhanVien('Vu Nguyen', 30, 1.5)
print('Ket qua 1:', vu.tien_luong())

print('\nKet qua 2:')
viettel = CongTy('Tap doan vien thong quan doi Viettel')
viettel.them_nhan_vien(vu)
viettel.them_nhan_vien(NhanVien('Yen', 25, 1))
viettel.them_nhan_vien(NhanVien('Trang', 20, 0.75))
viettel.them_nhan_vien(NhanVien('Quynh', 30, 2))
viettel.them_nhan_vien(NhanVien('Linh', 28, 2))
viettel.them_nhan_vien(NhanVien('Thu', 27, 1.25))
viettel.xoa_nhan_vien(3)
viettel.hien_thi_danh_sach()

print('\nKet qua 3:', viettel.thong_ke_tuoi_lon_nhat())
viettel.them_nhan_vien(NhanVien('Hoang', 35, 1.5))
print('\nKet qua 3:', viettel.thong_ke_tuoi_lon_nhat())

print('\nKet qua 4:', viettel.thong_ke_luong_trung_binh())
viettel.them_nhan_vien(NhanVien('Thinh', 19, 0.75))
print('\nKet qua 4:', viettel.thong_ke_luong_trung_binh())