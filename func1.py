def add (a,b,c,d,e):
    f=a+b+c+d+e
    print(f)
add(5,7,2,9,7)                                                                                                                                                                                                    

def name(ini):
    print(ini+" "+"Preethi")

name("JP")

def add():
    print("Addition:")
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    
    print(a+b)


add()

def sub():
    print("subtraction:")
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    print(a-b)

sub()

def multi():
    print("multiplication:")
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    print(a*b)

def divide():
    print("division:")
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    print(a/b)
    
multi()

divide()

def number(a,b):
    if a %2==0 and b %2==0:
        print(a, "and", b ,"even number")

    else:
        print(a, "and", b ,"odd number")

number(50,17)

def a(b):
    if b %2==0:
        print("even")


c=10
a(c)

def passfail(a):
   
    if a<=34:
        print("fail")

    elif a>=35:
        print("pass")

stu=int(input("enter marks:"))

passfail(stu)

def passfail():
     a=int(input("Enter number:"))
     if a<=34:
        print("fail")

     elif a>=35:
        print("pass")

passfail()


def printrange(r1,r2):
  for i in range(r1,r2):
     print(i)

printrange(5,7)

def printrange(r1,r2):
  r1=int(input("enter a:"))
  r2=int(input("enter b:"))
  for i in range(r1,r2):
    print(i)

printrange(5,7)



def validate():
    s_username="EMC"
    s_password="123"

    uname=input("enter value for uname:")
    password=input("enter password:")
    if (s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)

def add(n1,n2):
    return n1+n2

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

added=add(a,b)
output=added*c
print(output)
