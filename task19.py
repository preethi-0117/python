mark_1=int(input("physics:"))
mark_2=int(input("chemistry:"))
mark_3=int(input("biology:"))
mark_4=int(input("mathematics:"))
mark_5=int(input("computer:"))
percentage=(mark_1+mark_2+mark_3+mark_4+mark_5)/500*100


if percentage>=90:
    print("Grade A")   

elif percentage>=80:
    print("Grade B")  

elif percentage>=70:
    print("Grade C")  

elif percentage>=60:
    print("Grade D")  

elif percentage>=40:
    print("Grade E")  

elif percentage<40:
    print("Grade F")  








