def rotate_array(array,left,right):
    if left>=right:
        return
    else:
        array[left],array[right]=array[right],array[left]
        rotate_array(array,left+1,right-1)

array=[5,7,3,2,6,1,5,9]

rotated_arr=rotate_array(array,2,4)
print("The rotated array is:", array)


# using iterative approach

class Solution:
    def reverseArray(self, arr):
        left=0
        right=len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left=left+1
            right=right-1
            