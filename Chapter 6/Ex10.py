import math

def main():

    p = input('Enter the principal amount: $')
    i = input('Enter the monthly interest rate in %: ')
    t = input('Enter the number of months: ')

    f = comp_int(p,i,t)

    print 'The future value = $%.2f' %f  

def comp_int(p,i,t):

    future_value = p * pow(1+ (i/100.0),t)

    return future_value

main()
