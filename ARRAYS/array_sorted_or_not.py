arr=[10,20,30,40,50,70,80,90]
i=0


for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
        print("The array is not sorted")
        break
else:
        print("The array is sorted")    