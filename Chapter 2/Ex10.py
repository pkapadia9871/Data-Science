shares = 1000
pricepersharebought = 32.87
comm = 0.02
pricepersharesold = 33.92


amount_stock = shares * pricepersharebought
commission_bought = comm * amount_stock
amount_sold_for = shares * pricepersharesold
commission_sold = comm * amount_sold_for
amount_left = amount_sold_for - amount_stock

print 'Amounth paid for stock = $', '%.2f' %amount_stock
print 'Commission bought = $', '%.2f' %commission_bought
print 'Amount sold for = $', '%.2f' %amount_sold_for
print 'Amount commission sold = $', '%.2f' %commission_sold
print 'Difference between sold and bought price = $', '%.2f' %amount_left

if amount_left < 0:
    print 'Joe made a Loss'
if amount_left > 0:
    print 'Joe made a Profit'
    
