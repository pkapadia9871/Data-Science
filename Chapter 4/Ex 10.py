def main():
    
    weight = input('Enter the weight of the person in pounds: ')
    height = input('Enter the height of the person in inches: ')

    bmi = bmi_calc(weight, height)
    print 'The BMI of the person is: ', '%.2f' %bmi

    if bmi < 25 & bmi > 18.5:
        print 'Normal'
    elif bmi > 25:
        print 'Overweight'        
    if bmi < 18.5:
        print 'Underweight'


def bmi_calc(weight, height):
    bmi = (weight * 703 / (height**2))
    return bmi

main()
