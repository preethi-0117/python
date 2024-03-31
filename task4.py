a=int(input("age:"))
b=input("sex:(M/F):")
c=input("marital status:")



if (b=="male") and (20<a and 40>a) and (c=="yes" or "no"):
    print("work in anyplace")

elif (b=="male") and (40<a and 60>a) and (c=="yes" or "no"):
    print("work in urban areas")

elif (b=="female") and (0<a) and (c=="yes" or "no"):
    print("work in urban areas")

else:
    print("error")



