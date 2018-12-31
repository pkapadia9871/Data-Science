##The program asks the user to enter a time length in seconds
##and based on the given conditions, it will convert it to its respective number
##of minutes, hours, or days
##I assume that the question is asking me to print the numbers in terms of their
##nearest lower integer.

def main():
    seconds = input('Enter the time in seconds: ')

    if seconds >= 60 and seconds < 3600:
        mins = seconds / 60
        print 'The time in minutes = ', mins

    elif seconds >= 3600 and seconds < 86400:
        hrs = seconds / 3600
        print 'The time in hours = ', hrs

    elif seconds >= 86400:
        days = seconds / 86400
        print 'The time in days = ', days



main()
