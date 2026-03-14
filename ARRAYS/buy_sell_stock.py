# my approach
arr=[7,1,5,3,6,4]
if arr == sorted(arr, reverse=True):
    print("you cannot sell the stock as you have bought it on the last day")
else:
    buy=min(arr)
    for i in range(buy+1,len(arr)-1):
        sell=max(arr[i:])
        if sell>buy:
            print("you can buy the stock at", buy, "and sell it at", sell, "to make a profit of", sell-buy)
            break


# optimal approach same as mine but the way to write the code is bit different

prices=[7,1,5,3,6,4]
min_price=float('inf')
max_price=0

for price in prices:
    min_price=min(min_price,price)
    profit=price-min_price
    max_price=max(max_price,profit)

print(max_price)