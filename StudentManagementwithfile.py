import hashlib

teachers={}
students={}


#Hash pin
def hash_pin(pin):
    
    encoded_pin=str(pin).encode()

    hashed=hashlib.sha256(encoded_pin).hexdigest()

    return hashed


#Student Start/////////////////////////////////////////////////////////////////////////////////////
#Class of Student
class Student:
    def __init__(self,reg_no,name,pin):
        self.reg_no=reg_no
        self.name=name
        self.pin=pin
        self.enrollment=[]

#Add Student By Admin
def add_student():

    name=input("enter student name: ")
    reg_no=input("enter registration number: ")
    
    DEFAULT_HASH_Pin=hash_pin(reg_no)

    if reg_no in students:
        print("student with this registration number exist already\n")
        return

    students[reg_no]=Student(reg_no,name,DEFAULT_HASH_Pin)

    save_student_to_file()

    print(f"student with reg no:{reg_no} and name:{name} added successfully\n")


#View all or specific student To Admin
def view_student():

    if not students:
        print("No available student\n")
        return

    print("-------------------------")
    print("1.To view all student")
    print("2.To Search student")

    print("-------------------------\n")
    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid choice\n")
        return
    
    if(ch==1):
        print("Reg No   |Name")
        print("----------------------")
        for s_obj in students.values():
            print(f"{s_obj.reg_no}     |Name:{s_obj.name}")

        print("----------------------\n")

    elif(ch==2):  

        registration_no=input("enter registration no: ")

        if not registration_no:
            print("Student is not found\n")
            return
        
        print("-------------------------------")
        for reg_no,s_obj in students.items():
            if registration_no==reg_no:
                print(f"Registration number:{s_obj.reg_no} ")
                print(f"Name:{s_obj.name}")
                break
        print("-------------------------------\n")

    else:
        print("Invalid choice\n")

#Delete Student By Admin
def delete_student():

    if not students:
        print("No available student\n")
        return
    
    reg_no=input("enter registration no: ")

    if not reg_no in students:
        print("student with registration number not found\n")
        return
    
    s_obj=students[reg_no]

    for record in s_obj.enrollment:
        teacher=record.teacher
        if record in teacher.enrollment:
            teacher.enrollment.remove[record]

    del students[reg_no]

    save_marks_to_json()
    save_std_teacher_to_file()
    save_student_to_file()

    print(f"Student with registration no:({reg_no}) deleted successfully\n")


#Save Student Data To File
def save_student_to_file():
    try:
        with open("studentfileforSMS.txt","w") as f:
            for reg_no,s_obj in students.items():
                f.write(f"{reg_no},{s_obj.name},{s_obj.pin}\n")

    except FileNotFoundError:
        print("studentfileforSMS.txt is not found in saving\n")


#Load student From File
def load_student_from_file():
    try:
        with open("studentfileforSMS.txt","r") as f:
            for line in f:
                line=line.strip()

                if line=="":
                    continue

                parts=line.split(",")

                if len(parts)!=3:
                    print("Invalid line in loading student")
                    continue

                reg_no,name,pin=parts[:3]

                students[reg_no]=Student(reg_no,name,pin)
    except FileNotFoundError:
        print("studentfileforSMS.txt file not found while loading")


#Student End//////////////////////////////////////////////////////////////////////////////////////


#Teacher Start///////////////////////////////////////////////////////////////////////////////////

#Class Of Teacher
class Teacher:
    def __init__(self,teacher_id,name,subject_name,pin):
        self.teacher_id=teacher_id
        self.name=name
        self.subject_name=subject_name
        self.pin=pin
        self.enrollment=[]


#Add Teacher By Admin  
def add_teacher():
    
    try:
        teacher_id=int(input("enter teacher id: "))
    except:
        print("Invalid input\n")
        return
    
    if teacher_id in teachers:
        print("Teacher with this id present already\n")
        return
    
    name=input("enter name: ")
    subject_name=input("enter subject name: ")

    DEFAULT_PIN=hash_pin(teacher_id)
    
    teachers[teacher_id]=Teacher(teacher_id,name,subject_name,DEFAULT_PIN)

    save_teacher_to_file()

    print(f"Teacher with id:({teacher_id}) and Name:({name}) created successfully\n")


#View all and specific teacher To Admin
def view_teacher():

    if not teachers:
        print("No available teachers\n")
        return
    
    print("-------------------------")

    print("1.To view all teacher")
    print("2.To search teacher")

    print("-------------------------\n")
    
    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid choice\n")
        return
    
    if(ch==1):

        print("Teacher ID | Name       | Subject")
        print("----------------------------------")
        for t_id, t_obj in teachers.items():
            print(f"{t_obj.teacher_id}          | {t_obj.name}   | {t_obj.subject_name}")
        print("----------------------------------\n")
    
    elif(ch==2):

        teacher_id=int(input("enter teacher id: "))

        if not teacher_id in teachers:
            print("teacher is not found\n")
            return
        
        print("------------------------------")
        for t_id,t_obj in teachers.items():
            if t_id==teacher_id:
                print(f"Teacher id:{t_obj.teacher_id}")
                print(f"Name:{t_obj.name}")
                print(f"Subject:{t_obj.subject_name}")
                break
        print("------------------------------\n")


#Delete Teacher
def delete_teacher():

    if not teachers:
        print("no available teacher\n")
        return
    
    teacher_id=int(input("enter teacher id: "))

    if not teacher_id in teachers:
        print("Teacher is not found\n")
        return
    
    t_obj=teachers[teacher_id]
   
    for record in t_obj.enrollment:
        student=record.student
        if record in student.enrollment:
            student.enrollment.remove(record)
    

    del teachers[teacher_id]
    
    save_marks_to_json()
    save_std_teacher_to_file()
    save_teacher_to_file()

    print(f"Teacher with id:({teacher_id}) deleted successfully\n")


#View Student To Teacher Assign To Him
def view_std_to_teacher(t_obj):
    
    if not t_obj.enrollment:
        print("no student is assign to you\n")
        return
    
    print("------------------------")
    
    print("1.To View All Student")
    print("2.To Search Student")

    print("------------------------\n")
    
    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid input\n")
        return
    
    #View All Student
    if (ch==1):
        print("Name|       |Reg No")
        print("-------------------")

        for s in t_obj.enrollment:
            print(f"|{s.student.name},  |{s.student.reg_no}")

        print("-------------------\n")
    #View Specific Student
    elif(ch==2):
        found=False

        if not t_obj.enrollment:
            print("No student assign to you\n")
            return

        reg_no=input("enter registration no of student: ")  

        for s in t_obj.enrollment:
            if s.student.reg_no==reg_no:
                print("\n....Student Found....")
                print("-------------------------")

                print(f"Name:{s.student.name}")
                print(f"Registration no:{s.student.reg_no}")

                print("-------------------------\n")
                found=True
                break
        if not found:
            print("Student Not Found\n")
            return
    else:
        print("Invalid choice\n")


#Assigning Quiz Marks
def assign_quiz_marks(t_obj):
    found=False

    if not t_obj.enrollment:
        print("No student assign to you\n")
        return 
    
    reg_no=input("enter registration no of student: ")

    for s in t_obj.enrollment:
        if s.student.reg_no==reg_no:
            found=True

            quiz_no=int(input("enter quiz no: "))

            if quiz_no in s.quiz:
                print(f"Quiz no:{quiz_no} Already present.Overwriting.....")
            
            try:
                marks=int(input("enter quiz marks: "))

                if marks>10 or marks<0:
                    print("Marks must be between 10\n")
        
            except:
                print("Invalid marks.Marks must be number\n")
                return

            s.quiz[quiz_no]=marks

            print(f"Quiz:({quiz_no}) marks added successfully")

            save_marks_to_json()
            break
    if not found:
        print("Student not found\n")        


#Assigning Assignment Marks
def assign_assignment_marks(t_obj):
    found=False

    if not t_obj.enrollment:
        print("No student assign to you\n")
        return 
    
    reg_no=input("enter registration no of student: ")

    for s in t_obj.enrollment:
        if s.student.reg_no==reg_no:
            found=True

            assignment_no=int(input("enter assignmentt no: "))

            if assignment_no in s.assignment:
                print(f"Assignment no:{assignment_no} Already present.Overwriting.....")
            
            try:
                marks=int(input("enter assignment marks: "))

                if marks>10 or marks<0:
                    print("Marks must be between 10\n")
                    
            except:
                print("Invalid marks.Marks must be number\n")
                return
            
            s.assignment[assignment_no]=marks

            print(f"Assignment:({assignment_no}) marks added successfully\n")

            save_marks_to_json()
            break
    if not found:
        print("Student not found\n")    

#Assign Mid Marks
def assign_mid_marks(t_obj):
    found=False

    if not t_obj.enrollment:
        print("No student assign to you\n")
        return 
    
    reg_no=input("enter registration no of student: ")

    for s in t_obj.enrollment:
        if s.student.reg_no==reg_no:
            found=True

            try:
                marks=int(input("enter mid marks: "))

                if marks>25 or marks<0:
                    print("Marks must be between 25\n")
                    
            except:
                print("Invalid marks.Marks must be number\n")
                return
            
            if s.mid is not None:
                print("Mid Marks is assign already,Overwriting......\n")
    
            s.mid=marks

            print("Mid Marks Added Successfully")

            save_marks_to_json()
            break
    if not found:
        print("Student not found\n") 


#Assign Final Marks
def assign_final_marks(t_obj):
    found=False

    if not t_obj.enrollment:
        print("No student assign to you\n")
        return 
    
    reg_no=input("enter registration no of student: ")

    for s in t_obj.enrollment:
        if s.student.reg_no==reg_no:
            found=True

            try:
                marks=int(input("enter final marks: "))

                if marks>50 or marks<0:
                    print("Marks must be between 50\n")
                    continue

            except:
                print("Invalid input.Marks must be number\n")
                return

            if s.final is not None:
                print("Final Marks is assign already,Overwriting......\n")
    
            s.final=marks

            print("Final Marks Added Successfully\n")

            save_marks_to_json()
            break
    if not found:
        print("Student not found\n") 


#View Marks To Teacher 
def view_marks_of_student(t_obj):
   
    if not t_obj.enrollment:
        print("No Student is assign to you\n")
        return
   
    print("1.To View All Student Marks")
    print("2.To View Specific Student Marks")
    
    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid input\n")
        return
    
    print(f"\t\t\tTeacher Name:({t_obj.name})...Subject:({t_obj.subject_name})...\n")

    if (ch==1):
        print("Name      |Reg No   |Quiz Marks       |Assignment Marks       |Mid Marks  |Final Marks")
        print("----------------------------------------------------------------------------------------")

        for s in t_obj.enrollment:
            print(f"{s.student.name}  |{s.student.reg_no}     |{s.quiz}               |{s.assignment}                       |{s.mid}      |{s.final}|")
        print("-----------------------------------------------------------------------------------------")
    
    elif(ch==2):

        reg_no=input("enter registration no of student: ")
        found=False
        
        print(f"Teacher Name:({t_obj.name})...Subject:{t_obj.subject_name}...\n")
        for s in t_obj.enrollment:
            if s.student.reg_no==reg_no:
                found=True
                print("....Student Found....\n")
                print("---------------------------------------")
                print(f"Name:{s.student.name}")
                print(f"Registration no:{s.student.reg_no}")
                print(f"Quiz Marks:{s.quiz}")
                print(f"Assignment Marks:{s.assignment}")
                print(f"Mid Marks:{s.mid}")
                print(f"Final Marks:{s.final}")
                print("---------------------------------------\n")
                break

        if not found:
            print("student not found\n")
            return



#Marks writing and loading start///////////////////////////////////////////////////////////////////////////////////////
#Write Marks To File

import json
import os


# Save marks to JSON file
def save_marks_to_json():
    data = {}

    for teacher_id, teacher_obj in teachers.items():
        for record in teacher_obj.enrollment:
            reg_no = record.student.reg_no

            # Prepare marks dict
            marks_dict = {
                "quiz": record.quiz,           # {quiz_no: marks}
                "assignment": record.assignment, # {assignment_no: marks}
                "mid": record.mid,
                "final": record.final
            }

            # Unique key for each student-teacher pair
            data_key = f"{teacher_id}-{reg_no}"
            data[data_key] = {
                "teacher_id": teacher_id,
                "reg_no": reg_no,
                "marks": marks_dict
            }

    try:
        with open("marksfileforSMS.json", "w") as f:
            json.dump(data, f, indent=4)
      
    except Exception as e:
        print("Error saving marks:", e)



# Load marks from JSON file
def load_marks_from_json():
    if not os.path.exists("marksfileforSMS.json") or os.path.getsize("marksfileforSMS.json")==0:
        return

    try:
        with open("marksfileforSMS.json", "r") as f:
            data = json.load(f)

        for key, record_data in data.items():
            teacher_id = record_data["teacher_id"]
            reg_no = record_data["reg_no"]
            marks = record_data["marks"]

            if teacher_id in teachers and reg_no in students:
                # Check if this SubjectRecord already exists
                existing = None
                for rec in teachers[teacher_id].enrollment:
                    if rec.student.reg_no == reg_no:
                        existing = rec
                        break

                if existing:
                    record = existing
                else:
                    record = SubjectRecord(students[reg_no], teachers[teacher_id])
                    students[reg_no].enrollment.append(record)
                    teachers[teacher_id].enrollment.append(record)

                # Load marks
                record.quiz = {int(k): v for k, v in marks.get("quiz", {}).items()}
                record.assignment = {int(k): v for k, v in marks.get("assignment", {}).items()}
                record.mid = marks.get("mid")
                record.final = marks.get("final")

    except json.JSONDecodeError:
        print("Marks file corrupted. Starting fresh.")
    except Exception as e:
        print("Error loading marks:", e)




# Update marks function
def update_marks(t_obj):
    if not t_obj.enrollment:
        print("No student assigned to you\n")
        return

    reg_no = input("Enter registration number of student: ")
    found = False

    for record in t_obj.enrollment:
        if record.student.reg_no == reg_no:
            found = True
            print("---------------------------")

            print("1. Update Quiz Marks")
            print("2. Update Assignment Marks")
            print("3. Update Mid Marks")
            print("4. Update Final Marks")

            print("---------------------------\n")
            
            try:
                ch = int(input("Enter your choice: "))
            except:
                print("Invalid input\n")
                return
            
            if ch == 1:
                quiz_no = int(input("Enter quiz number: "))
                marks = int(input(f"Enter new marks for quiz {quiz_no}: "))

                record.quiz[quiz_no] = marks

                print("Quiz marks updated successfully!\n")

                save_marks_to_json()
                break

            elif ch == 2:
                assignment_no = int(input("Enter assignment number: "))
                marks = int(input(f"Enter new marks for assignment {assignment_no}: "))

                record.assignment[assignment_no] = marks

                print("Assignment marks updated successfully!\n")

                save_marks_to_json()
                break

            elif ch == 3:
                marks = int(input("Enter mid marks: "))

                record.mid = marks

                print("Mid marks updated successfully!\n")

                save_marks_to_json()
                break

            elif ch == 4:
                marks = int(input("Enter final marks: "))

                record.final = marks

                print("Final marks updated successfully!\n")

                save_marks_to_json()
                break

            else:
                print("Invalid choice\n")
                return

    if not found:
        print("Student not found\n")

#Marks writing and loading end///////////////////////////////////////////////////////////////////////////////////////


#Save Teacher Data To File 
def save_teacher_to_file():
    try:
        with open("teacherfileforSMS.txt","w") as f:

            for t_id,t_obj in teachers.items():
                f.write(f"{t_id},{t_obj.name},{t_obj.subject_name},{t_obj.pin}\n")

    except FileNotFoundError:
        print("teacherfileforSMS.txt not found during saving data\n")


#Load Teacher Data From File
def load_teacher_data():
    try:
        with open("teacherfileforSMS.txt","r") as f:
            for line in f:
                line=line.strip()

                if line=="":
                    continue

                parts=line.split(",")

                if len(parts)!=4:
                    print("Invalid line in loading teacher\n")
                    return
                
                teacher_id,name,subject_name,pin=parts[:4]

                teacher_id=int(teacher_id)

                teachers[teacher_id]=Teacher(teacher_id,name,subject_name,pin)
    except FileNotFoundError:
        print("teacherfileforSMS.txt not found while loading file\n")



#Teacher End///////////////////////////////////////////////////////////////////////////////////////


#Class of Marks 
class SubjectRecord:
    def __init__(self,student,teacher):
        self.student=student
        self.teacher=teacher

        self.quiz={}
        self.assignment={}
        self.mid=None
        self.final=None

    #Calculate quiz marks
    def calculate_quiz(self):

        quiz_marks=sum(self.quiz.values())

        return quiz_marks
    
    #Calculate assignment marks
    def calculate_assignment(self):

        assignment_marks=sum(self.assignment.values())

        return assignment_marks
    
    #Calculate mid marks
    def calculate_mid(self):
         
        if self.mid is not None:
            return self.mid
        
        else:
            return 0
        
    #Calculate final marks 
    def calculate_final(self):

        if self.final is not None:
            return self.final
        else:
            return 0
            
    #Total Quiz Marks
    def quiz_total(self):

        total_quiz=len(self.quiz)*10

        return total_quiz
    
    #Total Assignment Marks
    def assignment_total(self):

        total_assignment_marks=len(self.assignment)*10

        return total_assignment_marks
    
    


# Assign Student To Teacher
def assign_student_to_teacher():

    if not students:
        print("No available student\n")
        return
    
    if not teachers:
        print("No available teacher\n")
        return
    
    reg_no=input("enter student registration no: ")

    if not reg_no in students:
        print("student not found\n")
        return
    
    teacher_id=int(input("enter teacher id: "))

    s_obj=students[reg_no]
    t_obj=teachers[teacher_id]

    for record in s_obj.enrollment:
        if record.teacher.teacher_id==teacher_id:
            print("Student already enrolled in this subject\n")
            return
    
    record=SubjectRecord(s_obj,t_obj)

    s_obj.enrollment.append(record)
    t_obj.enrollment.append(record)

    save_std_teacher_to_file()

    print(f"({s_obj.name}) successfully enrolled in ({t_obj.subject_name}) teach by:{t_obj.name} \n")





#Save student + teacher to file
def save_std_teacher_to_file():
    try:
        with open("teacher+studentassignmentfile.txt","w") as f:
            for t_id,t_obj in teachers.items():
                for record in t_obj.enrollment:
                    f.write(f"{t_obj.teacher_id},{record.student.reg_no}\n")
        print("Student Assign Successfully\n")
    except FileNotFoundError:
        print("teacher+studentassignmentfile.txt is not found while saving\n")


#Load std + teacher from file
def load_std_teacher_file():
    try:
        with open("teacher+studentassignmentfile.txt","r") as f:
            for line in f:
                line=line.strip()

                if line=="":
                    continue

                parts=line.split(",")

                if len(parts)!=2:
                    print("Invalid Line in loadind student and teacher\n")
                    continue

                teacher_id,reg_no=parts[:2]

                teacher_id=int(teacher_id)

                if teacher_id in teachers and reg_no in students:
                    record=SubjectRecord(students[reg_no],teachers[teacher_id])

                    students[reg_no].enrollment.append(record)
                    teachers[teacher_id].enrollment.append(record)
    except FileNotFoundError:
        print("Assignment file not found. No assignments loaded.")

#//////////////////////////////////////////////////////////////////
load_teacher_data()
load_student_from_file()
load_std_teacher_file()
load_marks_from_json()
#//////////////////////////////////////////////////////////////////




#Admin Code Start////////////////////////////////////////////////////////////////////////////////////
admin_pin=[]

def change_admin_pin():

    old_pin=input("enter your old pin: ")

    if old_pin==admin_pin[0]:

        new_pin=input("enter new pin: ")
        confirm_pin=input("Confirm your pin: ")

        if new_pin==confirm_pin:
            admin_pin[0]=new_pin
            print("Password Change Successfully\n")

            write_admin_pin()
            return    
        else:
            print("Invalid confirm password\n")
    else:
        print("Wrong old pin\n")
       


#Admin Menu
def admin_menu():
    print("....Welcome To Admin Menu....")

    print("---------------------------")
    
    while True:
        print("1.To Add Teacher")
        print("2.To View Teacher")
        print("3.To Delete Teacher")
        print("4.To Add Student")
        print("5.To View Student")
        print("6.To Delete Student")
        print("7.Assign student to teacher")
        print("8.View Assign Student of Teacher")
       
        print("9.To Change Pin")
        print("10.To Logout")
        
        print("---------------------------\n")
        
        try:
            ch=int(input("enter your choice: "))
        except:
            print("Invalid Input\n")
            return
        
        match ch:
            case 1:
                add_teacher()
            case 2:
                view_teacher()
            case 3:
               delete_teacher()
            case 4:
                add_student()
            case 5:
                view_student()
            case 6:
                delete_student()
            case 7:
                assign_student_to_teacher()
            case 8:
                teacher_id=int(input("enter teaccher id: "))

                if teacher_id not in teachers:
                    print("no teacher found\n")
                    return
                
                t_obj=teachers[teacher_id]

                if not t_obj.enrollment:
                    print("No student assign to you\n")
                    return
                
                view_std_to_teacher(t_obj)
            case 9:
                change_admin_pin()
                return
            case 10:
                print("Thank You\n")
                break

#Admin Login
def admin_login():

    attempt=3

    while attempt>=1:
        pin=input("enter admin(pin): ")

        if(pin==admin_pin[0]):
            print("Login Successfully...")
            admin_menu()
            break
        else:
            attempt-=1
            print(f"Wrong Pin!Try Left:{attempt}")

      
#Save Admin Pin To File
def write_admin_pin():
    with open("adminpinfileforSMS.txt","w") as f:
        f.write(f"{admin_pin[0]}")
    
    print("Password change successfully\n")


#Load Admin Password
def load_admin_pin():
    try:
        with open("adminpinfileforSMS.txt","r") as f:
            pin=f.read().strip()

            if pin:
                admin_pin.append(pin)
            else:
                admin_pin.append("123")

    except FileNotFoundError:
        admin_pin.append("123") 


load_admin_pin()


#Admin Code End//////////////////////////////////////////////////////////////////////////////////////

#Start Teacher Menu/change pin//////////////////////////////////////////////////////////////////////////////////

def teacher_change_pin(t_obj):

    old_pin=input("enter your old pin: ")

    hash_old_pin=hash_pin(old_pin)

    if hash_old_pin==t_obj.pin:

        new_pin=input("enter new pin : ")
        hash_new_pin=hash_pin(new_pin)

        confirm_pin=input("confirm your pin: ")
        hash_confirm_pin=hash_pin(confirm_pin)

        if hash_new_pin==hash_confirm_pin:
            t_obj.pin=hash_new_pin

            save_teacher_to_file()
            print("Password Change Successfully\n")
        else:
            print("Invalid confirm pin\n")
    else:
        print("Wrong Old Password\n")


def teacher_menu(t_obj):

    print(f"....Welcome ({t_obj.name})....")

    while True:
        print("-------------------------------")

        print("1.View Student Assign To You")
        print("2.Assign Quiz marks")
        print("3.Assign Assignment Marks")
        print("4.Assign Mid Marks")
        print("5.Assign Final Marks")
        print("6.To Update Marks")
        print("7.View Marks Of Student")
        print("8.Change Password")
        print("9.To Logout")

        print("-------------------------------\n")

        try:
            ch=int(input("enter your choice: "))
        except:
            print("Invalid input\n")
            return
        
        match ch:

            case 1:
                view_std_to_teacher(t_obj)
            case 2:
                assign_quiz_marks(t_obj)
            case 3:
                assign_assignment_marks(t_obj)
            case 4:
                assign_mid_marks(t_obj)
            case 5:
                assign_final_marks(t_obj)
            case 6:
                update_marks(t_obj)
            case 7:
                view_marks_of_student(t_obj)
            case 8:
                teacher_change_pin(t_obj)
            case 9:
                print("Thanks You\n")
                return
            
            case _:
                print("Invalid choice\n")

#Teacher Login
def teacher_login():

    teacher_id=int(input("enter your id: "))

    if not teachers:
        print("no available teacher\n")
        return
    
    if not teacher_id in teachers:
        print("teacher not found\n")
        return
    
    t_obj=teachers[teacher_id]
    pin=input("enter your pin: ")

    hash_p=hash_pin(pin)

    if hash_p==t_obj.pin:
        print("Login Successfully....")
        teacher_menu(t_obj)
    else:
        print("Invalid pin\n")
#Teacher Meun End////////////////////////////////////////////////////////////////////////////



#View Marks To Student
def view_marks_to_student(s_obj):
    
     
    if not s_obj.enrollment:
        print("your not assign to any teacher\n")
        return
    
    print("----------------------------")

    print("1.To View All Subject Marks")
    print("2.View Specific Subject Marks")

    print("-----------------------------\n")

    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid input")
        return
    
    if ch==1:
    
        print("Teacher Name  |Subject    |Quiz Marks                 |Assignment Marks              |Mid Marks    |Final Marks")
        print("-----------------------------------------------------------------------------------------------------------------")
        for t in s_obj.enrollment:
            print(f"{t.teacher.name}      |{t.teacher.subject_name} |{t.quiz}                    |{t.assignment}                        |{t.mid}  |{t.final}\n")
        
        print("-----------------------------------------------------------------------------------------------------------------\n")
    
    elif ch==2:

        teacher_id=int(input("enter teacher id: "))
        
        if teacher_id not in teachers:
            print("Invalid teacher id\n")
            return
        
        found=False
        
        for t in s_obj.enrollment:
            if t.teacher.teacher_id==teacher_id:
                found=True
                print("Teacher name   |Subject     |Quiz                 |Assignment                      |Mid    |Final")
                print("--------------------------------------------------------------------------------------------------")
                print(f"{t.teacher.name}   |{t.teacher.subject_name}  |{t.quiz}           |{t.assignment}              |{t.mid}   |{t.final}")
                print("--------------------------------------------------------------------------------------------------\n")
                break

        if not found:
            print("You are not student of this teacher\n")
            return
    else:
        print("Invalid chocie\n")

#Calculate Percentage
def calculate_percentage(obtain_marks,out_of):

    percentage=(obtain_marks/out_of)*100

    return percentage


#Calculate Grade
def calculate_grade(percentage):

    if percentage>=85:
        return "A+"
    elif percentage>=80:
        return "A"
    elif percentage>=75:
        return "B+"
    elif percentage>=70:
        return "B"
    elif percentage>=65:
        return "C+"
    elif percentage>=60:
        return "C"
    elif percentage>=50:
        return "D"
    else:
        return "F"




#View Result
def view_result(s_obj):

    teacher_id=int(input("enter teacher id: "))

    if not teacher_id in teachers:
        print("Invalid teacher id\n")
        return   
    obtain_marks=0
    out_of=0
    found=False

    print("Teacher Name  |Subject   |Quiz Marks  |Assignment Marks  |Mid Marks  |Final Marks  |Total Marks  |Percentage  |Grade")
    print("---------------------------------------------------------------------------------------------------------------------")
    for record in s_obj.enrollment:
        if record.teacher.teacher_id==teacher_id:
            found=True

            quiz_marks=record.calculate_quiz()
            assignment_marks=record.calculate_assignment()
            mid_marks=record.calculate_mid()
            final_marks=record.calculate_final()
            #obtain marks
            obtain_marks+=quiz_marks+assignment_marks+mid_marks+final_marks
          
            total_quiz=record.quiz_total()
            total_assignment=record.assignment_total()
            #Marks got
            out_of+=total_quiz+total_assignment
            
            if mid_marks==0:

                out_of+=0
            else:
                out_of+=25

            if final_marks==0:
                out_of+=0
            else:
                out_of+=50

            percentage=calculate_percentage(obtain_marks,out_of)
            grade=calculate_grade(percentage)

            print(f"{record.teacher.name}      |{record.teacher.subject_name}     |{quiz_marks}/{total_quiz}       |{assignment_marks}/{total_assignment}              |{mid_marks}/25      |{final_marks}/50         |{obtain_marks}/{out_of}        |{percentage:.2f}%      |{grade}")
            print("---------------------------------------------------------------------------------------------------------------------\n")
    if not found:
        print("Invalid teacher id\n")        
            

#Change Password
def std_change_pin(s_obj):

    old_pin=input("enter your old pin: ")

    hash_old_pin=hash_pin(old_pin)

    if hash_old_pin==s_obj.pin:

        new_pin=input("enter new pin : ")
        hash_new_pin=hash_pin(new_pin)

        confirm_pin=input("confirm your pin: ")
        hash_confirm_pin=hash_pin(confirm_pin)

        if hash_new_pin==hash_confirm_pin:
            s_obj.pin=hash_new_pin

            save_student_to_file()
            print("Password Change Successfully\n")
        else:
            print("Invalid confirm pin\n")
    else:
        print("Wrong Old Password\n")


#Student Menu
def student_menu(s_obj):
    
    while True:
        print(f"...Welcome {s_obj.name}...")
        print("--------------------")

        print("1.To View Marks")
        print("2.To See Your Result")
        print("3.To Change Pin")
        print("4.To Logout")

        print("--------------------\n")

        try:
            ch=int(input("enter your choice: "))
        except:
            print("Invalid Input\n")

            return
        match ch:
            case 1:
                view_marks_to_student(s_obj)#966
            case 2:
                view_result(s_obj)
            case 3:
                std_change_pin(s_obj)
            case 4:
                print("Thank You\n")
                return
            case _:
                print("Invalid Choice")


#Student Login
def student_login():

    reg_no=input("enter your registration no: ")
    
    if  not reg_no in students:
        print("Invalid reg no\n")
        return
    
    s_obj=students[reg_no]
    
    pin=input("enter you pin: ")

    hash_p=hash_pin(pin)

    if hash_p==s_obj.pin:
        student_menu(s_obj)
    else:
        print("Invalid pin\n")
    
  
#Program Start
while True:
    print("....Welcome To Library System....")

    print("...............")

    print("1.For Admin")
    print("2.For Teacher")
    print("3.For Student")
    print("4.For Exit")

    print("...............\n")
    
    try:
        ch=int(input("enter your choice: "))
    except:
        print("Invalid Input\n")
        break
    
    match ch:
        
        case 1:
            admin_login()
        case 2:
            teacher_login()
        case 3:
            student_login()
        case 4:
            print("Thank you\n")
            break
        case _:
            print("Invalid Choice\n")
            



    