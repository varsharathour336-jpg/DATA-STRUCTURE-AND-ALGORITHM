arr=[1, 2, 3, 4, 5]
target=3
for i in range(0,len(arr)):
    if arr[i]==target:
        print("Element found at index",i)
        break
else:
    print("Element not found in the array")

# geek for geek solution
class Solution:
    def search(self, arr, x):
        n=len(arr)
        for i in range(0,n):
            if x==arr[i]:
                return i
                break
        return -1
# time complexity is O(n) and space complexity is O(1)