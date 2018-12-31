def main():

    unitpack = 99 
    packno = input('Enter the number of package purchased: ')
    
    if packno < 20 and packno >= 10:
           discount = 0.20
    elif packno < 50 and packno >= 20:
           discount = 0.30
    elif packno < 100 and packno >= 50:
           discount = 0.40
    elif packno >= 100 :
           discount = 0.50
           
    princ_amt = unitpack * packno
    print 'The principal amount bought = $', princ_amt
    discamount = princ_amt * discount
    print 'The amount of discount = $', discamount 
    total_amt =  princ_amt - discamount
    print 'The total amount after discount = $', total_amt


main()
