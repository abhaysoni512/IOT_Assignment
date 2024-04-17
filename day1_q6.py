num =int(input("Enter a number whose factorial needs to be calculated:"))
i=1
factorial =1
while i<=num:
    factorial = factorial*i
    i=i+1
    
print(factorial)