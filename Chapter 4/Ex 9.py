def main():
    
    weight = input('Enter the weight of the package in pounds: ')
    if weight < 2:
        charges = weight * 1.10
    elif weight < 6 and weight > 2:
        charges = weight * 2.20
    elif weight < 10 and weight > 6:
        charges = weight * 3.70
    elif weight > 10:
        charges = weight * 3.80 

    print 'The shipping charges = $' , charges

main()
