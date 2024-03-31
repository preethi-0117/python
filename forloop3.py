students_details=[
                  { 
                   "name":"Jaanu",
                   "place":"Nagercoil",
                   "major":"Maths",
                   "marks":[{
                             "sub_name":"Tamil",
                             "max_marks":200,
                             "marks_scored":180
                            },
                            {
                             "sub_name":"English",
                             "max_marks":200,
                             "marks_scored":176
                            },
                            {
                             "sub_name":"Maths",
                             "max_marks":200,
                             "marks_scored":186
                            },
                            {
                             "sub_name":"Biology",
                             "max_marks":200,
                             "marks_scored":165
                            },
                            {
                             "sub_name":"Physics",
                             "max_marks":200,
                             "marks_scored":169
                            },
                            {
                             "sub_name":"Chemistry",
                             "max_marks":200,
                             "marks_scored":184
                            },
                             ],
                   "age":22,
                   "hobbies":["Singing","Listening music","Gardening","Art collecting","Drawing"],
                   "gender":"Female",
                   "NCC":"True",
                   "sports":["Volleyball","Hockey"],
                   "annual_income":94000,
                  },

                  { 
                   "name":"Teena",
                   "place":"Monday market",
                   "major":"Maths",
                   "marks":[{
                             "sub_name":"Tamil",
                             "max_marks":200,
                             "marks_scored":160
                            },
                            {
                             "sub_name":"English",
                             "max_marks":200,
                             "marks_scored":180
                            },
                            {
                             "sub_name":"Maths",
                             "max_marks":200,
                             "marks_scored":190
                            },
                            {
                             "sub_name":"Biology",
                             "max_marks":200,
                             "marks_scored":191
                            },
                            {
                             "sub_name":"Physics",
                             "max_marks":200,
                             "marks_scored":189
                            },
                            {
                             "sub_name":"Chemistry",
                             "max_marks":200,
                             "marks_scored":160
                            },
                             ],
                   "age":23,
                   "hobbies":["Cooking","Jewellery making","Gardening","Dancing","Playing"],
                   "gender":"Female",
                   "NCC":"False",
                   "sports":["Football","Volleyball"],
                   "annual_income":98000,
                  },

                  { 
                   "name":"Lavanya",
                   "place":"Vetturnimadam",
                   "major":"Maths",
                   "marks":[{
                             "sub_name":"Tamil",
                             "max_marks":200,
                             "marks_scored":156
                            },
                            {
                             "sub_name":"English",
                             "max_marks":200,
                             "marks_scored":158
                            },
                            {
                             "sub_name":"Maths",
                             "max_marks":200,
                             "marks_scored":162
                            },
                            {
                             "sub_name":"Biology",
                             "max_marks":200,
                             "marks_scored":165
                            },
                            {
                             "sub_name":"Physics",
                             "max_marks":200,
                             "marks_scored":175
                            },
                            {
                             "sub_name":"Chemistry",
                             "max_marks":200,
                             "marks_scored":172
                            },
                             ],
                   "age":22,
                   "hobbies":["Reading","Cycling","Dancing","Painting","Scrapbooking"],
                   "gender":"Female",
                   "NCC":"True",
                   "sports":["Hockey","Football"],
                   "annual_income":99000,
                  },

                  { 
                   "name":"Meena",
                   "place":"Meenakshipuram",
                   "major":"Maths",
                   "marks":[{
                             "sub_name":"Tamil",
                             "max_marks":200,
                             "marks_scored":182
                            },
                            {
                             "sub_name":"English",
                             "max_marks":200,
                             "marks_scored":179
                            },
                            {
                             "sub_name":"Maths",
                             "max_marks":200,
                             "marks_scored":185
                            },
                            {
                             "sub_name":"Biology",
                             "max_marks":200,
                             "marks_scored":169
                            },
                            {
                             "sub_name":"Physics",
                             "max_marks":200,
                             "marks_scored":168
                            },
                            {
                             "sub_name":"Chemistry",
                             "max_marks":200,
                             "marks_scored":186
                            },
                             ],
                   "age":23,
                   "hobbies":["Singing","Listening music","Chess","Handicraft","Video game"],
                   "gender":"Female",
                   "NCC":"True",
                   "sports":["Volleyball","Hockey"],
                   "annual_income":90000,
                  },
                  { 
                   "name":"Vidya",
                   "place":"Vadasery",
                   "major":"Maths",
                   "marks":[{
                             "sub_name":"Tamil",
                             "max_marks":200,
                             "marks_scored":156
                            },
                            {
                             "sub_name":"English",
                             "max_marks":200,
                             "marks_scored":166
                            },
                            {
                             "sub_name":"Maths",
                             "max_marks":200,
                             "marks_scored":180
                            },
                            {
                             "sub_name":"Biology",
                             "max_marks":200,
                             "marks_scored":171
                            },
                            {
                             "sub_name":"Physics",
                             "max_marks":200,
                             "marks_scored":178
                            },
                            {
                             "sub_name":"Chemistry",
                             "max_marks":200,
                             "marks_scored":180
                            },
                             ],
                   "age":23,
                   "hobbies":["Meditation","Baking","Painting","Exercise","Writing"],
                   "gender":"Female",
                   "NCC":"False",
                   "sports":["Volleyball","Football"],
                   "annual_income":59000,
                  },
            ]


for student in students_details:
  if student["annual_income"]<=60000: 
    print(student["name"],"annual income is less than 60000")
  elif student["age"]<24:
   print(student["name"],"less than 24")

for students in students_details:
 sum=0
 for each in students["marks"]:
  sum=sum+each["marks_scored"]
 print(students["name"],sum)
  
for students in students_details:
  sum=0
  for each in students["marks"]:
   sum=sum+each["marks_scored"]
  print(students["name"],sum,"percentage",sum/1200*100)

# for student in students_details:
#  maths_highest=0
#  for m in student["marks"]:
#    if m["sub_name"=="maths"]:
#     maths_highest=m["marks_scored"]+"maths_highest"
#    print(student["name"],maths_highest) 
   
