import random as r
def total_stonks(price):
    stonk = 0
    for s in range(1, len(price)):
        if price[s] > price[s - 1]:
            stonk += price[s] - price[s - 1]

    return stonk


minisizeinput = int(input("Input minimum array size: "))
maxsizeinput = int(input("Input maximum array size: "))
n = int(input("Enter random start_value price: "))
m = int(input("Enter random end_value price: "))

size = r.randint(minisizeinput, maxsizeinput)

stonkers = [1] * size

for i in range(size):
    if r.random() < 0.5:
        stonkers[i] = r.randint(n, m)

print(f"total_stonks({stonkers}) = {total_stonks(stonkers)}")