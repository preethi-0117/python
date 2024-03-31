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

def names(name,emails):
    print(name+" "+emails)

names(my_resume["name"],my_resume["email"])

def wel():
    print("hello preeth")

wel()