# Functions In Python!!!!!
# Q) what is function and why we used in our code? 
# Ans) It is Block of Code which perform some specific task in our main code or in main function.
# Features of Functions: 
# 1) reusability: of same function in different time.
# 2) Modularity : Jo Code ko samajnay main asani hoti hai.
# 3) Maintenances : Suppose we have 10 functions in our code, so it's easy to find the bug in 
# Function wise coding.

#---------------------- Create A Function without return---------------------
# Example 1: Write a function to print a statement.
# def nam():
#     print("Taha")
# nam() # You need to call the Function, without this statment Function didn't Execute.
# ---------------------Create A Function with return-----------------------
#Example 2: Write a function to print a statement.
# def name():
#     name_1 = "Taha"
#     return name_1
# print(name())
#--------------------Parameter and Argument-------------------------------
# Parameters:  Placeholders for the values.
# Arguments :  They are those which are used in a calling a functions.
# Examples:
def nam(Name): # Name -> Parameter which I used in function.
    print("Hello",Name)

nam("Taha") # It Print Hello Taha -> Argument Which is pass to the function.
nam("Sagar") # It Print Hello Sagar
nam("Raza") # It Print Hello Raza. 
# Note : We are using one function def nam 3 times with different Argument.

#-------------------------Types of Arguments-------------------------
# 1) Positional Argument.
# 2) Keyword Argument.
# 3) Default Argument.

# ------------------------ Positional Argument---------------
# This Argument is pass to the function according to the position of parameters.
# Example:
# def city(name,city):
#     print(f"Welcome {name} to {city}")

# city("Nisar","Karachi") # Nisar is given to the name parameter and Karachi is given to the city parameter.

#-------------------------Keyword Argument--------------------
# If you want to pass the particular Arggument with the given or specific parameter.
# def city(name,city):
#     print(f"Welcome {name} to {city}")

# city(city="Karachi", name="Nisar") 

#-------------------------- Default Argument-------------------
# This Argument is already set with the parameters.
def city(name="Sagar",city="Karachi"):
    print(f"Welcome {name} to {city}")

# city() # If you don't pass any argument it will take the default Argument. 
city("Nisar","Karachi")  # But If you give an argument than it's not used default Argument.

#Example 1: Make a default variable. 
# def clone(a,b=None): # b -> Default Argument
#     b=a
#     b+=1
#     print(f"The output is {b}")

# clone(2)
# clone(4)
# clone(5)

# Example 2: Make a default List.
def clone(a,b=[]): # b -> Default Argument but in list.
    b.append(a)
    print(f"The output is {b}")

clone(2)
clone(4)
clone(5)

# Note : In this example the list is updated because the list is mutable, moreover the in above example 
# Variable , tuple are immutable but dictionaries are mutable.

# Q) What are global and local variable. 
# Ans) Global Variable are those which is assecible through out the program as well as in the function.
# and local variable are those which are only used in function.

#----------------------------------- lambda Function----------------------------
# It is also called Anonymous Function.(Without name functions)
# we don't used def keyword instead we used lambda keyword.
# It have easy syntax to solved the minimal problem.
# Syntax: lambda argument: expression condition

#Example: 
add_Ten = lambda x:x+10
print(f"The ouput is {add_Ten(5)}")