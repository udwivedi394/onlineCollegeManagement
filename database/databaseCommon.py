#import MySQLdb
import pymysql
from utility import dBconnectivity

def run_query(sql):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        cur.execute(sql)
        con.commit()
        return 1
    
    except pymysql.OperationalError as e:
        print(e)
        return -1
        

    except Exception as e:
        print(e)
        return -1

    finally:
        print(cur)
        cur.close()
        con.close()


def fetch_user_details(id_i):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        sql = "SELECT first_name, last_name, email, gender from user_details \
                where parent_user_id=%d"%(id_i)
        cur.execute(sql)
        for row in cur:
           return row
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
    
