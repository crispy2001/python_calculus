import pylab
from math import*
from numpy import*
import matplotlib.pyplot as plt
def taylor(k):
    if(k==0):
        return 0
    if(k%2!=0):
        return x**(2*k)/fun(2*k-1)+taylor(k-1)
    elif(k%2==0):
        return -(x**(2*k)/fun(2*k-1))+taylor(k-1)
def fun(x):
    total=1
    for i in range(1,x+1):
        total*=i
    return total

ax = plt.axes([0, 0, 2, 1.375])
ax.set_xlim(-7,7)
ax.set_ylim(-6,2)
x=linspace(-2*pi,2*pi,10000)


y=x*sin(x)
y1=taylor(1)
y2=taylor(2)
y3=taylor(3)
y4=taylor(4)
y5=taylor(5)
y6=taylor(6)
y7=taylor(7)
y8=taylor(8)
y9=taylor(9)
y10=taylor(10)



pylab.plot(x,y1,label="P2")
pylab.plot(x,y2,label="P4")
pylab.plot(x,y3,label="P6")
pylab.plot(x,y4,label="P8")
pylab.plot(x,y5,label="P10")
pylab.plot(x,y6,label="P12")
pylab.plot(x,y7,label="P14")
pylab.plot(x,y8,label="P16")
pylab.plot(x,y9,label="P18")
pylab.plot(x,y10,label="P20")
pylab.plot(x,y,label="x sin(x)")

ax.xaxis.set_major_locator(plt.MultipleLocator(2.0))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
pylab.title("Taylor polynomials with different orders for x sin(x)")

pylab.xlabel("x")
pylab.ylabel("y")
pylab.legend(loc="lower center")
pylab.show()
