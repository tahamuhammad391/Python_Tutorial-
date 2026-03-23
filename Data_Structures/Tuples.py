## Tiples in Python!!!!
# --------------- Chractertics of Tuple---------------------
#  1) immutable -> Can't be change, remove or add etc.
# 2)  Heterogenouse -> Mean we store multiple data typle in same tuples, like list.
# 3)  () -> Tuples are using round brackets.

a = 10,20,30 # It is also a tuple by default.  
# But the good practice is to store these values in round brackets.
b = (1,2,3,7,8,9,5,56,25)
print(type(b))
# Note : In tuple we can't use these method (append,extend,Insert,remove,pop,Clear)
# -------------- Access the Tuples----------------------
print(b[0],b[-1])
# --------------- Access using Slicing------------------
print(b[0:5])
#-------------Index Method-----------------------
# To find the index of the element. 
indexed=b.index(56)
print("Index is = ",indexed)
#-------------Count Method-----------------------
cnt = (1,2,1,6,8,6,9,7,7,9,7)
print(cnt.count(7))
# ------------Lenght Method---------------------
print("Total Element = ",len(cnt))
# H.w = try Max and min Method in list and tuple. 

# --------------- Concatination in List ---------------
# When we add or join two lists with in the one list. 
tup1=(1,2,3)
tup2=(4,5,6)
new_tup = tup1+tup2
print(new_tup) 

# ---------------- Membership Operator in Tuple------------
user = int(input("Enter the number = "))
if user in new_tup:
    print("Its present")
else:
    print("Not present")