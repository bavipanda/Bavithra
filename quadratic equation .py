import cmath
a,b,c=map(int,input().split())
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('{0} and {1}'.format(sol1,sol2))
