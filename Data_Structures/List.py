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
# Update The List: 
my_list [0] = 2
my_list [3] = "false"
print(my_list)
# ----------- update using Slicing-----------------
List = [1,2,32,5,68]
List[0:3] = 10,20,30
print(List)
# --------------- Concatination in List ---------------
# When we add or join two lists with in the one list. 
lis1=[1,2,3]
lis2=[4,5,6]
new_lis = lis1+lis2
print(new_lis)

# ---------------- Membership Operator in list------------
# user = int(input("Enter the number = "))
# if user in new_lis:
#     print("Its present")
# else:
#     print("Not present")
# ------------- append Method------------------
new_lis.append("Taha")
print(new_lis)
# ------------ extend Method--------------------
a=[1,2,3]
b=[7,8,9]
# a.extend(b)
print(a)
# ------------ Insert Method--------------------
# If we want to add an element in specific location or indexed.
a.insert(3,4)
b.insert(3,10)
# print(a+b)
# ------------ remove Method-------------------
# It's remove the element from the list (only pass the element)
a.remove(2)
print(a)
# ------------ pop Method----------------------
# It will remove with respect to the index number.
remove=a.pop(2) # 2-> is a index nummber.
print(remove)
print(a)
#-------------Clear Method-----------------------
# To remove all the element and get empty list.
a.clear()
print(a)
#-------------Index Method-----------------------
# To find the index of the element. 
indexed=b.index(10)
print(indexed)
#-------------Count Method-----------------------
cnt = [1,2,1,6,8,6,9,7]
print("Its repeat",cnt.count(6),"times")
# Example:
#----------------- Create a List using range Function---------------------
lst = []
for i in range(1,11):
    lst.append(i)
print(lst)    