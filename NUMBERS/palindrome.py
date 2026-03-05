# number=121
# new_str=str(number)
# reverse_str=new_str[::-1]

# if number==int(reverse_str):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


number=5885
number_copy=number
new_number=0
remainder=0

while number>0:
    remainder=number%10
    new_number=new_number*10+remainder
    number=number//10

if number_copy==new_number:
    print("Palindrome")
else:
    print("Not a Palindrome")
