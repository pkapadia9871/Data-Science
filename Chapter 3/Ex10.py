##File taxes for a retail company
##Enter the total sales for the month
##Calculate state sales tax rate at 4%
##Calculate county sales tax rate at 2%
##Calculate total sales tax rate

def main():
    sales_month = input('Enter the total sales : $')

    
    st = state_Tax(sales_month)
    ct = county_Tax(sales_month)
    tt = total_tax(st,ct)

    print 'The state tax is $', '%.2f' %st
    print 'The county tax is $', '%.2f' %ct
    print 'The total tax is $', '%.2f' %tt



def state_Tax(sales_month):
    return (sales_month * 0.04)

def county_Tax(sales_month):
    return (sales_month * 0.02)

def total_tax(st,ct):
    return (st+ct)

main()
