n=int(input("Nhap so gia phan tu cua list:"))
list=[]
for i in range(0,n,1):
    print("Nhap vao phan tu thu",i,":")
    x=input()
    list.append(x)  #them phan tu x vao cuoi list
print(list)
f=input("Nhap vao phan tu can dem:")
print(list.count(f))
#list.append(2,"here")  chen chuoi here vao vi tri so 2, co the thay append = insert
#list.pop(2) lay phan tu o vi tri so 2
#list.remove("here") xoa phan tu ra khoi chuoi
#list.reverse() dao chieu lop
#list.sort() sap xep mang theo thu tu tang dan
