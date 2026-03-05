# brute force approach

# n=15
# factors=[]

# for i in  range(1,n+1):
#     if n%i==0:
#         factors.append(i)
# print(factors)
import math
N=36
factor=[]
for i in range(1,int(math.sqrt(N))+1):
    if N%i==0:
        factor.append(i)
        if N//i != i:
            factor.append(N//i)

factor.sort()
print(*factor)