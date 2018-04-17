'''
Created on Apr 10, 2018
@author: utkarsh.dwivedi01
'''

from utility import dBconnectivity as db
from exceptions import adminModule as aM

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
        cur.execute("select id from user_validation where lower(user_id)='%s'"%(user_id.lower()))
        id_list = []
        for row in cur:
            id_list.append(row[0])

        return id_list
    except Exception as e:
        print(e)
        return []
    finally:
        cur.close()
        con.close()

def validate_admin(user_name, password):
    try:
        con=db.create_connection()
        cur=db.create_cursor(con)
        cur.execute("select id from admin_table where lower(user_id)='%s' and password='%s'"%(user_name,password))
        count = 0
        for row in cur:
            count += 1
        if count == 1:
            return row[0]
        raise aM.invalidUserPassword
    except aM.invalidUserPassword as e:
        print(e)
        return -1

    except Exception as e:
        print("Error Detected", e)
        return -2

    finally:
        cur.close()
        con.close()
