def add(nums):
    total = 0
    for adder in nums:
        total += adder
    return f'Answer = {total:.2f}'

def subtract(nums):
    total = nums[0]
    for subber in nums[1:]:
        total -= subber
    return f'Answer = {total:.2f}'

def multiply(nums):
    total = nums[0]
    for muller in nums[1:]:
        total *= muller
    return f'Answer = {total:.2f}'

def divide(nums):
    total = nums[0]
    for divver in nums[1:]:
        total /= divver
    return f'Answer = {total:.2f}'

if (__name__ == '__main__'):
    print("testing formula module")