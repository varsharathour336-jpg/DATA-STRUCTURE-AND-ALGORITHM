arr=[1,0,2,4,3,0,0,3,5,10]
i=0
j=i+1
while j<len(arr):
    if arr[i]==0 and arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
    if arr[i]!=0:
            i=i+1
    j=j+1
print("The array after moving zeroes to end is:", arr)