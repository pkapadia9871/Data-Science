def main():
    no = input('Enter a number: ')

    status = is_prime(no)

    if status == True:
        print 'The number is prime'
    elif status == False:
        print 'The number is not prime'

def is_prime(no):

    x = 0
    for i in range(2,no):
        if (no % i == 0):
            x = x+1
    if x == 0:
        return True
    else:
        return False

main()
