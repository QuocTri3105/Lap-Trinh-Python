# 1.	Sử dụng ngôn ngữ Python viết chương trình chấp nhận đầu vào là một câu,
#  đếm số chữ cái và chữ số trong câu đó.

x=input('Nhap vao mot cau bat ki: ')
countalpha=0
countdigit=0
for i in (x):
    if i.isalpha()==True:
        countalpha=countalpha+1
    if i.isdigit()==True:
        countdigit=countdigit+1
print('So chu cai trong cau la: ', countalpha)
print('So chu so trong cau la: ',countdigit)
