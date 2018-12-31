
##Design a recursive function that accepts an integer argument, n,
##and prints the numbers 1 up through n.

##This one is complicated to think of, because the only idea that I can think of
##is a function that passes two arguments as a requirement for
##printing the numbers in the forward direction 1-N, whereas this one can
##only pass one, and it ends up printing in the reverse direction.

def main():

    n = input('Enter an integer: ')
    
    print_n(n)

def print_n(n):

    if n > 1:
        print n
        print_n(n-1)
    elif n == 1:
        print 1
    
main()
