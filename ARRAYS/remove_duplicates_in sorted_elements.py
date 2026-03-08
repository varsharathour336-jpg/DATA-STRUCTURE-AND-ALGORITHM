# arr=[1,1,1,2,3,4,4,7,9,9,9,10]
# hash_map={}
# li=[]
# for i in range(0,len(arr)):
#     if arr[i] in hash_map:
#         continue
#     else:
#         hash_map[arr[i]]=1
# for j in range(0,len(hash_map)):
#     li.append(list(hash_map.keys())[j])
# print("The array after removing duplicates is:", li)

# for i in range(0,len(li)):
#     arr[i]=li[i]
# print("The array after removing duplicates is:", arr)

# Optimal approach using two pointers

arr=[1,1,1,2,3,4,4,7,9,9,9,10]
i=0
j=i+1

while j<len(arr):
    if arr[i]==arr[j]:
        j=j+1
    else:
        i=i+1
        arr[i]=arr[j]
        j=j+1
print("The array after removing duplicates is:", arr)