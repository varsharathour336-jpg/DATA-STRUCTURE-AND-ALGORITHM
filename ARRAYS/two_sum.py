arr=[5,9,1,2,4,15,6,3]
target=13
hash_map={}
for i in range(0,len(arr)):
    hash_map[arr[i]]=i
    if target-arr[i] in hash_map:
        print("The indices of the two numbers that add up to the target are:", hash_map[target-arr[i]], i)