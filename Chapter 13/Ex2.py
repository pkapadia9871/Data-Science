
def main():

    x = input('Enter x: ')
    y = input('Enter y: ')
    prod = mult(x,y)
    print 'The product of x and y =', prod

def mult(x,y):

    p = 0
    
    if y > 0:
       p = (x + mult(x, y-1))
    return p
main()
