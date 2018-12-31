#115 sqft requires:
#1 gal of paint
#8 hr labor
#20.00/hr for labor
#Enter the area of wall space in square feet
#Enter the price of paint per gallon


def main():
    sqft = input('Enter the square feet of wall space to be painted: ')
    paintprice = input('Enter the price of paint per gallon: $')
    laborperhour = 20.00
    pr = paint_req(sqft)
    lr = labor_req(sqft)
    cp = cost_pt(paintprice,sqft)
    lc = labor_charge(sqft,laborperhour)
    tc = total_cost(pr,lr,cp,lc)
    print 'Amount of paint required in gallons: ', pr
    print 'Hours of labor required: ', lr, ' hours'
    print 'Cost of paint: $', cp
    print 'Labor charge: $', lc
    print 'Total cost: $', tc

def paint_req(sqft):
    
    return (sqft / 115)

def labor_req(sqft):

    return (sqft * 8 / 115)

def cost_pt(paintprice,sqft):

    return (sqft * 8 / 115) * paintprice
    
def labor_charge(sqft,laborperhour):
    
    return (sqft * 8 / 115) * laborperhour
    
def total_cost(pr,lr,cp,lc):

    tc = pr+lr+cp+lc
    return tc

main()
