# brute force approach
# mathematically the total subarrays of an array of size n is n*(n+1)/2
arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
i=0
j=i+1
sum=0
max=float('-inf')
for i in range(len(arr)):
    sum=0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum > max:
            max = sum
print(max)

# optimal approach by usinhg kadane's algorithm

arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum=0
max=float('-inf')

for i in range(0,len(arr)-1):
    sum+=arr[i]
    if sum>max:
        max=sum
    if sum<0:
        sum=0
print(max)