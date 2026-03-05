number=5783
count=0

while number>0:
    remainder=number%10
    count=count+1
    number=number//10
print(count)