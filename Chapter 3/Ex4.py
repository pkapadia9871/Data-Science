def main():
     lp = input('Enter the loan payment: $')
     ins = input('Enter the insurance: $')
     gas = input('Enter the gas: $')
     oil = input('Enter the oil: $')
     tires = input('Enter the tires: $')
     maint = input('Enter the maintenance: $')
     monthc = month_cost(lp,ins,gas,oil,tires,maint)
     print 'The monthly cost is: $', '%.2f' %monthc
     annc = ann_cost(monthc)
     print 'The annual cost is : $', '%.2f' %annc

def month_cost(lp,ins,gas,oil,tires,maint):

    m_cost = lp + ins + gas + oil + tires + maint
    return m_cost
  

def ann_cost(mon_cost):
    a_cost = 12 * mon_cost
    return a_cost
             
main()             
