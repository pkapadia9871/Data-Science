price1 = input('Enter the the price of item 1: $')
price2 = input('Enter the the price of item 2: $')
price3 = input('Enter the the price of item 3: $')
price4 = input('Enter the the price of item 4: $')
price5 = input('Enter the the price of item 5: $')
subtotal = price1+price2+price3+price4+price5
print 'Subtotal = $', '%.2f' %subtotal 
tax = 0.06 * subtotal
totalprice = subtotal+tax
print 'Tax: $', '%.2f' %tax
print 'Total price = $', '%.2f' %totalprice
