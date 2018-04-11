class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def __init__(self, name, address):
        super().__init__(name, address)

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.std_branch = None
        self.std_roll_no = None
        self.std_year = None

class Faculty(Employee):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.salary = None
        self.designation = None

class NonFaculty(Employee):
    def __init__(self, name, address):
        super().__init__(name, address)

class SecurityStaff(NonFaculty):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.age = None
        self.qualification = None

class NormalStaff(NonFaculty):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.work = None
        self.salary = None
        self.department = None
