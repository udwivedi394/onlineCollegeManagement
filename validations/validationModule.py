'''
Created on Apr 9, 2018
@author: utkarsh.dwivedi01
'''

import re
from exceptions import userRegistrationException as ure
from database import validationModule as vm

def validate_usrname_pswd(user_name,password):
    try:
        id_list = vm.get_user_pwd(user_name, password)
        #print(id_list)
        if len(id_list) == 0:
            return []
        return id_list

    except Exception as e:
        print("Error Detected", e)
        return []
        

def validate_email_id(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
    raise ure.invalidEmailId

def validate_user_id(user_id):
    id_list = vm.get_userid(user_id)
    if len(id_list) != 0:
        raise ure.invalidUserid
    return 1

def validate_password(password):
    temp_list = list(password)
    low_count = up_count = num_count = sym_count = 0
    for i in temp_list:
        if i >= 'a' and i <= 'z':
            low_count += 1
        elif i >= 'A' and i <= 'Z':
            up_count += 1
        elif i >= '0' and i <= '9':
            num_count += 1
        elif i in ['@','#','$','<','%','&']:
            sym_count += 1
    
    if low_count == 0 or up_count == 0 or num_count == 0 or sym_count == 0 or len(temp_list) < 8:
        raise ure.invalidPassword()

    return True
