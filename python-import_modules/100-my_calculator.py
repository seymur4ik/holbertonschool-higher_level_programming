#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operates = ("+", "-", "*", "/")
        functions = (calc.add, calc.sub, calc.mul, calc.div)
        a = sys.argv[1]
        b = sys.argv[3]
        for i in range(0, 4):
            if sys.argv[2] == operates[i]:
                op = operates[i]
                f = functions[i]
                print("{} {} {} = {}".format(a, op, b, f(int(a), int(b))))
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
