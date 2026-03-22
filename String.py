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
# sentences = "Python is a king of AI:"
# print(sentences[12:17:1])

# If I want to repeat a string. 
# number = "10"
# print(number * 2)
# --------------------- Concatination --------------------
# Note : only same data type can concatinate only.

# fname = "Muhammad"
# lname = "Taha"
# print(fname + " " + lname)

# --------------------- membership Operator------------------------
# in , not in Operator. 

# text = "Python Language"
# print("Python" not in text) # It will find that "Python" in present in text variable or not
                        # It will also return Boolean. 

# Example: 
# email = input("Enter the email").capitalize()
# if "@" in email:
#     print("Correct Email")
# else:
#     print("Invalid email")

#  ----------------------- Method In Python ----------------------
# 1) lower() -> It will covert all text in lower case.
# 2) upper() -> It will covert all text in upper case.
# 3) capitalize() -> It will convert the first letter of sentences with upper case.
# 4) title() -> It will convert all first letter word with upper case.
# 5) swapcase() -> It will reverse and convert with upper and lower case.
#  --------------  Searching and Replacing ------------------
# 6) find() -> It will search for the first letter present in the text.
#              mean ya function mujay us character ka first index batayaga jo main find 
#              kar raha hoo (It return First Index of that particular chahracter)

# text = "python" 
# print(text.find("p"))
# replace() -> This will replace the other text (java) from previous one(Python). 
sent = "Pythonprograming"
print(sent.replace("Python","java"))
print(sent.isalpha())

# startswith()-> This method is check wether a character is starting with or not.
# endswith() -> This method is check wether a character is ending with or not.
# isalpha() -> It will check weather all character is in alphabatic or not.
# isdigit() -> It will check weather all character is in numbers or not.
# isalnum() -> It will check that there is a combination of alphabet & numbers or not.g 