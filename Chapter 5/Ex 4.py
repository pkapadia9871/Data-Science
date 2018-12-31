##The distance a vehicle travels can be calculated as follows: distance, speed, time
##For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles.
##Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled.
##It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.
##Here is an example of the desired output:


def main():
    mph = input('Enter the speed of the vehicle in mph: ')
    hours = input('Enter the time taken by the vehicle to travel this distance in hours: ')
    inc_hours = 1

    while inc_hours <= hours:
        inc_dist = mph * inc_hours
        print 'The distance traveled in ', inc_hours, ' hours = ', inc_dist, ' miles'
        inc_hours = inc_hours + 1

main()
