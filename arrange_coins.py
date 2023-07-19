def arrange_coins(coins):
    num=0
    while coins>=num*(num+1)/2:
        num+=1
    return num-1

coins=int(input("Enter the Number of Coins : "))
print(arrange_coins(coins))