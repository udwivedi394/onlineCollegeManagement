'''
Created on Jan 26, 2017
@author: utkarsh.dwivedi01
'''

from utility import dBconnectivity as db
#from exceptions import admin_Module as aM

def get_user_pwd(user_name, password):
    try:
        con=db.create_connection()
        cur=db.create_cursor(con)
        sql = "select id,user_id from user_validation where lower(user_id)='%s' and password='%s'" % (user_name.lower(),password)
        cur.execute(sql)
        for row in cur:
            return row
        return []
    
    except Exception as e:
        print("Error Detected", e)
        return -1
    
    finally:
        cur.close()
        con.close()

def get_userid(user_id):

    try:

        con=db.create_connection()

        cur=db.create_cursor(con)

        cur.execute("select id from user_validation where lower(user_id)= :u_id", {"u_id": user_id.lower()})

        id_list = []

        for row in cur:

            id_list.append(row[0])

        return id_list

    

    except:

        return -1

    finally:

        cur.close()

        con.close()

        

def get_email_mobile_id(value, metaclass):

    try:

        con=db.create_connection()

        cur=db.create_cursor(con)

        cur.execute("select id from user_meta where metaclass=:mid and metavalue=:e_id", {"mid": metaclass,"e_id": value})

        id_list = []

        for row in cur:

            id_list.append(row[0])

        return id_list

    

    except Exception as e:

        print(e)

        return -1

    finally:

        cur.close()

        con.close()

        

def get_city(city):

    try:

        con=db.create_connection()

        cur=db.create_cursor(con)

        sql = "select id from restaurant where lower(city) like ('%s%%')" % (city.lower())

        #print(sql)

        cur.execute(sql)

        id_list = []

        for row in cur:

            id_list.append(row[0])

        return id_list

    

    except Exception as e:

        print(e)

        return -1

    finally:

        cur.close()

        con.close()

        

def validate_admin(user_name, password):

    try:

        con=db.create_connection()

        cur=db.create_cursor(con)

        cur.execute("select id from admin_tab where lower(user_id)=:uname and password=:pwd", {"uname":user_name.lower() , "pwd":password})

        count = 0

        for row in cur:

            count += 1

        if count == 1:

            return row[0]

        raise aM.invalidUserPassword

    

    except aM.invalidUserPassword as e:

        print(e)

        return 0

    

    except Exception as e:

        print("Error Detected", e)

        return -1

    finally:

        cur.close()

        con.close()
