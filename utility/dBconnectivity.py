#import MySQLdb
import pymysql

def create_connection():
    #return MySQLdb.connect('collegeDB', user='shubhD', password='python')
    return pymysql.connect("localhost","shubhD","python","collegeDB" )

def create_cursor(conn):
    return conn.cursor()
