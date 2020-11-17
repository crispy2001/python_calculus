import pylab 
from numpy import*
import matplotlib.pyplot as plt


fig=plt.gcf()
fig.set_size_inches(18.5,10.5)

angs=linspace(0,10*pi,1000)
co=sin(2.3*angs)**2+cos(2.3*angs)**4

pylab.polar(angs,co,color="g")
pylab.title("graph of sin(2.3x)^2 + cos(2.3x)^4 for x ∈ (0,10pi)",color="r")


pylab.show()
