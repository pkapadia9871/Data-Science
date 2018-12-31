##Design a function that accepts a list of numbers as an argument.
##The function should recursively calculate the sum of all the numbers in
##the list and return that value.

def main():

    i = input('Enter the number of numbers, or the list of the list: ')
    a = [0]*i

    for i in range(len(a)):
        a[i] = input('Enter a number: ')

    s = sum_n(a,i)

    print 'The sum of the numbers in the list = ', s

def sum_n(a,i):

    if i == 0:
        return a[0]
    elif i > 0:
        return a[i] + sum_n(a,i-1)



main()
    
