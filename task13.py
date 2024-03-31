amount=float(input("total_amount:"))

option=int(input("enter your option:"))

if option==1:
    result=amount/500
    print("no.of 500 rupees notes:",result)

elif option==2:
    result=amount/200
    print("no.of 200 rupees notes:",result)

elif option==3:
    result=amount/100
    print("no.of 100 rupees notes:",result)

elif option==4:
    result=amount/50
    print("no.of 50 rupees notes:",result)

elif option==5:
    result=amount/10
    print("no.of 10 rupees notes:",result)