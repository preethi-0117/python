my_resume={
         
   
    "name":"Preethi.JP",
    "email":"preethi07@gmail.com",
    "date":"21-12-23",
    
    "experience":[{

        "company_name":"Tata",
        "years_of_experience":2,
    },
    
    {    "company_name":"HCL",
          "years_of_experience":3,
          }  
          ],
    "projects":[
        {"title":"financial analysis",
         "duration":"6 months",

        },
        {"title":"banking management",
         "duration":"5 months",
         
         }
    ],
    
     "objectives":"To secure a challenging position in a reputable organization to expand my learnings,knowledge, and skills",
    
    "academic_details":
     [{
      "course_name":"B.com",
      "institution_name":"Government arts&science college,konam",
      "percentage":80,
      "major":"commerce",
     },
       {"course_name":"12th",  
       "institution_name":"S.M.R.V.Hr.Sec.School",
       "percentage":90,
       "major":"commerce",

       }
    ],

    "certificate":{

                "course_name":"english typing",
                "year":2022,
    },
    "personal_information":{

        "date_of_birth":"17-10-2001",
        "father_name":"Prabhu.V",
        "mother_name":"Radha.M",
        "languages_known":"Tamil,English",
        "city":"Nagercoil",
        "pincode":"629 001",
        "hobbies":["Singing,Listening music"],
        "skills":["Active listening","hardworker"],
        "mobile":"+916576436766"
    },

"declaration":"I declare the above information are true",


}

print(my_resume["academic_details"][0])

print(my_resume["projects"][0])

print(my_resume["personal_information"]["languages_known"])

print(my_resume["academic_details"][0]["institution_name"])
     

    
print(my_resume["name"])



def name(name,email):
    print(name+" "+email)

name(my_resume["name"],my_resume["email"])

def wel():
    print("hello preeth")

wel()

wel()

def add():
    a=int(input())
    b=int(input())
    print(a+b)  

add()


def my_function(a):
    print(a+"Antony")

my_function("Pradeep")
my_function("Mark")

def my_function(fname,lname):
    print(fname+" "+lname)

my_function("Abdul","Kalam")
my_function("Rangu","Rangama")

def my_function(fname,lname):
    print(fname+" "+lname)

my_function("Seetha","Ki")

def my_function(*kids):
    print("the youngest child is "+kids[2])

my_function("Bingu", "Jingu", "Rangu")

def my_function(child1,child2,child3):
    print("the youngest child is "+ child3)

my_function(child1="Raji",child2="Lachu",child3="Suji")


def my_function(**kid):
    print("his last name is "+kid["lname"])
    
my_function(fname="Ammu",lname="kutty")

def my_function(country="Norway"):
    print("I am from "+country)
 
my_function()
my_function("India")
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)

fruits=["apple","banana","grapes"]

my_function(fruits)




def my_function(x,/):
    print(x)

my_function(3)
my_function(4*5)


def my_function(*, x):
    print(x)

my_function(x=3)



def add():
    pass
    a=int(input("enter 1:"))
    b=int(input("enter 2:"))
    c=int(input("enter 3:"))
    print(a+b+c)
add()


def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(4))



def my_function(x):
    print(x)

my_function(x=3)

def my_function(x,/):
    print(x)
my_function(3)

a=[1,2,3]
for each in a:
    print(each)
a.append(7)
for each in a:
    print(each)

a=["apple,Orange,Grapes"]
for each in a:
    print(each)


a.remove("apple")
for each in a:
    print(each)

a[0]="apple"
for each in a:
 a[len(a)-1]="kiwi"

print(each)


my_details={"name":"Preethi",
            "age":22,
            "place":"Nagercoil"
            },
print(my_details)

my_details.append("date-of-birth=17.10.2001")
my_details["Date_of_birth"]="17.10.2001"
print(my_details)


print(my_details)                             