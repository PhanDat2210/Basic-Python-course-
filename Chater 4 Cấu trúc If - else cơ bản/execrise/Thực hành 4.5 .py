def tinh_cuoc_phi(so_km) :
    if so_km <=0:
        return "Invalid kilometer . please re-enter"
    
    # số km đầu tiên 15000 đ
    if so_km <=1 :
        return 15000
    
    #ừ km số 2 đến km30 là 13000đ
    if so_km >=2 and so_km <=30 :
        return 15000 +(so_km -1) * 13000
    
    #Nếu lớn hơn 30km thì mỗi km thêm sẽ là 10000đ
    if so_km > 30 :
        return 15000 +(so_km -1) * 13000 + (so_km - 30 ) * 10000

so_km = float (input("nhap so km : "))
tien_cuoc = tinh_cuoc_phi(so_km)
print(f"So tien phai tra :{tien_cuoc:.1f}VND") 