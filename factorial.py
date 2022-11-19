import sys

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    nums = sys.argv[1:]
    print('Computing the factorial of',nums)
    for num in nums:
        num = int(num)
        result = factorial(num)
        print('The factorial of {} is {}'.format(num,result))

