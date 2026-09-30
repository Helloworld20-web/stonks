def profits(n):
    stonk = list(range(n, 0, -1)) + list(range(1, n + 1))

    min_stonks, profit = stonk[0], 0

    for s in stonk:
        min_stonks = min(min_stonks, s)


        profit = max(profit, s - min_stonks)

        
    return profit

#steps = int(input("Enter steps:"))
mony = int(input("Enter a Number: "))

print(f"max_profit({mony}) = {profits(mony)}")