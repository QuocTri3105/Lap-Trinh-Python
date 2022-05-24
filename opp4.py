class QuanLiCD:
    def __init__(self, tenCD,soBH,tenCS,gia):
        self.tenCD=tenCD
        self.soBH=soBH
        self.tenCS=tenCS
        self.gia=gia

    def show(self):
        print("-----------------------------------------------------------")
        print(self.tenCD," - ",self.soBH," - ",self.tenCS," - ",self.gia)
a=[]
n=int(input("Nhap so luong cd: "))
def nhap():
    for i in range (n):
        tenCD=input("Nhap ten CD: ")
        soBH=int(input("Nhap so bai hat: "))
        tenCS=input("Nhap ten ca si: ")
        gia=input("Nhap gia CD: ")
        print("------------------------------------------")
        ttbh=QuanLiCD(tenCD,soBH,tenCS,gia)
        a.append(ttbh)
def xuat():
    for i in range (n):
        print("Thong tin CD ",i+1,": ")
        a[i].show()

def tongtien():
    tong=0
    for i in a:
        tong =tong+i.gia
    print("Tong gia la: ",tong)

nhap()
xuat()
while True:
    print("Tiep tuc nhap:\n 1. Co\n0. Khong")
    choice=int(input())
    if choice==1:
        nhap()
        xuat()
    if choice==0:
        break
