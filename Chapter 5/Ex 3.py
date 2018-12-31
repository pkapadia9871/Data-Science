##Write a program that asks the user to enter the amount
##that he or she has budgeted for a month.
##A loop should then prompt the user to enter each of his or her expenses
#for the month, and keep a running total.
##When the loop finishes,
##the program should display the amount that the user is over or under budget.

def main():
    budget = input('Enter the budget for this month: $')
    month = 1
    expenses = 0
    while month == 1:
        
        add_expenses = input('Enter some expenses from the budget for this month: $')
        expenses = expenses + add_expenses
        print 'The total expenses for the month has amounted to: ', expenses

        month = input('Are you done entering the expenses for the month? Click 0 if yes, and 1 if no. ')
        

        if expenses > budget:
            print 'Over budget'
        elif expenses < budget:
            print 'Under budget'
        elif expenses == budget:
            print 'At budget'

main()
