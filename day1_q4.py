n1= float(input("Enter first number:"))
n2= float(input("Enter second number:"))
n3= float(input("Enter third number:"))

def fun(n1,n2,n3):
    if(n2>n1) :
        if(n2>n3):
            print(f"{n2} is maximum")
        else:
            print(f"{n3} is maximum")
    else:
        if(n1>n3):
            print(f"{n1} is maximum")
        else:
            print(f"{n3} is maximum")
        
fun(n1,n2,n3)