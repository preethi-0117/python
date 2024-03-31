seema_mark=int(input("Enter seema mark:"))
jeena_mark=int(input("Enter jeena mark:"))
if seema_mark<jeena_mark:
    print("jeena is high scored")
elif seema_mark>jeena_mark:
    print("seema is high scored")
elif jeena_mark==seema_mark:
    print("both are equal")
else:
    print("invalid")


a=15  
b=23
if a>b:
    print("a is high number")

else:
    print("b is high number")


maths=60
english=80
tamil=93

if maths>50 and english>70:
    print("eligible")

maths=78
english=80

if maths>70 or english>85:
    print("selected")


science=99
social=80

if science>=95 and social>=80:
    print("good")

