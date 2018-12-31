
# This program accepts an input of distance in miles
# and converts it to kilometers

def main( ):
    miles = input('Enter the distance in miles: ')
    # Call the mil_to_km function.
    mil_to_km(miles)

def mil_to_km(miles):
    km = miles / 0.6214
    print miles, 'miles = ', '%.2f' %km, 'km'
        

#call the main function
main()
