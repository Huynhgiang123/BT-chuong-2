print("Nhap hai canh ke cua tam giac vuong: ")
a=int(input())
b=int(input())
import math
x=a**2+b**2
d=round(math.sqrt(x),2)
print("Canh ke thu nhat la:" ,a,end=",")
print(" canh ke thu hai la:" ,b,end=",")
print(" co canh huyen =",d)