# Newted loop : it is work in a fashion of rows and colums.
"""
Outer loop run once and than inner loop completly
Again
outer loop run second time and than inner loop completly.
and this will moving so on untill outer loop condition false or range would be complete.
"""

# Example 1:
# for i in range(1,3):
#     for j in range(1,7):
#         print(f"{i} and {j}")

#Example 2:
i=1
while (i<=3):
    j=1
    while (j<=5):
        print(f"{i}-{j}")
        j+=1
    i+=1

