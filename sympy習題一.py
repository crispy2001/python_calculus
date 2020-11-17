from sympy import*
f=var("x")
f=cos(x)**3
f1=-3*sin(x)*cos(x)**2
f2=6*sin(x)**2*cos(x) - 3*cos(x)**3
f3=-6*sin(x)**3 + 21*sin(x)*cos(x)**2
f4=-9*cos(x)**3 + 6*cos(x)
f5=3*sin(x)**3 - 3*sin(x)
print("d/dx(cos(x)**3)\n","=",diff(f))
print("d/dx(-3*sin(x)*cos(x)**2)\n","=",diff(f1))
print("d/dx(6*sin(x)**2*cos(x) - 3*cos(x)**3)\n","=",diff(f2))
print("∫(6*sin(x)**2*cos(x) - 3*cos(x)**3)dx\n","=",integrate(f3,x))
print("∫(-9*cos(x)**3 + 6*cos(x))dx\n","=",integrate(f4,x))
print("∫(3*sin(x)**3 - 3*sin(x))dx\n","=",integrate(f5,x))
