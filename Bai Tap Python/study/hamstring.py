from gettext import find


string = "i love cats"
print(string.capitalize())
#ghi hoa chu cai dau
print(string.center(25,"_"))
#center chuoi bang 1 ki tu
print(string.count("ove",0))
#dem so lan chuoi con xuat hien trong chuoi trong khoang (start,end)
print(string.find("ove",0,11))
#tim vi tri chuoi con trong chuoi, neu co tra ve vi tri, neu khong tra ve -1
print("12334".isdigit())
#kiem tra se chuoi co chua chi so hay khong, neu cos ki tu khac so tra ve false
print(string.replace("cats","dogs"))
#thay the 1 doan bang 1 doan khac
print(string.strip("love"))
#loai bo cac ki tu giong nhau o dau va cuoi chuoi
print(string.split())
#tach cac tu tu chuoi
