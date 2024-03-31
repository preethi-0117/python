a=["amazon","apple","facebook","google","leetcode"]
b="e"
c="o"
def zeb(a):
    for i in a:
       if a==b and a==c:
         print("true")

       else:
            print("false")



def getname():
    return"ab"
name=getname()
print(name)

a=[1,2,3]
for each in a:
    print(each)

a.append(8)
for each in a:
    print(each)

list=["seenu","meenu","reenu"]
for each in list:
    print(each)
list.remove("seenu")
for each in list:
    print(each)

list[0]="Megna"
for each in list:
    print(each)

list=["a","b","c"]
list[len(list)-1]="d"
list[0]="k"
print(list)


def b():
    return" "
a=b()
print(a)


my_details={
           "name":"Preethi",
           "age":22,
           "place":"Nagercoil"
}

my_details["date_of_birth"]="17.10.2001"
my_details["age"]=21
my_details.pop("name")
my_details.pop("age")
print(my_details)