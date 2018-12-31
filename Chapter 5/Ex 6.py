def main():
    
    c = 0
    print 'The temperature at the start is 0 degrees Celsius'
    
    while c <= 20:
        
        f =  float((9/5)*c + 32)
        
        print 'Temperature in farenheit at ', c , ' degrees celsius is ', float(f) , ' degrees farenheit.'
        c = c + 1

main()
