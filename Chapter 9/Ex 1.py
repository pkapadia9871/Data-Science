## Write a program to input the first, middle and last names
## Output the initials
## Sample input : John William Smith
## Output: J.W.S

def main():
    first = raw_input('Enter the first name: ')
    middle = raw_input('Enter the middle name: ')
    last = raw_input('Enter the last name: ')
    print_initials(first, middle, last)

def print_initials(first, middle, last):
    first_initial = first[0]
    middle_initial = middle[0]
    last_initial = last[0]
    print first_initial, '.', middle_initial, '.', last_initial, '.'

main()
