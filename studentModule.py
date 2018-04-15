from utility import dBconnectivity
from classes import memberModule as mM
import datetime
import pymysql

def studentModule(user):
    student_attrib = check_user_as_student(user.id)
    if len(student_attrib)==5:
        student = mM.Student(user.id, user.user_id, student_attrib[0], 
                    student_attrib[1], student_attrib[2], student_attrib[3], student_attrib[4])
        user = None
    else:
        print("You're not enrolled as student")
        ch = input("Do you want to register as student?(y/n) : ")
        if ch.lower()=='y':
            print("Please signup")
            ret = student_signup_form(user)
            if ret == 1:
                print("Signup successful. Login again!")
            elif ret == -1:
                print("Some error occured!")
            else:
                pass
            return
        else:
            return
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
            check_results(student)
        elif choice=='4':
            view_student_profile(student)
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

def view_student_profile(student):
    print("\n\n")
    print("Name          : %-30s %-10s : %s"%(student.user_details.first_name+' '+student.user_details.last_name,
                                        'User ID',student.user_id))
    print("Email         : %-30s %-10s : %s"%(student.user_details.email,'Gender',student.user_details.gender))
    print("Roll No       : %-30s"%(student.std_roll_no))
    print("Admission Year: %-30s %-10s : %d"%(student.std_admission_year,'Semester',student.semester))
    print("Branch        : %s"%(student.branch_name))
    print("\n\n")
    return 

def student_signup_form(user):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)

        sql = "SELECT branch_code, branch_name FROM branch"
        cur.execute(sql)

        branch_dict = {}
        for row in cur:
            branch_dict[row[0]]=row[1]

        print('Available Branches in our college: ')
        for key in branch_dict:
            print("%-6s:%s"%(key,branch_dict[key]))
        
        while 1:
            branch = input("Enter branch code from above list (xxx to exit): ")
            if branch=='xxx':
                return
            elif branch_dict.get(branch)==None:
                print("Wrong Choice!")
            else:
                break

        sql = "SELECT max(std_roll_no) FROM students"
        cur.execute(sql)
        
        for row in cur:
            pass

        max_id = int(row[0])+1
        
        sql = "INSERT INTO students (parent_user_id, std_roll_no,\
                 std_admission_year, std_semester, std_branch) VALUES \
                (%d,%d,%d,%d,'%s')"%(user.id,max_id,datetime.datetime.now().year,1,branch)
        cur.execute(sql)
        con.commit()

    except pymysql.OperationalError as e:
        print(e)
        return -1

    except Exception as e:
        print(e)
        return -1

    finally:
        cur.close()
        con.close()

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

def check_results(student):
    ch = input("Enter the semester to view the result: ")
    if ch.isdigit()==False or int(ch)<0 or int(ch)>student.semester:
        print("Wrong Semster!")
        return

    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        print("\n\n\nName: %s %s"%(student.user_details.first_name, student.user_details.last_name))
        print("Roll. No.: %d"%(student.std_roll_no))
        print("Course: B.Tech. %s\n"%(student.branch_name))
        
        print("Semester %s Details"%(ch))
        print("%-10s|%-30s|%-18s|%-18s|%-14s|%-14s|%-6s"%('Paper Code','Paper Name','Max Internal Marks',
            'Max External Marks','Internal Marks','External Marks','Credits'))

        sql = "SELECT B.subject_code, B.subject, A.max_internal_marks,\
                A.max_external_marks, A.internal_marks, A.external_marks, A.credits\
                FROM stu_subject_marks A\
                JOIN subjects B ON B.subject_code = A.subject_code\
                where A.student_roll_no=%s and A.semester=%d"%(student.std_roll_no,int(ch))
        
        cur.execute(sql)
        ctr = 0

        for row in cur:
            print("%-10s|%-30s|%18s|%18s|%14s|%14s|%6s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            ctr += 1

        sql = "SELECT sem_%d_status FROM stu_semwise_status\
                WHERE std_roll_no=%s"%(int(ch),student.std_roll_no)
        cur.execute(sql)
        
        for row in cur:
            status = row[0]
            
        if status not in ('PASS','FAIL') and ctr!=0:
            status = 'IN PROGRESS'
 

        print("\nStatus: %s\n\n"%(status))
        return

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
        sql = "SELECT A.std_roll_no, A.std_admission_year, A.std_semester, \
                A.std_branch, B.branch_name FROM students A\
                JOIN branch B ON B.branch_code=A.std_branch\
                WHERE parent_user_id=%d"%(id_i)
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
