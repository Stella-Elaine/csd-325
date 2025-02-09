import json
def student_json():
   with open('student.json') as f:
        n = 0
        students = json.load(f)
        try:
            while True:
                last_name = students[n]["L_Name"]
                first_name = students[n]["F_Name"]
                id = students[n]["Student_ID"]
                email = students[n]["Email"]
                print(f"{last_name}, {first_name} : ID {id}, Email = {email}")
                n = n + 1
        except IndexError as err:
            exit
            
def stella_student
{
	"Name": "stella",
	"Age": 28,
	"Email": "stella@gmail.com"
}

append()
            #add your last name, first name, fictional ID, and email to the class list using append().
student_json()