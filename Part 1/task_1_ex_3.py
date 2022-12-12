import argparse


def func(string):
    x = ""
    number = 0
    pr_sign = None
    double_sign = True
    for item in string:

        if item == "+" or item == "-":
            if double_sign:
                return False, None

            if pr_sign:
                if pr_sign == "+":
                    number += int(x)
                    x = ""
                    pr_sign = item
                    double_sign = True
                elif pr_sign == "-":
                    number -= int(x)
                    x = ""
                    pr_sign = item
                    double_sign = True
            else:
                if item == "+":
                    number = int(x)
                    x = ""
                    pr_sign = "+"
                    double_sign = True

                elif item == "-":
                    number = int(x)
                    x = ""
                    pr_sign = "-"
                    double_sign = True

        elif item == "0" or item == "1" or item == "2" or item == "3" or item == "4" or item == "5" or item == "6" or item == "7" or item == "8" or item == "9":
            x += item
            double_sign = False

        else:
            return False, None
    if double_sign:
        return False, None
    if pr_sign == None:
        number = int(x)
    if pr_sign == "+":
        number += int(x)
    if pr_sign == "-":
        number -= int(x)
    return True, number


parser = argparse.ArgumentParser()

parser.add_argument("string", help="string", default=False, nargs="?")

args = parser.parse_args()

string = str(args.string)
if string:
    print(func(string))
else:
    print(False, None)