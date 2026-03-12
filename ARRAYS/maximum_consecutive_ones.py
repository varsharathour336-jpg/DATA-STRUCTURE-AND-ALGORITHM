arr=[1,1,0,1,0,1,1,1,1,0,1,1]

max_consec=0
current_consecutive=0

for i in range(len(arr)):
    if arr[i]==1:
        current_consecutive+=1
    else:
        max_consec=max(max_consec,current_consecutive)
        current_consecutive=0

max_consec=max(max_consec,current_consecutive)

print("The maximum number of consecutive ones is:", max_consec)