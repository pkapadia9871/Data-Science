def main():

    g = 9.8
    for t in range(1,11):
        d = falling_distance(t,g)
        print 'The distance in meters for t = ', t , ' seconds is : ', d , ' meters.' 
        

def falling_distance(t,g):
    
    return (g * t * t / 2)

main()
