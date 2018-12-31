##Design a function that accepts a list as an argument,
##and returns the largest value in the list.
##The function should use recursion to find the largest item. 

##The development for this problem is complicated, in a context similar to
##that of questions 1 and 3 - I cannot think of the right words to describe it
##as.

def main():

    n = input('Enter the number of items to be input: ')

    user_list = 0*[n]

    for i in range(n-1):
        user_list[i] = input('Enter each item: ')

    largest = largest_item(user_list,n)

    print 'The largest item in the list is : ', largest

def largest_item(user_list,n):

    if user_list(n) < user_list(n-1):
        return user_list(n-1)
    else:
        return largest_item(n-1)
    


main()
