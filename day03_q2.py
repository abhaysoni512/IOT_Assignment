import dbconn


# def add():
#     connection = dbconn.get_connection()
#     empid = int(input("Enter empid :"))
#     name = input("Enter name : ")
#     department = input("Enter department: ")
#     email = input("Enter email :")
#     salary = int(input("Enter salary : "))
#     dateofjoining =input("Enter Date of joining:")
#     query = f"insert into employee values({empid}, '{name}','{department}','{email}',{salary},'{dateofjoining}');"
#     # create a cursor to execute the query
#     cursor = connection.cursor()
#     #execute query
#     cursor.execute(query)
#     # after execution of query commit your changes
#     connection.commit()
#     # close the cursor
#     cursor.close()
#     #close the connection with mysql server 
#     connection.close()
#     print("Record added successfully!")
# add()

def delete(empid):
   connection = dbconn.get_connection()
   #form query
   query = f"delete from employee where empid =%s;" 
   val = (empid, )
   # create a cursor to execute the query
   cursor = connection.cursor()
   # execute query using cursor
   cursor.execute(query,val)
   #after execution of query commit your changes
   connection.commit()
   # close the cursor
   cursor.close()
   #close the connection with mysql server 
   connection.close()

# delete(3)

def update_employee(email,empid):
    # get connection
    connection = dbconn.get_connection()

    # form a query
    query = f"update employee SET email = %s where empid = %s;"
    val = (email,empid)

    # create a cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    connection.commit()

    # close cursor as well as connection
    cursor.close()
    connection.close()
    print("done")

update_employee("xx@gmail.com",2)



    


    