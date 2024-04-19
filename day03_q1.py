# * create a table to store employee information
# 	* empid
# 	* name
# 	* department
# 	* email
# 	* salary
# 	* date of joining

# import mysql connector
import mysql.connector

# create a connection with mysql database server
connection =mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# create a query1 
query1 = f"CREATE TABLE employee(empid INT ,name VARCHAR(20),department VARCHAR(20),email VARCHAR(30),salary INT,Date_Of_joining VARCHAR(20))"

# create a cursor to execute the query
cursor = connection.cursor()
# execute query using cursor

# cursor.execute(query1)
cursor.execute(query1)
# after execution of query commit your changes
connection.commit()
# close the cursor
cursor.close()
#close the connection with mysql server 
connection.close()