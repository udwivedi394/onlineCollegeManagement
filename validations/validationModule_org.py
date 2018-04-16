'''
Created on Apr 9, 2018
@author: utkarsh.dwivedi01
'''

from utility import DBConnectivity
from classes.restrauntModule import Restaurant
import datetime
from exceptions import user_registration_exception as ure
from database import validation_module as vm
from database import restaurant_search as rs
from exceptions import place_order_exception as poe

def validate_usrname_pswd(user_name,password):

    try:

        id_list = vm.get_user_pwd(user_name, password)

        #print(id_list)

        if len(id_list) != 1:

            return -1

        return id_list[0]

    except Exception as e:

        print("Error Detected", e)

        return -1



def set_user_attributes(user,id):

    try:

        user.set_customer_id(id)

        con=DBConnectivity.create_connection()

        cur=DBConnectivity.create_cursor(con)

        cur.execute("select metavalue from user_meta where user_id=:i1 and metaclass=:i2", {"i1":id ,"i2":"f_name"})

        for row in cur:

            user.set_f_name(row[0])

        

        cur.execute("select metavalue from user_meta where user_id=:i1 and metaclass=:i2", {"i1":id ,"i2":"pin_code"})

        for row in cur:

            user.set_pincode(row[0])

            

        cur.execute("select metavalue from user_meta where user_id=:i1 and metaclass=:i2", {"i1":id ,"i2":"city"})

        for row in cur:

            user.set_city(row[0])

            

        cur.execute("select metavalue from user_meta where user_id=:i1 and metaclass=:i2", {"i1":id ,"i2":"area"})

        for row in cur:

            user.set_area(row[0])

        

        cur.execute("select metavalue from user_meta where user_id=:i1 and metaclass=:i2", {"i1":id ,"i2":"state"})

        for row in cur:

            user.set_state(row[0])

        

        #print(user)

        return 0

    except:

        return -1

    finally:

        cur.close()

        con.close()





def validate_city(city):

    id_list = vm.get_city(city)

    if len(id_list) == 0:

        raise ure.cityInvalid

    return 1

        



def validate_pincode(pincode):

    try:

        con=DBConnectivity.create_connection()

        cur=DBConnectivity.create_cursor(con)

        cur.execute("select id from restaurant where pincode like ("+pincode[:4]+"%)")

        count = 0

        for row in cur:

            count += 1

        if count >= 1:

            return 1

        return 0

    except:

        return -1

    finally:

        cur.close()

        con.close()

        

def validate_rest_area(ip_value):

    area_count = 0

    rest_list = []

    row_list = rs.searchRestaurant(ip_value, 'area')

    

    if len(row_list) != 0:

        for row in row_list:

            temp_rest = Restaurant()

            set_restaurant_attributes(temp_rest, row[0])

            rest_list.append(temp_rest)

            area_count += 1

    

    if area_count != 0:

        return rest_list

    

    row_list = rs.searchRestaurant(ip_value, 'name')

    name_count = 0

    

    if len(row_list) != 0:

        for row in row_list:

            temp_rest = Restaurant()

            set_restaurant_attributes(temp_rest, row[0])

            rest_list.append(temp_rest)

            name_count += 1

    

    if name_count != 0:

        return rest_list

    

    if name_count == 0 and area_count == 0:

        raise poe.noRestaurantFound

    



def set_restaurant_attributes(temp_rest, id):

    try:

        con=DBConnectivity.create_connection()

        cur=DBConnectivity.create_cursor(con)

        cur.execute("select id, name, area, pincode, contactno from restaurant where id=:id", {"id": id})

        for id, name, area, pincode, contactno in cur:

            temp_rest.set_contact_no(contactno)

            temp_rest.set_restaurant_id(id)

            temp_rest.set_pincode(pincode)

            temp_rest.set_r_name(name)

            temp_rest.set_area(area)

        return 1

    

    except:

        return -1

        

    finally:

        cur.close()

        con.close()

        

def validate_email_id(email_id):

    id_list = vm.get_email_mobile_id(email_id, "email_id")

    if len(id_list) != 0:

        raise ure.invalidEmailId

    return 1

        

def validate_mob_no(mobile_no):

    id_list = vm.get_email_mobile_id(mobile_no, "mobile_no")

    if len(id_list) != 0:

        raise ure.invalidMobileno

    return 1





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





def validate_start_end_date(start_date, end_date):

    try:

        start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")

        end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")

    

        if start_date > end_date:

            print("Error! Start date greater than end date!")

            return -1

        return 1

    

    except ValueError:

        print("Invalid Date Format")

        return -2

    

    except Exception as e:

        print(e)

        return -3
