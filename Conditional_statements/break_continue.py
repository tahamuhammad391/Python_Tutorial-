# Break and Continue statement. 
# Break statement is used when we want to stop the program at certain condition.
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
print("Skip the even number from the list")
for i in range(1,11):
    if i%2==0:
        continue # Skip the step 
    print(i)