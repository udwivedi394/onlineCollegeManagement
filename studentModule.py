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
            print("Check attendance")
        elif choice=='2':
            print("Check subjects")
        elif choice=='3':
            print("Check results")
        elif choice=='4':
            print("View/Edit profile")
        else:
            print("Wrong choice!")

def studentMenu(student):
    print("Hi! %s"%(student.user_details.first_name))
    print("1. Check attendance")
    print("2. Check subjects")
    print("3. Check results")
    print("4. View/Edit profile")
    print("5. Go back to previous menu")
    ch = input("Please enter your choice: ")
    return ch

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
