##Running on a particular treadmill you burn 3.9 calories per minute.
##Write a program that uses a loop to display the
##number of calories burned after 10, 15, 20, 25, and 30 minutes.

def main():
    
    mins = 10
    cals = input('Enter the number of calories you have with you at the start, which is 0 minutes: ')
    
    while mins <=30:
        print 'Number of minutes gone by: ', mins
        
        reduced_cals = cals - (3.9 * mins)
        
        print 'The number of calories burned after ', mins , 'minutes is ', reduced_cals, ' calories'
        mins = mins+5

        
main()
