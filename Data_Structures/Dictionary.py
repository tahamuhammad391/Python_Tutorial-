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
# #---------------------------Access a Dictionary------------------------
# my_dict2={
#     "lis1":[1,2,3],
#     "lis2":[4,5,6],
#     "tup1":(7,8,9),
#     "dic":{"grp1":1,"grp2":2,"grp3":3}
# }
# print(my_dict2) # Only print the "my_dict2" dictionary.
# print(type(my_dict2["dic"])) # If i want to access the element of the dictionary.
# -----------------------Adding the element in Dictionary-----------------
my_dict3={
    "fruit":["Banana","Orange","Apple"],
    "Vege" :["Tomato","Potato","lady_Finger"]
}
# print(my_dict3)
my_dict3["price"]=43.76 # Add new element like price= 43.76
my_dict3["fruit"].append("Anar") # If you want to update the "fruit" list. 
my_dict3["Vege"].remove("Tomato")
print(my_dict3)

#---------------------Deleting the Element-------------------
my_dict4={
    "employ":"Taha",
    "Salary":120000,
    "Emp_number":364
}
print(my_dict4)
del my_dict4["Emp_number"]
print(my_dict4)