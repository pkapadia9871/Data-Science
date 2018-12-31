#Input the property value
#Calculate the assessment value = 0.6 * property value
#Calculate property tax = ((0.64)/100) * (assessment value)


def main():

    prop_value = input('Enter the property value: $')

    av = assess_val(prop_value)
    pt = proptax(av)

    print 'The assessment value is: $', '%.2f' %av
    print 'The property tax paid is: $', '%.2f' %pt


def assess_val(prop_value):
    return (prop_value * 0.6) 


def proptax(av):
    return (av * 0.64 / 100)


main()
