# String in Python !!!!!!
# In python String have 3 characters 
# 1) immutable -> String is not changable.
# 2) String are indexed -> String is store in index foam.
#                          It have +ve and -ve indexing
# Example 1:
# lan1 = "python"
# lan2 = 'JavaScript'
# print(f"{lan1[0]}\n") # +ve indexing is start from 0.
# print(lan2[-1], lan2[-2], lan2[-3]) # -ve indexing is start from -1.
# 3) iterable: with the help of loop you can access each characters. 

# Example 2: 

# lan1 = "Python"
# for i in lan1:
#     print(i)

# ----------------------------
# Len function used to find lenght.

# inst = "youexcel "  # It may also include the spaces. 
# print(len(inst))

# practice Question 1 : Make a program to take a decision according to the lenght of 
# password which would be enetered by the user.
# 
# ---------------------------Slicing-------------------------
# Q) when this method is usefull? 
# Ans) If we want to extract multiple characters or group of characters than we use slicing?
# string = [start:stop:step]
# start -> It is Included
# stop -> It is Excluded
# step -> The number of step you want to move. 
sentences = "Python is a king of AI:"
print(sentences[12:17:1])

# If I want to repeat a string. 
number = "10"
print(number * 2)
# --------------------- Concatination --------------------
# Note : only same data type can concatinate only.

fname = "Muhammad"
lname = "Taha"
print(fname + " " + lname)
