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


resume={}
getname=input("name:")
resume["name"]=getname
email=input("email:")
resume["email"]=email


objectives=input("objectives:")
resume["objectives"]=objectives
declaration=input("declaration:")
resume["declaration"]=declaration
educational_qualification=int(input("Enter how many educational_qualification do you want to add?"))
resume["educational qualification"]=[]
for each in range(educational_qualification):
    course=input("Enter course name:")
    major=input("Enter major:")
    percentage=input("Enter percentage:")
resume["educational qualification"].append(
                                         {"course":course,
                                           "major":major,
                                           "percentage":percentage}
                                          )
experience=int(input("Enter how many experience do you want to add?"))
resume["experience"]=[]
for each in range(experience):
    name=input("company name:")
    years=input("years of experience:")
resume["experience"].append(
                            {
                             "name":name,
                             "years":years}
)
projects=int(input("Enter how many projects do you want to add?"))
resume["projects"]=[]
for each in range(projects):
    title=input("Enter project title:")
    subject=input("Enter subject:")
resume["projects"].append({
                           "title":title,
                           "subject":subject
                          })  

certificates=int(input("How many certificates do you want to add?"))
resume["certificate"]=[]
for each in range(certificates):
    course_name=input("Enter course name:")
    level=input("Enter level:")
    year=input("Enter year of completed:")
resume["certificate"].append({
                             "course name":course_name,
                             "level":level,
                             "year":year
                             })           

personal_details=(input("Enter your personal details:"))
resume["personal_details"]={}

date_of_birth=input("Enter your dob:")
resume["personal_details"]["date_of_birth"]=date_of_birth
father_name=input("Enter your father name:")
resume["personal_details"]["father_name"]=father_name
mother_name=input("Enter your mother name:")
resume["personal_details"]["mother_name"]=mother_name
city=input("Enter your city:")
resume["personal_details"]["city"]=city
pin_code=input("Enter your pincode:")
resume["personal_details"]["pin_code"]=pin_code
mobile=input("Enter your mobile:")
resume["personal_details"]["mobile"]=mobile
hobbies=input("Enter your hobbies:")
resume["personal_details"]["hobbies"]=[].append(hobbies)
languages_known=input("Enter languages known:")
resume["personal_details"]["languages_known"]=[]
# resume["skills"]=[]
skills=input("Enter your skills:")
resume["personal_details"]["skills"]=[]
print(resume) 

