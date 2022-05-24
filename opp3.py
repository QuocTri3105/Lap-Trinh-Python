class SinhVien:
    def __init__(self,ten,lop,diem,truong):
        self.ten=ten
        self.lop=lop
        self.diem=diem
        self.truong=truong
    def show(self):
        print("Ten sinh vien:",self.ten)
        print("Lop",self.lop)
        print("Diem",self.diem)
        print("Truong",self.truong)

a=[]
n =int(input("Nhap vao so sinh vien can quan li: "))
def nhap():
    for i in range (n):
        print("Nhap thong tin sinh vien thu ",i,":")
        ten=input("Nhap ten sinh vien: ")
        lop=input("Nhap lop:")
        diem=float(input("Nhap diem sinh vien: "))
        truong=input("Nhap truong: ")
        sv=SinhVien(ten,lop,diem,truong)
        a.append(sv)
def xuat():
    i=1
    for sv in a:
        print("Thong tin cua sinh vien thu ",i,":")
        sv.show()
        i=i+1

def xepdiem():
    for i in range(n):
        for j in range(n):
            if (a[i].diem > a[j].diem):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp

def xeploai():
    print("Nhung hoc sinh xep loai gioi la: ")
    for i in range (a):
        if (a[i].diem > 8):
            a[i].show()
