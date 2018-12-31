##Write a recursive function that accepts an integer argument, n.
##The function should display n lines of asterisks on the screen,
##with the first line showing 1 asterisk, the second line showing 2 asterisks,
##up to the nth line which shows n asterisks.


##This one is complicated to think of, because the only idea that I can think of
##is a function that passes two arguments as a requirement for
##printing the asterisks a number of times
##in the forward direction 1-N, whereas this one can
##only pass one, and it ends up printing in the reverse direction.
##For visual clarity, this prints the asterisks N times first, then
##(N-1) times, and so on, instead of in the reverse direction.


def main():

    n = input('Enter the number of lines: ')
    
    disp(n)
    
def disp(n):

    print '*' * n
    if n > 1:
        disp(n-1)

main()
