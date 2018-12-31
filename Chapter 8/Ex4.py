##Design a program that asks the user to enter a series of 20 numbers.
##The program should store the numbers in a list
##and then display the following data:
##The lowest number in the list
##The highest number in the list
##The total of the numbers in the list
##The average of the numbers in the list

n = 5

def main():
##numbers contains a series of 20 numbers



    numbers = [0]*n

    index = 0

    lowest = 0
    highest = 0
    total = 0
    

    while index <= (n-1):
        print 'Day ', (index + 1)
        numbers[index] = input('Enter the numbers: ')
        total = total + numbers[index]
        index = index + 1

    index = 0
    
    while index <= (n-2):
        if numbers[index] < numbers[index+1]:
            highest = numbers[index+1]
        elif numbers[index] > number[index+1]:
            highest = numbers[index]
        index = index+1

    index = 0

    while index <= (n-2):
        if numbers[index] > numbers[index+1]:
            lowest = numbers[index+1]
        elif numbers[index] < numbers[index+1]:
            lowest = numbers[index]
        index = index + 1
            
    avg = total / n

    print 'The highest of the numbers is $', highest
    print 'The lowest of the numbers is $', lowest
    print 'The total of the numbers is $', total
    print 'The average of the numbers is $', avg


main()
    


    
