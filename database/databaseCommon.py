#import MySQLdb
import pymysql
from utility import dBconnectivity

def run_query(sql):
    try:
        con = dBconnectivity.create_connection()
        cur = dBconnectivity.create_cursor(con)
        print(cur)
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
