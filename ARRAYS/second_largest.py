arr=[-1,-3,-9,-8,-2,-5,-6]

first_max=arr[0]
second_max=float('-inf')
for i in range(1,len(arr)):
    if arr[i]>first_max:
        second_max=first_max
        first_max=arr[i]
    elif arr[i]>second_max and arr[i]!=first_max:
        second_max=arr[i]
print("The second largest element in the array is:", second_max)


# leetcode solution
# class Solution:
#     def getSecondLargest(self, arr):
#         first_max=arr[0]
#         second_max=float('-inf')
#         for i in range(1,len(arr)):
#             if arr[i]>first_max:
#                 second_max=first_max
#                 first_max=arr[i]
#             elif arr[i]>second_max and arr[i]!=first_max:
#                 second_max=arr[i]
#         if second_max==float('-inf'):
#             return -1
#         return second_max