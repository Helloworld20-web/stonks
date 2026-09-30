# 03-rainwater.py
import random as r
# Topic: Left tallest bars, Right tallest bars, Rainwater trapped

def rainwater(bars): # Defines a function called rainwater that takes one argument, n.
    
    
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

minisizeinput = int(input("Input minimum array size: "))
maxsizeinput = int(input("Input maximum array size: "))
n = int(input("Enter random start_value bar height: "))
m = int(input("Enter random end_value bar height: "))

size = r.randint(minisizeinput, maxsizeinput)

barsed = [0] * size

for i in range(size):
    if r.random() < 0.5:
        barsed[i] = r.randint(n, m)

print(f"rainwater trapped({barsed}) = {rainwater(barsed)}")