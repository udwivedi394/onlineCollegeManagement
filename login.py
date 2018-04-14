from utility import dBconnectivity as db
from validations import validationModule as vm
from classes import memberModule as memc
import studentModule as sM

def login():
    end = False
    counter = 0
    while end == False:
        user_name=input('Input username: ')
        password=input('Input Password: ')
        attrib=vm.validate_usrname_pswd(user_name,password)
        if len(attrib) and attrib[0]>0:
            #print(attrib)
            counter = 0
            user = memc.Person(attrib[0],attrib[1])
            sM.studentModule(user)
            end = True
            """
            user=Customer()
            vm.set_user_attributes(user,id)
            if ae.A_E()==True:
                enterchoice(user)
                return
            else:
                continue
            """

        elif counter>=2:
            print("You have tried too many times")
            return
        else:
            counter+=1
            print("Try Again")
