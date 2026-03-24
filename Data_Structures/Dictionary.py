## Dictionary in Python!!!!
# It is a data Structure used to store the data in (key:value) -> pair.
# Dictionary are ordered after version 3.7
# Dictionary are also Mutable means (Add, remove etc ) just like list.
# Note : We may store any data type like list, tuple or dictionary in dictionary(nested Dictionary).

#--------------------------- Creating a Dictionary---------------------
my_dict1={
    "name":"Taha", # Note : Key must be unique.
    "Roll_no" : 157,
    "Diciplain": "Electronic"
}
print(my_dict1)

my_dict2={
    "lis1":[1,2,3],
    "lis2":[4,5,6],
    "tup1":(7,8,9),
    "dic":{"grp1":1,"grp2":2,"grp3":3}
}
print(my_dict2) # Only print the "my_dict2" dictionary.
print(type(my_dict2["dic"])) # If i want to access the element of the dictionary.