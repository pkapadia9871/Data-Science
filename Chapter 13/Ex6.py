##Design a function that accepts an integer argument and
##returns the sum of all the integers from 1 up to the number passed as an
##argument. For example, if 50 is passed as an argument, the function will
##return the sum of 1, 2, 3, 4, . . . 50.
##Use recursion to calculate the sum. 

def main():

    n = input('Enter an integer: ')
    
    s = sum_B(n)

    print 'The sum of all of the integers from 1 to', n, 'is', s

def sum_B(n):

    if n == 1:
        return 1
    elif n > 1:
        return n + sum_B(n-1)
main()
