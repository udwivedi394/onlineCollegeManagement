from utility import dBconnectivity
from classes import memberModule as mM
from classes import objectModule as oM
import pymysql

def facultyModule(user):
    faculty_attrib = check_user_as_faculty(user.id)
    if len(faculty_attrib)==4:
        faculty = mM.Faculty(user.id, user.user_id, faculty_attrib[0], 
                    faculty_attrib[1], faculty_attrib[2], faculty_attrib[3])
        user = None
    else:
        print("You are not authorized on this page!")
        return
    end = False
    while end==False:
        choice = facultyMenu(faculty)
        if choice=='5':
            end = True
        elif choice=='1':
            faculty_subjects(faculty)
        elif choice=='2':
            upload_attendance(faculty)
        elif choice=='3':
            print("Upload Marks")
        elif choice=='4':
            print("View/Edit profile")
        else:
            print("Wrong choice!")
    return

def facultyMenu(faculty):
    print("Hi! %s"%(faculty.user_details.first_name))
    print("1. View your subjects")
    print("2. Upload attendance")
    print("3. Upload Marks")
    print("4. View/Edit Profile")
    print("5. Go back to previous menu")
    ch = input("Please enter your choice: ")
    return ch

def faculty_subjects(faculty):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT A.id,C.id,B.Subject_code,B.Subject,C.branch_code,C.semester \
                FROM faculty_subjects A \
                JOIN subjects B on B.Subject_code = A.subject_code \
                JOIN branch_subjects C on C.id = A.branch_subject_id \
                WHERE A.taught_by_faculty_id = '%s'"%(faculty.faculty_id)
        cur.execute(sql)
        
        subject_list = []
        ctr = 1
        for row in cur:
            temp_sub = oM.FacultySubject(row[0],row[1],row[2],row[3],row[4],row[5])
            subject_list.append(temp_sub)
            print("|%2d|%-6s|%-25s|%-5s|%2d|"%(ctr,temp_sub.subject_code,temp_sub.subject_name,
                                                temp_sub.branch_code,temp_sub.semester))
            ctr += 1 
        return subject_list
       
    except pymysql.OperationalError as e:
        print(e)
        return []
    
    except Exception as e:
        print(e)
        return []

    finally:
        cur.close()
        con.close()
   
def upload_attendance(faculty):
    try:
        subject_list = faculty_subjects(faculty)
        if len(subject_list)==0:
            print("There are no subjects allocated to you!")
            return
        
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        while 1:
            sub_ctr = input("Please enter the serial# of the subject to upload attendance: ")
            if sub_ctr.isdigit()==False or int(sub_ctr) <= 0 or int(sub_ctr) > len(subject_list):
                print("Wrong Choice!")
            else:
                break
        
        upload_attendance_subject(subject_list[int(sub_ctr)-1])
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
   
def upload_attendance_subject(faculty_subject):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
       
        print(faculty_subject) 
        datetime = input("Please enter datetime of the lecture (YYYY-MM-DD HH:MM:SS): ")
        sql = "INSERT INTO class_attendance_header (faculty_subject_id, \
                class_id, class_startdatetime, class_total_strength) VALUES \
                (%d,%d,'%s',%d)"%(faculty_subject.faculty_subject_id, faculty_subject.branch_subject_id,
                datetime,120)
        print(sql)
        cur.execute(sql)
       
        print("Executed") 

        sql = "SELECT id FROM class_attendance_header \
                WHERE faculty_subject_id=%d and class_id=%d and \
                class_startdatetime='%s'"%(faculty_subject.faculty_subject_id, faculty_subject.branch_subject_id,
                datetime)
        
        print(sql)
        cur.execute(sql)

        for row in cur:
            class_id = row[0]

        print("Please enter below the roll# of the students who attended the class separated by ,:")
        roll_list = input().strip().split(',')
        roll_list = map(int, roll_list)
        
        #Include check to ensure, that attendance should be given to the student belonging to the same class only
        for roll_no in roll_list:
            sql = "INSERT INTO class_attendance_details VALUES (%d,%d)"%(class_id, roll_no)
            cur.execute(sql) 
        con.commit()
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

 
def check_user_as_faculty(id_i):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        
        emp_id = check_user_as_employee(id_i)
        if len(emp_id)!=1:
            print("Not Employee!")
            return []

        sql = "SELECT faculty_id, designation, salary from faculty \
                where employee_id=%d"%(emp_id[0])
        cur.execute(sql)
    
        for row in cur:
           return emp_id+row
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

def check_user_as_employee(id_i):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT employee_id from employee \
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
