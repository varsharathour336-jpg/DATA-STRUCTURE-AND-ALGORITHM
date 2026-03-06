n="abba"
left=0
right=len(n)-1
while left<right:
            if n[left]!=n[right]:
                print("The string is not a palindrome")
                break
            left+=1
            right-=1
else:
    print("The string is a palindrome")