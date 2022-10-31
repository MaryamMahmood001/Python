size = int(input())
price = list(map(int,input().split()))

# Initialize current_min_stock by first day price of stock
current_min_stock = price[0]

# Initialize max_profit to zero ( 0 ) 
max_profit = 0

for i in range(0, size):
    
    # Each DAY checking for MINIMUM STOCK PRICE
    current_min_stock = min(current_min_stock, price[i])
    
    # using MINIMUM STOCK PRICE finding the MAXIMUM PROFIT 
    max_profit = max(max_profit, price[i]-current_min_stock)

# print the MAXIMUM PROFIT
print(max_profit)
