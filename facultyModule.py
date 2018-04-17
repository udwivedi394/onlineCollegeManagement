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
            upload_marks(faculty)
        elif choice=='4':
            view_faculty_profile(faculty)
        else:
            print("Wrong choice!")
    return

def facultyMenu(faculty):
    print("Hi! %s"%(faculty.user_details.first_name))
    print("1. View your subjects")
    print("2. Upload attendance")
    print("3. Upload Marks")
    print("4. View Profile")
    print("5. Go back to previous menu")
    ch = input("Please enter your choice: ")
    return ch

def view_faculty_profile(faculty):
    print("\n\n")
    print("Name          : %-30s %-10s : %s"%(faculty.user_details.first_name+' '+faculty.user_details.last_name,
                                        'User ID',faculty.user_id))
    print("Email         : %-30s %-10s : %s"%(faculty.user_details.email,'Gender',faculty.user_details.gender))
    print("Employee ID   : %-30s %-10s : %s"%(faculty.employee_id,'Faculty ID', faculty.faculty_id))
    print("Designation   : %-30s %-10s : %d"%(faculty.designation,'Salary',faculty.salary))
    print("\n\n")
    return 

def faculty_subjects(faculty,display_marks=False):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT A.id,C.id,B.Subject_code,B.Subject,C.branch_code,C.semester,\
                B.internal_marks,B.external_marks,B.Credits \
                FROM faculty_subjects A \
                JOIN subjects B on B.Subject_code = A.subject_code \
                JOIN branch_subjects C on C.id = A.branch_subject_id \
                WHERE A.taught_by_faculty_id = '%s'"%(faculty.faculty_id)
        cur.execute(sql)
        
        if cur.rowcount == 0:
            return []

        subject_list = []

        if display_marks:
            print("%4s|%-11s|%-45s|%-6s|%-8s|%13s|%13s|%s"%('Sr.#','SubjectCode','Subject Name',\
                    'Branch','Semester','Max.Int.Marks','Max.Ext.Marks','Credits'))
        else:
            print("%4s|%-11s|%-45s|%-6s|%-8s"%('Sr.#','SubjectCode','Subject Name',\
                    'Branch','Semester')) 

        ctr=1
        for row in cur:
            temp_sub = oM.FacultySubject(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            subject_list.append(temp_sub)
            if display_marks:
                print("%4s|%-11s|%-45s|%-6s|%-8s|%13s|%13s|%s"%(ctr,temp_sub.subject_code,temp_sub.subject_name,\
                    temp_sub.branch_code,temp_sub.semester,temp_sub.internal_marks,temp_sub.external_marks,temp_sub.credits))
            else:
                print("%4d|%-11s|%-45s|%-6s|%-8d"%(ctr,temp_sub.subject_code,temp_sub.subject_name,\
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
            print("Note: Enter %d to exit"%(len(subject_list)+1))
            sub_ctr = input("Please enter the serial# of the subject to upload attendance: ")
            if sub_ctr.isdigit()==False or int(sub_ctr) <= 0 or int(sub_ctr) > len(subject_list)+1:
                print("Wrong Choice!")
            elif int(sub_ctr)==len(subject_list)+1:
                return
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
  
def display_enrolled_students(faculty_subject):
    try: 
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT A.std_roll_no, CONCAT(D.first_name,' ',D.last_name) as Name FROM students A\
                JOIN user_details D ON D.parent_user_id = A.parent_user_id\
                JOIN branch_subjects B ON B.branch_code = A.std_branch and B.semester=A.std_semester\
                JOIN faculty_subjects C ON C.branch_subject_id = B.id\
                WHERE C.id=%d"%(faculty_subject.faculty_subject_id)

        cur.execute(sql)
        if cur.rowcount==0:
            print("No students enrolled for this subject")
            return -5

        print("\nPlease find below the list of students enrolled for this subject:")
        print("%-11s|%s"%('Roll.No.','Name'))
        for row in cur:
            print("%-11s|%s"%(row[0],row[1]))
       
        print('\n') 
        return 1            
        
    
    except pymysql.OperationalError as e:
        print(e)
        return -1
    
    except Exception as e:
        print(e)
        return -1

    finally:
        cur.close()
        con.close()   


 
def upload_attendance_subject(faculty_subject):
    try:
        ret=display_enrolled_students(faculty_subject)
        if ret < 1:
            return
        
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
       

        datetime = input("Please enter datetime of the lecture (YYYY-MM-DD HH:MM:SS): ")
        sql = "INSERT INTO class_attendance_header (faculty_subject_id, \
                class_id, class_startdatetime, class_total_strength) VALUES \
                (%d,%d,'%s',%d)"%(faculty_subject.faculty_subject_id, faculty_subject.branch_subject_id,
                datetime,120)
        #print(sql)
        cur.execute(sql)
       
        #print("Executed") 

        sql = "SELECT id FROM class_attendance_header \
                WHERE faculty_subject_id=%d and class_id=%d and \
                class_startdatetime='%s'"%(faculty_subject.faculty_subject_id, faculty_subject.branch_subject_id,
                datetime)
        
        #print(sql)
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

def upload_marks(faculty):
    try:
        subject_list = faculty_subjects(faculty,True)
        if len(subject_list)==0:
            print("There are no subjects allocated to you!")
            return
        
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        while 1:
            print("Note: Enter %d to exit"%(len(subject_list)+1))
            sub_ctr = input("Please enter the serial# of the subject to upload marks: ")
            if sub_ctr.isdigit()==False or int(sub_ctr) <= 0 or int(sub_ctr) > len(subject_list)+1:
                print("Wrong Choice!")
            elif int(sub_ctr)==len(subject_list)+1:
                return
            else:
                break
        
        upload_marks_subject(subject_list[int(sub_ctr)-1])
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


def upload_marks_subject(faculty_subject):
    try: 
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        
        ret=display_enrolled_students(faculty_subject)
        if ret < 1:
            return
        
        year = 2018 
        print("Note: To upload marks *.csv file should be written in following format")
        print("Student_Roll_No,Internal_Marks,External_Marks,Credit\n")
        print("Please enter the absolute/relative path name of the *.csv file: ")
        path = input("Path: ")
        
        try:
            f1 = open(path,'r')
            
            student_list = []
            marks = f1.readline()
            while marks:
                marks = marks.strip().split(',') 
                
                for i in range(len(marks)):
                   marks[i] = marks[i].strip()
            
                student_list.append(marks[0])
                sql = "INSERT INTO stu_subject_marks (subject_code, semester, year,\
                    student_roll_no, max_internal_marks, internal_marks, max_external_marks,\
                    external_marks, max_credits, credits) VALUES ('%s',%d,%d,%s,%d,%s,%d,%s,%f,%s)"%(faculty_subject.subject_code,
                    faculty_subject.semester,year,marks[0],faculty_subject.internal_marks,marks[1],faculty_subject.external_marks,
                    marks[2],faculty_subject.credits,marks[3])

                cur.execute(sql)
                marks = f1.readline()
            
            con.commit()
            
            for std_roll_no in student_list:
                update_semester_status(std_roll_no,faculty_subject.semester)
            
            
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

def update_semester_status(student_roll_no, semester): 
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
       
        sql = "SELECT D.subject_code,D.internal_marks, \
                D.external_marks, D.credits FROM students A \
                JOIN branch B on A.std_branch = B.branch_code \
                JOIN branch_subjects C on A.std_branch = C.branch_code \
                JOIN subjects D on C.subject_code = D.subject_code \
                where std_roll_no=%s and C.semester=%d"%(student_roll_no,semester) 
       
        cur.execute(sql)
        tot_internal_marks, tot_external_marks, tot_credits = 0, 0, 0.0
        subject_list = []

        for row in cur:
            tot_internal_marks += int(0 if row[1]==None else row[1])
            tot_external_marks += int(0 if row[2]==None else row[2])
            tot_credits += float(0.0 if row[3]==None else row[3])
            subject_list.append(row[0])
        
        tot_max_marks = tot_internal_marks+tot_external_marks
        if tot_max_marks == 0:
            return

        sql = "SELECT subject_code, internal_marks, external_marks, \
                credits FROM stu_subject_marks \
                WHERE student_roll_no=%s and semester=%d"%(student_roll_no, semester)
        cur.execute(sql)

        internal_marks, external_marks, credits = 0, 0, 0.0
        for row in cur:
            if row[0] in subject_list:
                subject_list.remove(row[0])
            internal_marks += int(row[1])
            external_marks += int(row[2])
            credits += float(row[3])
 
        if len(subject_list)!=0:
            return
    
        tot_marks_obtained = internal_marks+external_marks
        percentage = (tot_marks_obtained/tot_max_marks)*100
        
        if percentage <= 34.0:
            status = "FAIL"
        else:
            status = "PASS"
        
        #ll = [semester,tot_max_marks,semester,tot_marks_obtained,semester,status,student_roll_no]
 
        sql = "UPDATE stu_semwise_status SET\
                sem_%d_max_marks=%d, sem_%d_marks=%d, sem_%d_status='%s'\
                WHERE std_roll_no=%s"%(semester,tot_max_marks,semester,tot_marks_obtained,semester,status,student_roll_no)

        cur.execute(sql)
        
        if status == "PASS" and semester!=8:
            sql = "UPDATE students SET std_semester=std_semester+1\
                    WHERE std_roll_no=%s"%(student_roll_no)
            cur.execute(sql)
        
        con.commit()
         
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
