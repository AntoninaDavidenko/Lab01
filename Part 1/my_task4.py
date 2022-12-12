import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W", help="capacity")
parser.add_argument("-w", nargs="+", type=int, help="weights")
parser.add_argument("-n", help="bars_number")


args = parser.parse_args()

weights = (args.w)
capacity = int(args.W)
number = int(args.n)
weights.sort()
weights.reverse()

count = 0
for item in weights:
    if count + item < capacity:
        count += item
print(f"{count} is maximum weight of gold that fits into a knapsack with capacity of {capacity}")
