##Enter a number between 1 and 10.
#If the number is less than 1 or more than 10, display an error message
#Otherwise, display its corresponding roman numeral.

def main():

    numer = input('Enter a number: ')

    roman(numer)

def roman(numer):

    if numer == 1:
        print 'I'
    elif numer == 2:
        print 'II'
    elif numer == 3:
        print 'III'
    elif numer == 4:
        print 'IV'
    elif numer == 5:
        print 'V'
    elif numer == 6:
        print 'VI'
    elif numer == 7:
        print 'VII'
    elif numer == 8:
        print 'VIII'
    elif numer == 9:
        print 'IX'
    elif numer == 10:
        print 'X'
    else :
        print 'error' 

main()
