# by using slicing

arr=[1,2,3,4,5]
k=2
length=len(arr)
rotation=k%length
# right rotation by k places
arr[:]=arr[length-rotation:]+arr[:length-rotation]
# time complexity of this is (k)+o(n-k)=>o(n) because if we slice the array for slicing k elemnet it takes o(k) and for slicing the rest of the array it takes o(n-k)
print("The right rotated array is:", arr)



# optimal solution by using reversal algorithm

def reverse_array(array,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
arr=[1,2,3,4,5,6]
k=3
n=len(arr)
rotation=k%n
reverse_array(arr,n-rotation,n-1)
reverse_array(arr,0,n-rotation-1)
reverse_array(arr,0,n-1)