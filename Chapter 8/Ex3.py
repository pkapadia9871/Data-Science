##Design a program that lets the user enter the total rainfall
##for each of 12 months into a list.
##The program should calculate and display the total rainfall for
##the year, the average monthly rainfall,
##and the months with the highest and lowest amounts.

def main():
##numbers is an array containing the rainfall for each months of the year
    months = 12
    numbers = [0]*months

    index = 0

    total_rainfall = 0

    while index <= (months-1):
        print 'Month ', (index + 1)
        numbers[index] = input('Enter the rainfall for this month in inches: ')
        total_rainfall = total_rainfall + numbers[index]
        index = index + 1
        
    print 'The total rainfall for the year is $', total_rainfall, 'inches'
    avg_rainfall = float(total_rainfall / months)
    print 'The average rainfall for the year', avg_rainfall, 'inches'
    
main()
    


    
