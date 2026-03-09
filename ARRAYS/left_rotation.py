arr= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d=3
rotation=d%len(arr)
# left rotation by d places

arr[:]=arr[rotation:]+arr[:rotation]
print("The left rotated array is:", arr)