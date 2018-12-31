def main():
    print('The cost of a Class A ticket is $15 ')
    print('The cost of a Class B ticket is $12 ')
    print('The cost of a Class C ticket is $9 ')
    tick_a = input('Enter the number of tickets sold for class A: ')
    tick_b = input('Enter the number of tickets sold for class B: ')
    tick_c = input('Enter the number of tickets sold for class C: ')
    total_cost(tick_a,tick_b,tick_c)

def total_cost(tick_a,tick_b,tick_c):

    cost_a = 15 * tick_a
    cost_b = 12 * tick_b
    cost_c = 9 * tick_c
    tot_c = cost_a + cost_b + cost_c 
    print 'The total cost of the tickets sold', '%.2f' %tot_c

main()



    
