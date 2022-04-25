def taxicost(qd):
    cost =0
    if 0<=qd<=2:
        cost=qd*150000
        print(cost)
    elif 2<=qd<=5:
        cost=qd*135000
        print(cost)
    elif 120>qd>=6:
        cost=qd*11000
        print(cost)
    elif qd>=120:
        cost=(qd*11000)-(qd*11000)/10
        print(cost)

qd=eval(input("Nhap quang duong da di:"))
taxicost(qd)
