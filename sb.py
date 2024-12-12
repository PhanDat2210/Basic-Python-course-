from PIL import Image, ImageFilter

def resize_image(input_image_path, output_image_path):
    # Mở hình ảnh
    img = Image.open(input_image_path)
    
    # Chuyển đổi hình ảnh sang chế độ RGB nếu cần
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Kích thước mới của hình ảnh
    new_size = (128, )  # Đổi kích thước thành 128x64
    img_resized = img.resize(new_size)

    # Áp dụng bộ lọc unsharp_mask
    enhancer = ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
    img_resized = img_resized.filter(enhancer)

    # Lưu hình ảnh đã xử lý
    img_resized.save(output_image_path)

# Đường dẫn vào và ra
input_image_path = "C:/Users/datzi/Downloads/OIP.jpg"
output_image_path = "C:/Users/datzi/Downloads/1111ss1.jpg"

resize_image(input_image_path, output_image_path)
