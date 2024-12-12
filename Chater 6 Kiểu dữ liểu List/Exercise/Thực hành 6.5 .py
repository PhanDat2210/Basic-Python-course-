def tinh_tong(list_con):
  """Tính tổng các giá trị trong một list con."""
  tong = 0
  for so in list_con:
    tong += so
  return tong

def tim_so_lon_nhat(list_con):
  """Tìm số lớn nhất trong một list con."""
  so_lon_nhat = list_con[0]
  for so in list_con:
    if so > so_lon_nhat:
      so_lon_nhat = so
  return so_lon_nhat

def tim_list_con_tong_lon_nhat(list_2d):
  """Tìm list con có tổng lớn nhất trong một list 2 chiều."""
  tong_lon_nhat = 0
  list_con_tong_lon_nhat = []
  for list_con in list_2d:
    tong_hien_tai = tinh_tong(list_con)
    if tong_hien_tai > tong_lon_nhat:
      tong_lon_nhat = tong_hien_tai
      list_con_tong_lon_nhat = list_con
  return list_con_tong_lon_nhat

def kiem_tra_so_nguyen_to(so):
  """Kiểm tra xem một số có phải là số nguyên tố hay không."""
  if so <= 1:
    return False
  for i in range(2, int(so**0.5) + 1):
    if so % i == 0:
      return False
  return True

def tim_so_nguyen_to_dau_tien(list_2d):
  """Tìm số nguyên tố đầu tiên trong một list 2 chiều."""
  for list_con in list_2d:
    for so in list_con:
      if kiem_tra_so_nguyen_to(so):
        return so
  return None

# Ví dụ:
a = [[8,12,9], [4, 10, 13], [15, 8, 20], [12, 11, 10]]

# Kết quả 1: Tổng của tất cả các giá trị trong list
tong_tat_ca = 0
for list_con in a:
  tong_tat_ca += tinh_tong(list_con)
print("Kết quả 1:", tong_tat_ca)

# Kết quả 2: Số lớn nhất trong list
so_lon_nhat = 0
for list_con in a:
  so_lon_nhat_hien_tai = tim_so_lon_nhat(list_con)
  if so_lon_nhat_hien_tai > so_lon_nhat:
    so_lon_nhat = so_lon_nhat_hien_tai
print("Kết quả 2:", so_lon_nhat)

# Kết quả 3: List con có tổng lớn nhất
list_con_tong_lon_nhat = tim_list_con_tong_lon_nhat(a)
print("Kết quả 3:", list_con_tong_lon_nhat)

# Kết quả 4: Số nguyên tố đầu tiên xuất hiện trong list
so_nguyen_to_dau_tien = tim_so_nguyen_to_dau_tien(a)
print("Kết quả 4:", so_nguyen_to_dau_tien)