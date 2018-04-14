from utility import dBconnectivity as db
from validations import validationModule as vm
from classes import memberModule as memc
import studentModule as sM
import facultyModule as fM

def login():
    end = False
    counter = 0
    while end == False:
        user_name=input('Input username: ')
        password=input('Input Password: ')
        attrib=vm.validate_usrname_pswd(user_name,password)
        if len(attrib) and attrib[0]>0:
            counter = 0
            user = memc.Person(attrib[0],attrib[1])
            while 1:
                print("Choose Module:")
                print("1. Student Module")
                print("2. Faculty Module")
                print("3. Signout")
                ch = input("Enter your choice: ")
                if ch == '1':
                    sM.studentModule(user)
                elif ch == '2':
                    fM.facultyModule(user)
                elif ch == '3':
                    end = True
                    break
                else:
                    print("Wrong Choice!")

        elif counter>=2:
            print("You have tried too many times")
            return
        else:
            counter+=1
            print("Try Again")

if __name__=='__main__': 
    while 1:
        print("1. Login")
        ch=input("Any other key to exit: ")
        if ch=='1':
            login()
        else:
            break
