# Dictionary

# students={"Harry":"Gryffindor","Hermione":"Gryffindor","Ron":"gryffindor","Draco":"Slytherin"}
# for student in students:
#     print(student)
# for student in students:
#     print(student,":",students[student])

# List of dictionaries
Student= [{"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
          {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
          {"name":"Ron","house":"Gryffindor","patronus":" Jack Russell terrier"},
          {"name":"Draco","house":"Slytherin","patronus":None}]
n=1
for i in Student:
    print(n,":",i["name"],",",i["house"],",",i["patronus"])
    n+=1