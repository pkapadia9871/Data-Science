def main():

    m = input('Enter m: ')
    n = input('Enter n: ')
    a = ackermann(m,n)
    print 'Ackermann = ', a

def ackermann(m,n):
    if m == 0:
        return (n+1)
    elif n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))

main()
