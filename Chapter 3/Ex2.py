def main():
    amount = input('Enter the amount of a purchase: ')
    stateandcountytax(amount)

def stateandcountytax(amount):
    state_tax = 0.04 * amount
    print 'The state tax =  ', '%.2f' %state_tax
    county_tax = 0.02 * amount
    print 'The county tax =  ', '%.2f' %county_tax
    totaltax(amount, county_tax, state_tax)
    
def totaltax(amount, county_tax, state_tax):
    total_tax = state_tax + county_tax
    print 'The total sales tax =  ', '%.2f' %total_tax  
    totalamount(amount, total_tax)
    
def totalamount(amount, total_tax):
    total_amount = amount + total_tax
    print 'The total of the sale =  ', '%.2f' %total_amount

main()
