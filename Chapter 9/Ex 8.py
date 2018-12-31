##Accept a string as an argument
##Return a copy of the string with each character of each sentence captialzied.




def main():

    strinp = raw_input('Enter a string: ')

    x = len(strinp)
    
    capstr = strcap(strinp,x)

    print 'The string with the first letter of each sentence capitalized is:',capstr


def strcap(strinp,x):

    for i in range(x):
        if strinp[i] == '.' and i < (len(strinp)-1):
            strinp[i+1] = (strinp[i+1]).upper()

    strcapv = strinp

    return str_capv


main()    
