# List in Python
# In list we store multiple data in one variable like : 
# my_list = [1.2,3,5,True,"Hello"]
#  
# --------------- Charactertics of List-------------------------
# 1) It is mutable -> Mean we can update or remove the element of list.
# 2) It is Heterogeneous -> We can store different data Types in one list like above.
# ------------------------- Ways of Creating list---------------
# 1) Using List Constructor:
my_list1 = list((1.2,3,5,True,"Hello")) 
print(my_list1)
# 2) List Comprehanssion and using range:
Ran = list(range(1,11)) # we may Also used range function in for loop. 
print(Ran)
# ----------------------- Access and Update ---------------------
my_list = [1.2,3,5,True,"Hello"]
print(my_list[1]," ", my_list[2])
