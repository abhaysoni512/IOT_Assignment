num = int(input("Enter a four digit number :"))
print(f"{int((num/1000)%10)} {int((num/100)%10)} {int((num/10)%10)} {int(num%10)}")

th = (int((num/1000)%10)) *1000
h= (int((num/100)%10)) *100
ten =(int((num/10)%10)) *10
one=(int(num%10)) *1
print(f"{th}+{h}+{ten}+{one}")

th = (int((num/1000)%10)) 
h= (int((num/100)%10))
ten =(int((num/10)%10)) 
one=(int(num%10)) 
print(f"{one}{ten}{h}{th}")
