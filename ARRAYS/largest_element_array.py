arr=[-1,-3,-9,-8,-2,-5,-6]

largest=arr[0]
for i in range(1,len(arr)):
    if largest<=arr[i]:
        largest=arr[i]
print("The largest element in the array is:", largest)