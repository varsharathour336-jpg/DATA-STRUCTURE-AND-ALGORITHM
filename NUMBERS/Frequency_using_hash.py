hashmap = {}
n = [5,6,7,5,6,8,9,5]
length = len(n)

for i in range(length):
    if n[i] in hashmap:
        hashmap[n[i]] = hashmap.get(n[i],0) + 1
    else:
        hashmap[n[i]] = 1

print(hashmap)