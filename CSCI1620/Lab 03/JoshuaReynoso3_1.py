import sys
import formulas

def main():
    if len(sys.argv) <= 1:
        sys.exit("Need to provide operator name")
    elif len(sys.argv) <= 3:
        sys.exit("Need to provide at least two values or more")
    else:
        nums_float = [float (x)*1.00 for x in sys.argv[2:]]
        oper(sys.argv[1],nums_float)

def oper(operation, nums):
    if operation == 'add':
        print(formulas.add(nums))
    elif operation == 'subtract':
        print(formulas.subtract(nums))
    elif operation == 'multiply':
        print(formulas.multiply(nums))
    elif operation == 'divide':
        if 0 not in nums[1:]:
            print(formulas.divide(nums))
        else:
            sys.exit("Cannot divide by 0")
    else:
        sys.exit("Need to provide valid operation name (add, subtract, multiply, divide)")

if (__name__ == '__main__'):
    main()