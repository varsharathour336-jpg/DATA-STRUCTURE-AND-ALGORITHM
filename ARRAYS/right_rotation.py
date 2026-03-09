arr=[5,-2,3,9,0,6,10,7]
# right rotation by one place
arr=arr[-1:]+arr[0:7]
# time complexity is o(1)+o(n-1)=>o(n) because if we slice the array for slicing one elemnet it takes o(1) and for slicing the rest of the array it takes o(n-1)
print("The right rotated array is:", arr)


# right rotation another way

arr=[5,-2,3,9,0,6,10,7]
n=len(arr)
temp=arr[n-1]

for i in range(n-2,-1,-1):
    arr[i+1]=arr[i]
arr[0]=temp
print("The right rotated array is:", arr)