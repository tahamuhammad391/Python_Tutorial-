#Control Statement.
# If , Elif, Else.
# Q) When we need to learn Conditional Statements? 
# Ans) In our program if we want to decide the flow of program or a particular 
# desire output, then we used control statements. 

# Example 1:
# We want to calculate Area of Circle. 
# pie=3.142
# radius = float(input("Enter the Float value of Radius = "))
# Area = pie * radius * radius
# print(int(Area))
# This program will Execute Line by line -> But now Enhanced this code
# By Adding If and Else condition.
# 
# Syntax:
'''
if condition:
    Exacution code which runs under if condition. 

else:
    otherwise runs the code inside else. 
'''
# Example 2:
# i=10
# if i<15:
#     print("I is less than 15")
# print("I am Not in if")

# Example 3:

# user = int(input("Enter a Integer value = "))
# if user >= 15:
#     print("I am greater than 15")
#     print("\nI am in this Block ")
# else:
#     print("I am less than 15")
#     print("I am in else Block")
# print("I will execute after If and eles block....")

# Example 3: Write a code in which age wise vote Eliglibility. 
# person = int(input("Enter a Age of person = ")) 
# if person > 0 and person <=17:
#     print("That you can't vote because you are under 18")
# elif person >=18 and person <=60:
#     print("You can vote")
# elif person >60:
#     print("You also cant't vote because are Above 60")
# else:
#     print("Invalid input")

# Practice Questions 1: write a code for mini calculator (+,-,*,/).
# practice Questions 2: Write a code for discount Calculator (According to phone battery percentage). 

# Example 4: Enhanced the Above code using nested if conditions.
person = int(input("Enter a Age of person = ")) 
if person > 0:
    if person <=17:
        print("That you can't vote because you are under 18")
    elif person >=18 and person <=60:
        print("You can vote")
    elif person >60:
        print("You also cant't vote because are Above 60")
else:
    print("Invalid input")
