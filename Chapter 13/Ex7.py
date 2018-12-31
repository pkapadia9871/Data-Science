##Design a function that uses recursion to raise a number to a power.
##The function should accept two arguments: the number to be raised and the exponent.
##Assume that the exponent is a nonnegative integer.

def main():

    n = input('Enter an integer: ')
    p = input('Enter a power: ')
    
    s = expow(n,p)

    print 'The base', n,'to the power', p, 'is', s 

def expow(n,p):

    if n == 1:
        return 1
    elif p == 1:
        return n
    elif p == 0:
        return 1
    elif p > 1:
        return n * expow(n,p-1)
main()
