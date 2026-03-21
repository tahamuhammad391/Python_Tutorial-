# Loops 
# for loop and while loop
"""
while loop: This loop is execute According to some True conditions until it's false.
while (condition==True):
    Executive code
    Executive code
    until the condition is false.  
""" 
# Example 1:

val = 1
while (val<=10):
    print(f"Number = {val}")
    val +=1

# Practice question 1: Write a code to find even and odd number.
# val = 1
# while (val<=10):
#     if val%2==0:
#         print(f"Even: {val}")
#     else:
#         print(f"Odd:  {val}")
#     val+=1

# Practice Question 2: Write a code to print a table. 
# --------------------------------
# for Loop: This loop is execute or iterate on sequences 
# Suppose you have a list of 5 element than this loop is execute 5 times. 
# Q)   When we use for loop?
# Ans) Where we used list, tuples or dictinaries etc.
 
# Example 1: write a code to print the table. 
# list = [1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     value = 2
#     print(f"{value}*{i} = ",value*i)


## range Function -> usally we used in for loop or as general.
# range (start,stop,step)
# range (1,101,1) -> this will start from 1 to 100 with 1 step of iteretion.
# Example:
# a = list(range(1,11,1))
# print(a)
# Note: every time we don't iterate our for loop with the list so in this case we 
# use range function.
# Example : write a code using range function with for loop.
for i in range(1,11):
    val=2
    print(f"{val}*{i} = ",val*i)