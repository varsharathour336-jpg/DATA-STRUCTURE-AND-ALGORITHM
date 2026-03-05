number=153
sum=0
number_copy=number
x=len(str(number))

while number>0:
    remainder=number%10
    sum=sum+remainder**x
    number=number//10

if sum==number_copy:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")