arr=[1,0,5,6,7,8,9,2,3]
missing_number=0
n=len(arr)
total_sum=n*(n+1)//2
sum_of_arr=sum(arr)
missing_number=total_sum-sum_of_arr
print("The missing number is:", missing_number)