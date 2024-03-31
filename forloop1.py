for each in range(10):
    #  print(each)
     if each==8:
         print(each,"is my lucky number")
        


for each in range(10):
    if each %2==0:
        print(each,"even")

    else:
         print(each,"odd")

for each in range(100):
    if each %3==0:
        print(each,"is divisible by 3")

for each in range(100):
    if each %3==0 and each %9==0:
        print(each,"is divisible by 3 and 9")

for each in range(100):
    if each %7==0 or each %13==0:
        print(each,"is divisible by 7 or 13")


for each in range(1,100):
      largest_no=0  
      if each>largest_no:
       largest_no=each
       print("largest number is",largest_no)



list=[5,16,7,2,18,1]
largestnumber=0
for each in list:
      
      if each>largestnumber:
       largestnumber=each
print("largest number is",largestnumber)


        
