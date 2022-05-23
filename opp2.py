class SinhVien:
    def __init__(self,ten,lop,diem,truong):
        self.ten=ten
        self.lop=lop
        self.diem=diem
        self.truong=truong


    def show(self):
        print("Ten sinh vien:",self.ten)
        print("Lop: ", self.lop)
        print("Diem sinh vien: ",self.diem)
        print("Truong: ",self.truong)

cd=[]
def nhap():
    n=int(input('Nhap vao so sinh vien :'))
    for i in range (n):
        print("Sinh vien thu",i+1)
        ten=input("Ten sinh vien: ")
        lop=input("Lop: ")
        diem=float(input("Nhap diem: "))
        truong=input("Nhap truong: ")
        print("-----------------------------------------------")
        sv=SinhVien(ten,lop,diem,truong)
        cd.append(sv)

def xuat():
    i=1
    for sv in cd:
        print("Thong tin cua sinh vien thu ",i)
        sv.show()
        i=i+1
        print(sv.diem)

def fmax():
    dmax=cd[0].diem #max = thuoc tinh "diem" cua phan tu thu 0 trong mang cd ( cd=[(ten,lop,diem,truong), (),....] )
    imax=0
    for i in cd:
        if (cd[i].diem<dmax):
            dmax=cd[i].diem
            imax=i
    cd[imax].show()
