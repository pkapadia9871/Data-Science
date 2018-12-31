def main():

    number = raw_input('Enter a number: ')
    print 'Now I will calculate the sum of its digits: ' 
    sum_of_digits(number)


def sum_of_digits(number):

    sum = 0 ;
    for ch in number:
        sum = sum + int(ch)


    print 'The sum of its digits is: ', sum
    
main()
