charge = input('Charge for food = $')
tip = 15* charge / 100
tax = 7 * charge/ 100
total_amount = charge + tip + tax
print 'Charge for food = $', '%.2f' %charge
print 'Tip = $', '%.2f' %tip
print 'Tax = $', '%.2f' %tax
print 'Total amount = $', '%.2f' %total_amount
