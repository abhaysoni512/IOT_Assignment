'''
The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
'''
s1 = int(input("Enter s1 marks :"))
s2 = int(input("Enter s2 marks :"))
s3 = int(input("Enter s3 marks :"))
avg = (s1+s2+s3)/3

if (avg<60):
    print(f"Grade F")
elif (59<avg<70):
    print(f"Grade D")
elif (69<avg<80):
    print(f"Grade C")
elif (79<avg<90):
    print(f"Grade B")

else:
    print(f"Grade A")

