from database import databaseCommon

class Person:
    def __init__(self, id_i, user_id):
        self.id = id_i
        self.user_id = user_id
        self.user_details = None

    def populate_userdetails(self):
        self.user_details = Details(self)
        self.user_details.populate_attributes()

    def __str__(self):
        return "%d|%s|%s|%s"%(self.id,self.user_id,self.user_details.first_name,self.user_details.gender)

class Details:
    def __init__(self, obj):
        self.parent_obj = obj
        self.first_name = None
        self.last_name = None
        self.email = None
        self.gender = None

    def populate_attributes(self):
        attrib_list = databaseCommon.fetch_user_details(self.parent_obj.id)
        self.first_name, self.last_name, self.email, self.gender = attrib_list[0],attrib_list[1],attrib_list[2],attrib_list[3]

    def __str__(self):
        return "%s|%s|%s|%s"%(self.first_name,self.last_name,self.email,self.gender)

class Employee(Person):
    def __init__(self, id_i, user_id, emp_id):
        super().__init__(id_i, user_id)
        super().populate_userdetails()
        self.employee_id = emp_id

class Student(Person):
    def __init__(self, id_i, user_id, std_roll_no, std_year, std_sem, std_branch, branch_name):
        super().__init__(id_i, user_id)
        super().populate_userdetails()
        self.std_roll_no = std_roll_no
        self.std_admission_year = std_year
        self.semester = std_sem
        self.std_branch = std_branch
        self.branch_name = branch_name 
    
    def __str__(self):
        return "%d|%s|%s|%d|%d|%d|%s"%(self.id, self.user_id, self.user_details, self.std_roll_no,
                self.std_admission_year, self.semester, self.std_branch)

class Faculty(Employee):
    def __init__(self, id_i, user_id, emp_id, faculty_id, designation, salary):
        super().__init__(id_i, user_id, emp_id)
        self.faculty_id = faculty_id
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return "%d|%s|%s|%d|%s|%s|%d"%(self.id, self.user_id, self.user_details, self.employee_id,
                self.faculty_id, self.designation, self.salary)

"""
class NonFaculty(Employee):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.payroll = None
"""

class SecurityStaff(Employee):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.age = None
        self.qualification = None

class NormalStaff(Employee):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.work = None
        self.salary = None
        self.department = None
