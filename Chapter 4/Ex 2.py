##Enter the length and width of two rectangles
##Compare the two areas
##Then tell the user which one has the greater area:

def main():

    length1 = input('Enter the length of the first rectangle: ')
    width1 = input('Enter the width of the first rectangle:')

    length2 = input('Enter the length of the second rectangle: ')
    width2 = input('Enter the width of the second rectangle:')
    
    area1 = length1 * width1
    area2 = length2 * width2

    print 'The first area is: ', area1 
    print 'The second area is: ', area2

    if area1 > area2:
        print 'Rectangle 1 has the greater area.'
    elif area1 < area2:
            print 'Rectangle 2 has the greater area.'
    elif area1 == area2:
            print 'Rectangles 1 and 2 have the same area.' 
main()

