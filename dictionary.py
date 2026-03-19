#store data in KEY:VALUE pairs
#use curly brackets

student = {
    "name" : "leo",
    "age": 23,
    "major" : "computer science"
}
print(student)
#accessing items
print(student["age"])
print(student.get("major"))

#adding items
student["graduation year"]=2025
print(student)

#changing value
student["age"] = 25

#remove value
student.pop("major")
print(student)

#check item existence
if "name" in student:
    print("yup")

    #nested dictionaries
    students = {
        "student1" : {"name": "leo", "age":22},
        "student2":{"name": "tim", "age": 42}
    }
    print(students["student2"]["age"])# access nested values

    report_card = {
        "name" : "tim", "subject": "math", "grades": (88,87,95)
    }
    average = sum(report_card["grades"]) / len(report_card["grades"])
    report_card["average"]=average
    print(report_card)
    if average > 89:
        print("EXCELLENT")
    elif average >69 and average <90:
        print("Good Job")
    else:print("keep trying")
