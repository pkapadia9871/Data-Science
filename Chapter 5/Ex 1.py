##A bug collector collects bugs every day for seven days.
##Write a program that keeps a running
##total of the number of bugs collected during the seven days.
##The loop should ask for the number of bugs collected for each day,
##and when the loop is finished,
##the program should display the total number of bugs collected.


def main():
    bugs = 0
    days = 1
    while days <=7:
        print 'Day ', days
        add_bugs = input('Enter the number of bugs today: ')
        bugs = bugs + add_bugs
        print 'The number of bugs collected today', add_bugs
        days = days+1

    print 'The total number of bugs collected over the course of 7 days = ', bugs


main()
