equation = 'y=-12x+11111140.2121'
x = 2.5
chl1=equation[2:5]
chl2=equation[7:]
y = int(chl1)*x+float(chl2)
print('При x={xr} {eq}={yr}'.format(eq=equation, xr=x, yr=y))


