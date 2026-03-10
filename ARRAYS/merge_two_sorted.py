nums=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]

i=0
j=0
merge_arr=[]

while i < len(nums) and j < len(nums2):

    if nums[i] < nums2[j]:
        if nums[i] not in merge_arr:
            merge_arr.append(nums[i])
        i+=1

    else:
        if nums2[j] not in merge_arr:
            merge_arr.append(nums2[j])
        j+=1

while i < len(nums):
    if nums[i] not in merge_arr:
        merge_arr.append(nums[i])
    i+=1

while j < len(nums2):
    if nums2[j] not in merge_arr:
        merge_arr.append(nums2[j])
    j+=1

print("The merged array is:", merge_arr)