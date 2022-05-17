class Insect:
    def __init__(self,legs,wings,IsVenomous): #phuong thuc khoi tao
        self.legs=legs
        self.wings=wings
        self.IsVenomous=IsVenomous

    def showlegs(self):
        print("So chan la: ",self.legs) #Phuong thuc cua lop Insect

    def showwings(self):
        print("So canh la",self.wings)

dragonfly=Insect(6,4,"FALSE")
spider=Insect(8,0,"TRUE")
centipede=Insect(46,0,"TRUE")

class IsVariableEcology(Insect): #class con cua insect
    def __init__(self, legs, wings, IsVenomous):
        super().__init__(legs, wings, IsVenomous)
        
butterfly = IsVariableEcology(6,2,"FALSE") 

spider.showlegs()
dragonfly.showwings()
print(spider.IsVenomous)
butterfly.showlegs()