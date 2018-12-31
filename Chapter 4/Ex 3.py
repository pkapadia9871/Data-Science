def main():
    
    weight = input('Enter the mass of the person in kilograms: ')

    weight = weight_calc(weight)
    print 'The weight of the object is: ', '%.2f' %weight

    if weight < 10 :
        print 'Too light'
    elif weight > 1000:
        print 'Too heavy'        

def weight_calc(mass):
    weight = mass * 9.8
    return weight

main()
