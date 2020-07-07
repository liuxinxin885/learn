from math import sqrt
n=input('请输入整数')
n=int(n)

for i in range(2,int(sqrt(n)+1)):
    if n%i!=0 and i<int(sqrt(n)):
        continue
    if n%i==0:
        print(n,'不是素数')
        break
    print(n,'是素数')