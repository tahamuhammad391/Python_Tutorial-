# Operators
# They are a symbol which are used with operand's  
# Example : 5+4
# Arthematic Operators[+,-,*,/,//,%,**]
num1=5
num2=4
print(num1+num2) #-> Addition of two numbers
print(num1-num2) #-> Subtrction of two numbers
print(num1*num2) #-> Multiplication of two numbers
print(num1/num2) #-> Division of two numbers
print(num1//num2) #-> Float Division of two numbers 
print(num1%num2) #-> Modulas-> remaider
print(num1**num2) #-> Power of number 

# If you have more than one Arthematic operators than use PEMDAS:
# P: Parathesis ()
# E: Exponent **
# MD: Multiply and Division *,/,//,%
# AS: Addition and Subtraction 

# Camparison operator:
# In this operator we will compare two value and it will return Boolean value. 

num1=10
num2=20
print(num1 == num2)
print(num1 != num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 < num2)

# Logical Operators(and , or, not ): We can combine multiple conditions and return boolean value. 
# Example:
is_student=True
age = 20
print("Logical operators")
print(age<18 and is_student)
print(age>25 or is_student)
print(not is_student)

# Assignment Operator: 
'''
= -> used to Assign the value 
+= -> Ex: x=x=1 
-= -> Ex: x=x-1 
*= -> Ex: x=x*1
'''

x=5
#  add 5 in 'X' variable beginner level 
x=x+5
# add 5 in 'X' variable pro level 
x+=5
print(x)

#Identity operators: To compare the memory location of two objects. 
'''
is -> return True if memory location is same.
is not -> return True if memory location is not same.
Note -> It is apply in List/ tuples etc
'''
a=[1,2,3]
b=a
c=[1,2,3]
print("Identity operator")
print(a is b)
print(a is not c)

# Membership Operator: To check weather the value is exist in sequences or not. 
'''
in -> return True when the value is present .
not in -> return True when the value is not present.
This operator is only suitable for List/ tuples and Dictonary.
'''

vegetable = ["Karala", "Aloo", "Tamatar", 123]
print("Membership Operator")
print("Aloo" in vegetable)
print("Pizza" in vegetable)
print(123 in vegetable)
