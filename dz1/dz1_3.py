#ax2+bx+c=0
import math
a=int(input('Enter a= '))
b=int(input('Enter b= '))
c=int(input('Enter c= '))
print(a,'x2+',b,'x+',c,'=0', sep='')
d = b**2-4*a*c
print('D= b2-4ac = ',d)
if (a==0) or (d < 0):
	print('No roots')
elif d==0:
	x=-b/(2*a)
	print(f'x1=x2={x}')
else:
	x1=(-b+math.sqrt(d))/(2*a)
	x2=(-b-math.sqrt(d))/(2*a)
	print(f'x1={x1}, x2={x2}')

