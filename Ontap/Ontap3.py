# 3.	Sử dụng ngôn ngữ Python viết chương trình nhập vào một danh sách số nguyên gồm n phần tử,
#        sau đó thực hiện:
#       -  Tính tổng phần tử là số lẻ trong danh sách;
#        -  Tìm vị trí của phần tử có giá trị lớn nhất trong danh sách.
list=[]
n=int(input("Nhap vao so luong phan tu:"))
for i in range(n):
    print("Nhap vao phan tu thu",i,":")
    x=int(input())
    list.append(x)
sumodds=0
for i in range(n):
    if list[i]%2==1:
        sumodds = sumodds + list[i]
print('Tong cac phan tu le la:',sumodds)
max=0
imax=0
for i in range(n):
    if max<list[i]:
        max=list[i]
        imax=i
print('Phan tu co gia tri lon nhat la ',max,'tai vi tri thu ',imax,' trong mang.' )
