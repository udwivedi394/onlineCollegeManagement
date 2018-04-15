import random
from functionality import password_generator as pg
from validations import validationModule as vm
from exceptions import userRegistrationException as ure
from utility import dBconnectivity

def user_registration():
    f_name=input("First Name: ")
    while f_name == "":
        print("Invalid Input (Mandatory Field)")
        f_name=input("First Name: ")
        
    l_name=input("Last Name: ")
    while l_name == "":
        print("Invalid Input (Mandatory Field)")
        l_name=input("Last Name: ")

    e_id=input("Email Id: ")
    while e_id == "":
        print("Invalid Input (Mandatory Field)")
        e_id=input("Email Id: ")
    
    gender=input("Gender (Male/Female): ")
    while gender == "" or gender not in ('Male','Female'):
        print("Invalid Input (Mandatory Field)")
        gender=input("Gender: ")
    
    choice=input("Do you wish to register? (Y/N): ")
    if choice not in('Y','y'):
        return
    
    count = 0
    try:
        vm.validate_email_id(e_id.lower())
    except ure.invalidEmailId as e:
        print(e)
        count += 1 

    except Exception as e:
        print("Error Detected: ", e)

    if count != 0:
        print("User cannot be registered!\n")
        return

    print("Hi",f_name+"... Your Generated User Id and password are:")
    end = False
    while end == False:
        n=random.randrange(100,999)
        user_id=f_name[0:3]+l_name[0:3]+str(n)
        try:
            vm.validate_user_id(user_id)
            end = True
        except ure.invalidUserid as e:
            continue 
    print("User Id:",user_id)
    password=pg.auto_generate_password()
    print("Password:",password)

    choice2=input("Do you wish to change user id and password (Y/N): ")
    if choice2 in ('Y', 'y'):
        end = False
        while end == False:
            new_userid=input("Enter User Id: ")
            try:
                if new_userid == "":
                    print("User_id will remain same.")
                    new_userid = user_id
                    break

                vm.validate_user_id(new_userid)
                print("UserId available.\n")
                end = True

            except ure.invalidUserid as e:
                print(e)

        end = False
        while end == False:
            new_password=input("Enter Password: ")
            try:
                vm.validate_password(new_password)
                confirm_password = input("Confirm Password: ")
                if confirm_password == new_password:
                    print("Password updated.")
                    end = True
                else:
                    raise ure.invalidConfirmPass
            except ure.invalidPassword as e:
                print(e)

            except ure.invalidConfirmPass as e:
                print(e)

        user_id = new_userid
        password = new_password 

    ret = insert_user(user_id, password, f_name, l_name, e_id, gender)
    
    if ret == 1:
        print("User Successfully registered!")
    else:
        print("Some error occurred. Please Try Again!")


def insert_user(user_id, password, f_name, l_name, e_id, gender):
    try:
        con=dBconnectivity.create_connection()
        cur=dBconnectivity.create_cursor(con)

        sql = "INSERT INTO `user_validation` (`user_id`,`password`) VALUES ('%s', '%s')"%(user_id,password)
        cur.execute(sql)
    
        if cur.rowcount == 0:
            return 0
 
        sql = "SELECT id FROM user_validation WHERE user_id='%s'"%(user_id) 
        cur.execute(sql)
        
        if cur.rowcount == 0:
            return 0

        parent_id = None
        for row in cur:
            parent_id = row[0]

        sql = "INSERT INTO user_details (parent_user_id, first_name, last_name, email, gender) VALUES \
                (%d,'%s','%s','%s','%s')"%(parent_id,f_name,l_name,e_id,gender)

        cur.execute(sql)
        con.commit()
        return 1

    except pymysql.OperationalError as e:
        print(e)
        print("Error Detected")
        return -1
    
    except Exception as e:
        print(e)
        return -1

    finally:
        cur.close()
        con.close()
