from utility import dBconnectivity
from classes import memberModule as mM
import pymysql

def studentModule(user):
    student_attrib = check_user_as_student(user.id)
    if len(student_attrib)==4:
        student = mM.Student(user.id, user.user_id, student_attrib[0], 
                    student_attrib[1], student_attrib[2], student_attrib[3])
        user = None
    else:
        print("You're not enrolled as student")
        print("Do you want to register as student?(y/n) : ")
        ch = input()
        if ch.lower()=='y':
            print("Please signup")
            #signupform()
    end = False
    while end==False:
        choice = studentMenu(student)
        if choice=='5':
            end = True
        elif choice=='1':
            check_subjects(student)
        elif choice=='2':
            check_attendance(student)
        elif choice=='3':
            print("Check results")
        elif choice=='4':
            print("View/Edit profile")
        else:
            print("Wrong choice!")

def studentMenu(student):
    print("Hi! %s"%(student.user_details.first_name))
    print("1. Check subjects")
    print("2. Check attendance")
    print("3. Check results")
    print("4. View/Edit profile")
    print("5. Go back to previous menu")
    ch = input("Please enter your choice: ")
    return ch

def check_subjects(student):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
 
        print("Name: %-25s  Roll No: %-10d  Branch: %-4s  Current Semester: %-2d"%
            (student.user_details.first_name, student.std_roll_no, student.std_branch, student.semester))
        
        sem = student.semester
        while 1:
            sem = int(input('Enter the semester to view subjects: '))
            if sem > 8 or sem <= 0:
                print("Enter the correct Value")
            else:
                break

        sql1 = "SELECT D.subject_code, D.subject, D.credits FROM students A \
                JOIN branch B on A.std_branch = B.branch_code \
                JOIN branch_subjects C on A.std_branch = C.branch_code \
                JOIN subjects D on C.subject_code = D.subject_code \
                where std_roll_no=%s and C.semester=%d"%(student.std_roll_no,int(sem))        
        cur.execute(sql1)       

        ctr = 1
        print("%-6s|%-13s|%-45s|%11s"%('Sr.No.','Subject_Code','Subject_Name','Credits')) 
        for row in cur:
            print("%6d|%-13s|%-45s|%11.2f"%(ctr,row[0],row[1],row[2]))
            ctr += 1 
     
    except pymysql.OperationalError as e:
        print(e)
        return [] 

    except Exception as e:
        print(e)
        return []

    finally:
        cur.close()
        con.close()

def check_attendance(student):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
 
        print("Name: %-25s | Roll No: %-10d | Branch: %-4s | Semester: %-2d"%
            (student.user_details.first_name, student.std_roll_no, student.std_branch, student.semester))
        
        sem = student.semester
        while 1:
            sem = int(input('Enter the semester for which you want attendance: '))
            if sem > student.semester or sem <= 0:
                print("Enter the correct Value")
            else:
                break

        sql1 = "SELECT C.id, D.subject_code, D.subject FROM students A \
                JOIN branch B on A.std_branch = B.branch_code \
                JOIN branch_subjects C on A.std_branch = C.branch_code \
                JOIN subjects D on C.subject_code = D.subject_code \
                where std_roll_no=%s and C.semester=%d"%(student.std_roll_no,int(sem))        
        print(sql1)
        cur.execute(sql1)       

        cur2 = dBconnectivity.create_cursor(con)
        print("%-13s| %-45s|%11s|%7s"%('Subject_Code','Subject_Name','Net_Classes','Present')) 
        for row in cur:
            sql = "select count(*) from class_attendance_header where class_id=%d"%(row[0])
            cur2.execute(sql)
            
            tot_classes = 0
            for row2 in cur2:
                tot_classes = row2[0]

            sql = "select count(*) from class_attendance_header A \
                    JOIN class_attendance_details B on A.id = B.class_id \
                    where A.class_id=%d and B.student_roll_no=%d"%(row[0],student.std_roll_no)
            
            cur2.execute(sql)
            present = 0
            for row2 in cur2:
                present = row2[0]
            print("%-13s| %-45s|%11d|%7d"%(row[1],row[2],tot_classes,present)) 
        
        cur2.close()
     
    except pymysql.OperationalError as e:
        print(e)
        return [] 

    except Exception as e:
        print(e)
        return []

    finally:
        cur.close()
        con.close()


def check_user_as_student(id_i):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT std_roll_no, std_admission_year, std_semester, std_branch from students \
                where parent_user_id=%d"%(id_i)
        cur.execute(sql)
        for row in cur:
           return row 
        return []
       
    except pymysql.OperationalError as e:
        print(e)
        return []
    

    except Exception as e:
        print(e)
        return []

    finally:
        cur.close()
        con.close()
