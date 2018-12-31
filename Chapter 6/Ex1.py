##One foot equals 12 inches.
##Write a function named feet_to_inches that
##accepts a number of feet as an argument,
##and returns the number of inches in that many feet.
##Use the function in a program that prompts the user
##to enter a number of feet
##and then displays the number of inches in that many feet.


def main():
    feet = input('Enter the length in feet: ')

    inch = feet_to_inches(feet)

    print 'The length in inches is ', inch, ' inches.'


def feet_to_inches(feet):

    inches = feet * 12

    return inches


main()
