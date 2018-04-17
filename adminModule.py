from database import validationModule as vm
from utility import dBconnectivity as db
from classes import memberModule as mM
import pymysql

def adminModule():
    try:
        user_name = input('Enter username: ')
        password = input('Enter password: ')
        
        ret = vm.validate_admin(user_name,password)
        if ret<=0:
            print("With big power comes big responsibility.")
            print("Access Denied!")
            return -1
        
        print("Hello Mr. Admin!")
        end = False
        while end==False:
            ch = adminMenu()
            if ch=='1':
                addFaculty()
            elif ch=='2':
                allocateSubjects()
            elif ch=='3':
                viewReport()
            elif ch=='4':
                end = True
            else:
                print("Wrong Choice!")
    except Exception as e:
        print(e)
        return -1
    return 1

def adminMenu():
    print("1. Add Faculty")
    print("2. Allocate Subjects to Faculties")
    print("3. View Reports")
    print("4. Exit")
    ch = input('Enter your choice: ')
    return ch

def addFaculty():
    try:
        con=db.create_connection()
        cur=db.create_cursor(con)
        print("-----------Add Faculty------------")
        print("Note: To add faculty, the person should be registered as user already!")
        print("Also, since you are admin you must be knowing the id(Primary key) of the users to be added.")
        
        u_id = input('Please enter the user_id of user: ')
        user = mM.Person(int(u_id),None)
        user.populate_userdetails()        

        #validate user_id
        print("User Name: ",user.user_details.first_name,user.user_details.last_name)
        designation_dict = {3:'Assistant Professor', 2:'Professor', 4:'Lab Assistant', 1:'HOD'}
        for i in range(1,5):
            print("%d. %s"%(i, designation_dict[i]))
        
        while 1:
            key = input("Enter the sr# of designation: ")
            if key.isdigit() and int(key) in range(1,5):
                break
            print("Wrong choice!")
        
        while 1:
            salary = input('Enter the salary: ')
            if salary.isdigit():
                break
            print("Please enter the numeric value")
        
        sql = "INSERT INTO employee(parent_user_id, emp_category) VALUES (%s,'Faculty')"%(user.id)

        cur.execute(sql)
        sql = "SELECT employee_id FROM employee WHERE parent_user_id=%s"%(user.id)

        cur.execute(sql)
            
        if cur.rowcount == 0:
            raise Exception

        for row in cur:
            employee_id = row[0]

        sql = "INSERT INTO faculty(employee_id,designation,salary) VALUES (%s,'%s',%s)"%(employee_id,
                designation_dict[int(key)],salary)

        cur.execute(sql)
        
        con.commit()
        sql = "SELECT faculty_id FROM faculty WHERE employee_id=%s"%(employee_id)

        cur.execute(sql)
        
        if cur.rowcount==0:
            raise Exception
    
        for row in cur:
            faculty_id = row[0]
    
        print("Generated Employee ID: %s    Faculty ID: %s"%(employee_id,faculty_id))
        return 1

    except Exception as e:
        print("Error Detected", e)
        return -2

    finally:
        cur.close()
        con.close()

def allocateSubjects():
    try:
        con = db.create_connection()
        cur = db.create_cursor(con)

        ch = input("Press v to view the faculty list: ")
        if ch.lower()=='v':
            display_faculty()
        
        ch = input("Press v to view the subject list: ")
        if ch.lower()=='v':
            display_subjects()

        print("Note: To allocate subjects *.csv file should be written in following format")
        print("Faculty ID,Branch Code,Semester,Subject Code\n")
        print("Please enter the absolute/relative path name of the *.csv file: ")
        path = input("Path: ")

        try:
            f1 = open(path,'r')

            subject = f1.readline()
            while subject:
                subject = subject.strip().split(',')
                print("Subject: ",subject)
                for i in range(len(subject)):
                   subject[i] = subject[i].strip()
                
                sql = "SELECT id FROM branch_subjects WHERE branch_code='%s' \
                        and semester=%s and subject_code='%s'"%(subject[1],subject[2],subject[3])
                cur.execute(sql)

                if cur.rowcount==0:
                    print("Id not found!")
                    print("Abort")
                    return
                
                for row in cur:
                    branch_subject_id = row[0]
                    
                sql = "INSERT INTO faculty_subjects (taught_by_faculty_id, subject_code, branch_subject_id) VALUES\
                        ('%s','%s',%s)"%(subject[0],subject[3],branch_subject_id)

                cur.execute(sql)
                subject = f1.readline()

            con.commit()

        except Exception as e:
            print(e)
            return

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


def display_faculty():
    try:
        con = db.create_connection()
        cur = db.create_cursor(con)
        
        sql = "SELECT A.faculty_id, A.employee_id, CONCAT(C.first_name,' ',C.last_name),\
                A.designation FROM faculty A\
                JOIN employee B ON A.employee_id = B.employee_id\
                JOIN user_details C ON C.parent_user_id = B.parent_user_id"

        cur.execute(sql)
        
        if cur.rowcount==0:
            print("No faculties available")
            return

        print("%-5s|%-10s|%-7s|%-30s|%s"%('Sr.#','Faculty ID','Emp.ID.','Name','Designation'))
        
        ctr = 1
        for row in cur:
            print("%-5s|%-10s|%-7s|%-30s|%s"%(ctr,row[0],row[1],row[2],row[3]))
            ctr += 1
        
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

def display_subjects():
    try:
        con = db.create_connection()
        cur = db.create_cursor(con)
        
        sql = "SELECT A.branch_code,A.semester,A.subject_code,B.subject\
                FROM branch_subjects A\
                JOIN subjects B ON B.subject_code = A.subject_code\
                order by A.branch_code , A.semester ASC"

        cur.execute(sql)
        
        if cur.rowcount==0:
            print("Thats weired! No Subject available")
            return

        print("%-5s|%-10s|%-7s|%-8s|%-30s"%('Sr.#','Branch Code','Semester','Sub Code','Subject Name'))
        
        ctr = 1
        for row in cur:
            print("%-5s|%-10s|%-7s|%-8s|%-30s"%(ctr,row[0],row[1],row[2],row[3]))
            ctr += 1
        
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

def viewReport():
    end = False
    while end==False:
        ch = reportMenu()
        if ch=='1':
            display_faculty_subject_distribution()
        elif ch=='4':
            end = True
        else:
            print("Wrong Choice!")
     
 
def reportMenu():
    print("1. View Faculty Subject Allocation")
    print("4. Exit")
    ch = input('Enter your choice: ')
    return ch

def display_faculty_subject_distribution():
    try:
        con = db.create_connection()
        cur = db.create_cursor(con)
        
        sql = "SELECT B.faculty_id,E.employee_id,CONCAT(F.first_name,' ',F.last_name),\
                D.branch_code,D.semester,C.subject_code,C.subject FROM faculty_subjects A\
                JOIN faculty B ON B.faculty_id = A.taught_by_faculty_id\
                JOIN subjects C ON C.subject_code = A.subject_code\
                JOIN branch_subjects D ON D.id = A.branch_subject_id\
                JOIN employee E ON E.employee_id = B.employee_id\
                JOIN user_details F ON F.parent_user_id = E.parent_user_id\
                ORDER BY B.faculty_id, D.branch_code, D.semester"

        cur.execute(sql)
        
        if cur.rowcount==0:
            print("No subject allocation has been done yet")
            return

        print("%-5s|%-10s|%-7s|%-30s|%-11s|%-8s|%-8s|%s"%('Sr.#','Faculty ID','Emp.ID',
                'Name','Branch Code','Semester','Sub Code','Subject Name'))
        
        ctr = 1
        for row in cur:
            print("%-5s|%-10s|%-7s|%-30s|%-11s|%-8s|%-8s|%s"%(ctr,row[0],row[1],
                row[2],row[3],row[4],row[5],row[6]))
            ctr += 1
        
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
    
