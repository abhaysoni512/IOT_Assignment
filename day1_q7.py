def factorial(k):
    
    i=1
    factorial =1
    while i<=k:
        factorial = factorial*i
        i=i+1
    print(f"{k}={factorial}")

k=0
while k<=10:
    factorial(k)
    k=k+1

