##Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
##The program should first ask for the number of years.
##The outer loop will iterate once for each year.
##The inner loop will iterate twelve times, once for each month.
##Each iteration of the inner loop will ask the user for
##the inches of rainfall for that month.
##After all iterations, the program should display:
##the number of months,
##the total inches of rainfall
##and the average rainfall per month for the entire period.

def main():

    years = input('Enter the number of years: ')
    months = years * 12
    add_year = 1
    inch_year = 0

    while add_year <= years:
        
        inch_year = 0
        add_month = 1
        
        while add_month <= 12:
            print add_month
            add_inch_month = input('Enter the inches of rain for this month : ')
            inch_year = inch_year + add_inch_month     
            add_month = add_month + 1

        total_inch = inch_year 

        add_year = add_year + 1

    total_inch_period = total_inch

    print 'The number of months = ', months
    print 'The total inches of rainfall for the entire period: ', total_inch_period 
    avg_inch = total_inch_period / months
    print 'The average rainfall in inches per month for the entire period = ', avg_inch


main()
