#if/else
a=21
b=32
if(a>b):
    print("False")
elif(a<b):
    print("True") 

A=453
B=400
if(A!=B):
    print("True")
elif(A==B):
    print('False')
elif(A>=B):
    print('100% True')

#Even/Odd
A=45
if A/2==0:
    print('Even')
else:
    print('Odd')

#Positive/Negative
B=-76
if B>0:
    print('Positive')
elif B<0:
    print('Negative')

#Age group checker
Age1=10
if Age1<=12:
    print('Child')
elif Age1<=19:
    print('Teenager')
else:
    print('Adult')

Age1=15
if Age1<=12:
    print('Child')
elif Age1<=19:
    print('Teenager')
else:
    print('Adult')

Age1=40
if Age1<=12:
    print('Child')
elif Age1<=19:
    print('Teenager')
else:
    print('Adult')

# Voting Eligibility
age=14
if age>=18:
    print('Eligible')
else:
    print ('Not')

#Password Checker
password=8764
if password is 8764:
    print('Correct')
else:
    print('incorret')

# Simple Calculator
num1 = int(input("first number= "))
num2 = int(input("second number= "))
operation = input("operation (+, -, *, /)= ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else :
    result = num1 / num2

print(result)   

#Grading
number=12
if number>=90:
    print("Grade: A")
elif number>=75:
    print("Grade: B")
elif number>=60:
    print("Grade: C")
elif number<60:
    print("Grade: D")
else:
    print("Fail")



marks = [65, 78, 45, 90, 56]
mark =int(input('Number ='))
marks[-1]=mark 
print(marks)
if mark<50:
    print('Fail')
else:
    print('Pass')
assending=sorted(marks,reverse=False)
print(assending)