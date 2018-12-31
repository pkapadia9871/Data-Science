##Write a program with a loop that asks the user to
##enter a series of positive numbers.
##The user should enter a negative number to signal the end of the series.
##After all the positive numbers have been entered,
##the program should display their sum.


def main():

    print 'Start entering numbers in the sequence , but only positive numbers: ' 
    sum_ = 0

    x = 1

    while x == 1:
        ## x is a sentinel variable that ensures that
        ## if a negative number is input, it will be set to another value
        ##which ends the while loop and proceeds to printing the sum
        ##of the sequence.
        num =  input('Enter a number: ')
        if num < 0:
            x = 0
            print 'The sequence is over. '

        sum_ = sum_ + num

    total_sum = sum_
    


    print 'The sum of the sequence is: ', total_sum

main()
