## Dictionary in Python!!!!
# It is a data Structure used to store the data in (key:value) -> pair.
# Dictionary are ordered after version 3.7
# Dictionary are also Mutable means (Add, remove etc ) just like list.
# Note : We may store any data type like list, tuple or dictionary in dictionary(nested Dictionary).

#--------------------------- Creating a Dictionary---------------------
# my_dict1={
#     "name":"Taha", # Note : Key must be unique.
#     "Roll_no" : 157,
#     "Diciplain": "Electronic"
# }
# print(my_dict1)
# --------------------------- Creating a Dictionary using Constructors---------------------
# empty_Dic=dict(Name="Taha",emp=3456)
# print(empty_Dic)
#--------------------Create a dictionary from two lists using zip()-----------------
# Zip() -> The built-in zip() function pairs up elements from the two lists.
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dynamic_dict = dict(zip(keys, values))
# print(dynamic_dict) # Output: {'a': 1, 'b': 2, 'c': 3}

#---------------------------Access a Dictionary------------------------
# my_dict2={
#     "lis1":[1,2,3],
#     "lis2":[4,5,6],
#     "tup1":(7,8,9),
#     "dic":{"grp1":1,"grp2":2,"grp3":3}
# }
# print(my_dict2) # Only print the "my_dict2" dictionary.
# print(type(my_dict2["dic"])) # If i want to access the element of the dictionary.
# -----------------------Adding the element in Dictionary-----------------
# my_dict3={
#     "fruit":["Banana","Orange","Apple"],
#     "Vege" :["Tomato","Potato","lady_Finger"]
# }
# print(my_dict3)
# my_dict3["price"]=43.76 # Add new element like price= 43.76
# my_dict3["fruit"].append("Anar") # If you want to update the "fruit" list. 
# my_dict3["Vege"].remove("Tomato")
# print(my_dict3)

#---------------------Deleting the Element-------------------
# my_dict4={
#     "employ":"Taha",
#     "Salary":120000,
#     "Emp_number":364
# }
# print(my_dict4)
# del my_dict4["Emp_number"]
# print(my_dict4)
#---------------------Methods in Dictionary------------------
#---------------------Get Method-----------------------------
# We used get method to retrive the value of specific key. 
# my_dict5={
#     "employ":"Arsalan",
#     "Salary":140000,
#     "Emp_number":340
# }
# print(my_dict5.get("salary","Not Found"))
# print(my_dict5.get("Salary","Not Found"))
#------------------------Keys and Value Method------------------------
# print(my_dict5.keys())
# print(my_dict5.values())
#---------------------- Items Method---------------------
# my_dict6 = {"name": "Taha","Salary":55000,"designation":"Engineer"}
# all_items = my_dict6.items()
# print(all_items)
#--------------------- pop Method--------------------
# my_dict6 = {"name": "Taha","Salary":55000,"designation":"Engineer","Emp": 3456}
# popped = my_dict6.pop("Emp","Not Found")# Note: you must give the Argument as "Key" and If 
# # a key is not present in the dictionaryy than its print the not found message.
# print(popped)
# print(my_dict6)
#---------------------- pop item Method-----------------------
# my_dict6 = {"name": "Taha","Salary":55000,"designation":"Engineer","Emp": 3456}
# popped = my_dict6.popitem() # It Will delect the last item in the dictionary.
# print(popped)
# --------------------- Clear Method------------------------
# my_dict6 = {"name": "Taha","Salary":55000,"designation":"Engineer","Emp": 3456}
# my_dict6.clear() # It Will delect the All item in the dictionary.
# print(my_dict6)
#------------------- Nested Dictionary!!!!----------------------
# Nested Dictionaries is define as the main dictionary have it's inside dictionary.
# main_user={}
# limit = int(input("Enter a number of users you want to Add!!!"))
# for i in range(limit):
#     key="User"+str(i+1)
#     name1=input(f"Enter a name for {key}: ")
#     city1=input(f"Enter a city for {key}: ")
#     age1=input(f"Enter a age for {key}: ")
#     trans=[]
#     no= int(input("Enetr the number of transaction= "))
#     for i in range(no):
#       transaction=int(input("Enter the amount="))
#       trans.append(transaction)
#     value=dict(name=name1,city=city1,age=age1,Tran=trans)
#     main_user[key]=value
# ------------------------Dictionary Comprehenshion-------------
# First Method:
print("Frist Method")
Emp_dic={}
for i in range(1,6):
    square=i**2
    Emp_dic[i]=square

print(Emp_dic)

# Second Method:
print("Second Method")
Emp_dic2={i: i**2 for i in range(1,6)}
print(Emp_dic2)