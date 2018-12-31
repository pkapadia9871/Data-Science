def main():

    cost = input('Enter the cost to replace the structure: $')
    insure_cost(cost)

def insure_cost(cost):
    insured_cost = 0.80 * cost
    print 'The minimum cost of insurance to replace the structure is: $', '%.2f' %insured_cost


main()
        
