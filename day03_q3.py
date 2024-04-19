#* Write a python program to print all employees, employees of given department, employee with highest and lowest salary
import dbconn
connection = dbconn.get_connection()
def print_all():
    

    # form a query
    query = "select name from employee;"

    # create a cursor to execute query
    cursor = connection.cursor()   #agent h humara

    # execute query using cursor
    cursor.execute(query)          #isi agent n humhra execute kiya

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples
    for rec in records:
        print(rec)

    # close the cursor
    cursor.close()

    # close the connection
    #connection.close()
print_all()

print("-----------------------/n")
#employees of given department
def employe_dep(department):
    
    # form a query
       
    query = f"select name from employee where department = %s;"
    value = (department,)

    # create a cursor to execute query
    cursor = connection.cursor()   #agent h humara
    
    # execute query using cursor
    cursor.execute(query,value)          #isi agent n humhra execute kiya

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples
    for rec in records:
        print(rec)

    # close the cursor
    cursor.close()

    # close the connection
    #connection.close()
employe_dep('production')
print("-----------------------/n")
def employe_salaryh_salaryl():
    
    # form a query1 
    query1 = "select name from employee order by salary ASC LIMIT 1;"
   
    # create a cursor to execute query
    cursor = connection.cursor()   #agent h humara

    # execute query using cursor
    cursor.execute(query1)          #isi agent n humhra execute kiya

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples
  
    print(records)

    # close the cursor
    cursor.close()
    #form query 2
    query2 = "select name from employee order by salary DESC LIMIT 1;"
     # create a cursor to execute query
    cursor = connection.cursor()   #agent h humara

    # execute query using cursor
    cursor.execute(query2)          #isi agent n humhra execute kiya

    # get data from cursor
    records2 = cursor.fetchall()     #   returns list of tuples
  
    print(records2)

    # close the cursor
    cursor.close()

   
employe_salaryh_salaryl()

# close the connection
connection.close()



