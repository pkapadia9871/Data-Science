##Write a program that calculates the amount of money a person would earn over
##a period of time if his or her salary is one penny the first day,
##two pennies the second day, and continues to double each day.
##The program should ask the user for the number of days.
##Display a table showing what the salary was for each day, and then show the total pay at the end of the period.
##The output should be displayed in a dollar amount, not the number of pennies.


def main():
    print 'You
    have 1 penny today. '
    salary = 0.01;

    ##salary = 1 penny = $0.01

    days = input('Enter the number of days: ')

    new_salary = salary

    inc_days = 1

    total_salary = 0

    while inc_days <= days:
        
        new_salary = 2*new_salary
        print 'Your new salary after ', inc_days, ' days is $', new_salary
        inc_days = inc_days + 1
        total_salary = total_salary + new_salary

    period_salary = total_salary + salary
    print 'The total pay at the end of the period = $', (period_salary)


main()
