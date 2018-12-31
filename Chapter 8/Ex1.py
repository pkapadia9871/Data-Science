##Design a program that asks the user to enter a store’s sales for each day of
##the week. The amounts should be stored in a list.
##Use a loop to calculate the total sales for the week and display the result.

def main():
##numbers is an array containing the sales for each day of the week
    days = 7
    numbers = [0]*days

    index = 0

    total_sales = 0

    while index <= 6:
        print 'Day ', (index + 1)
        numbers[index] = input('Enter the sales for today: $')
        total_sales = total_sales + numbers[index]
        index = index + 1
        
    print 'The total sales for the week is $', total_sales


main()
    


    
