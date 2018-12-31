#Write a function named maximum that accepts two integer values as arguments
##and returns the value that is the greater of the two.
##For example, if 7 and 12 are passed as arguments to the function,
##the function should return 12.
##Use the function in a program that prompts the user to
##enter two integer values.
##The program should display the value that is the greater of the two.

def main():
    int1 = input('Enter the first integer: ')
    int2 = input('Enter the second integer: ')

    greater_int = maximum(int1,int2)

    print 'The greater of the two numbers is ', greater_int
    
    

def maximum(int1,int2):

    if int1 < int2:
        return int2
    elif int1 > int2:
        return int1
    else:
        return 0

main()
