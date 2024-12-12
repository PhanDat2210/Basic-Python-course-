import re

def extract_information(s):
    programing_languages = ["Python","Javascript","CPlusPlus","Java","CSharp"]
    results = {}  # Tạo một từ điển rỗng

    # ngôn ngữ lập trình
    results["Kết quả 1:"] = [item for item in programing_languages if item in s ]

    # Địa chỉ trang web
    results["Kết quả 2:"] = re.findall(r"http://[a-zA-Z0-9]+\.(?:com|vn)",s)

    #Địa chỉ email
    results["Kết quả 3:"] = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:com|vn)",s)

    #Chuỗi kí tự thời gian
    results["Kết quả 4:"] = re.findall(r"\d{2}:\d{2}:\d{2}|\d{2}-\d{2}-\d{2}",s)

    # Chuỗi số tăng liên tiếp
    results["Chuỗi số tăng"] = []
    for i in range(len(s)-2):
        if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit() and int(s[i]) + 1 == int(s[i+1]) and int(s[i+1]) + 1 == int(s[i+2]):
            results["Chuỗi số tăng"].append(s[i:i+3]) 
    return results

s="Python1234Vu_http://vunguyencoder.com123vunguyencoder@gmail.com5678Javascript111CPlusPlus17:05:300000xxx"
s1 = "xxxyyy000CSharp3421CPlusPlus18:09:4056789http://!!!abc@viettel.vnhttp://kenh14.vnnnnnnwwwwXXX1230004561X"

result1= extract_information(s)
result2= extract_information(s1)

print(result1)
print(result2)