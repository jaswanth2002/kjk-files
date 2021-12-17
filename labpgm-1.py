#Step -1 : Download mysql server.
#Step -2: Make sure its up and running.
#Step -3: Write the code
#pip3 install mysql-connector
# mysql -u root
# show databases;
# CREATE DATABASE rupam;
# use rupam;
# show tables;
# CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255));
# describe customers;
# INSERT INTO customers (name, address) VALUES('Reva2', 'Bangalore2');
# SELECT * FROM customers;
# INSERT INTO customers (name, address) VALUES('IIT', 'Patna');
#mysql query#http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm

import mysql.connector
from mysql.connector import Error
try:
 connection = mysql.connector.connect(host='localhost', database='rupam', user='root', password='')
 if connection.is_connected():
     db_Info = connection.get_server_info()
     print("Connected to MySQL database... MySQL Server version: ",db_Info)
     cursor = connection.cursor()
     selected = input("Enter the type of operation which you want to perform i.e insert/select: ")
     if selected == 'insert':
         q = input('Type your insert sql query : ');
         cursor.execute(q)
         connection.commit()
         print("insert query executed succesfully")
     elif selected == 'select':
        q = input('Type your select sql query : ');
        cursor.execute(q)
        # record = cursor.reva91    123()
        # print ("Expected Result - ", record)
        # record = cursor.fetchone()
        # print(record)
        allrecords = cursor.fetchall()
        for x in allrecords:
            print(x)
     else:
        print('Terminating, Please Enter insert or select to proceed')
     #closing the connection here instead of finally
     # if(connection.is_connected()):
     #     print("MySQL is still Connected")
     #     cursor.close()
     #     connection.close()
     #     print("MySQL connection is closed")
except Error as e:
    print ("Error while connecting to MySQL", e)
finally:
    print("inside finally")
    if(connection.is_connected()):
        print("MySQL is still Connected")
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
