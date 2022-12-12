import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", help="first number")
parser.add_argument("operation", help="operation")
parser.add_argument("num2", help="second number")


args = parser.parse_args()

n1 = int(args.num1)
n2 = int(args.num2)

if args.operation == "+":
    result = n1 + n2
    print("The Result is : ", result)

elif args.operation == "-":
    result = n1 - n2
    print("The Result is : ", result)

elif args.operation == "*":
    result = n1 * n2
    print("The Result is : ", result)

elif args.operation == "/":
    result = n1 / n2
    print("The Result is : ", result)
else:
    print("Unmatched Argument")