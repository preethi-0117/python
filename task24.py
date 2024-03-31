a=int(input("first_value:"))


if a%5==0 and a%11==0:
    print(a,"is divided by 5 and 11")


else:
    print(a,"is not divided by 5 and 11")



b=int(input("value:"))

if b%5==0:
    print(b,"is divided by 5")

elif b%11==0:
    print(b,"is divided by 11")

elif b%5==0 and b%11==0:
    print(b," is divided by 5 and 11")

else:
    print(b,"is not divided by 5 and 11")