##Enter the length and width of two rectangles
##Compare the two areas
##Then tell the user which one has the greater area:

def main():

    books = input('Enter the number of books: ')

    if books == 0:
        print 'You earned 0 points'
    elif books == 1:
        print 'You earned 5 points'
    elif books == 2:
        print 'You earned 10 points'
    elif books == 3:
        print 'You earned 15 points'
    elif books >= 4:
        print 'You earned 30 points'
 
main()

