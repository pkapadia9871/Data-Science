##In this chapter you saw an example of how to write an algorithm
##that determines whether a number is even or odd.
##Write a program that generates 100 random numbers,
##and keeps a count of how many of those random numbers are even and
##how many are odd.

def main():

    print 'Start entering 100 numbers: ' 
    even = 0
    odd = 0

    for i in  range(1,101):
        x = input('Enter a number: ')
        if x%2 == 0:
            even = even + 1
        elif x%2 == 1:
            odd = odd + 1
    print 'The number of even numbers is ', even
    print 'The number of odd numbers is ', odd  


main()
