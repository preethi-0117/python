a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

d=b**2-4*a*c
d1=d**0.5

if (d<0):
    print("the roots are imaginary")

else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("the first root:",round(r1,2))
    print("the second root:", round(r2,2))