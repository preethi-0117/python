a=int(input("Enter amount of units:"))

if a<=50:
    amount=50*0.50
    print("amount to be paid:",amount)

elif 50<a<=150:
    amount=25+100*0.75
    print("amount to be paid:",amount)

elif 150<a<=250:
    amount=100+100*1.20
    print("amount to be paid:",amount)

elif a<250:
    amount=220+250
    surcharge=amount+0.20
    print("amount to be paid:",amount)