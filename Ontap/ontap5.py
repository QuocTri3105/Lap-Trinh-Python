n=int(input('Nhap vao so sinh vien:'))
list=[n]
for i in range(n):
    print('Nhap vao ten sinh vien thu ',i,' : ')
    temp=input()
    list.append(temp)
ten=input('Nhap vao ten sinh vien can tim vi tri: ')
for i in range(n):
    if list[i]==ten:
        index = i-1
print('Sinh vien ',ten,' nam o vi tri thu',index,'trong list')
