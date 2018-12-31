##Assume that a file containing a series of integers is named numbers.txt and
##exists on the computer’s disk.
##Write a program that displays all of the numbers in the file.

##This code is based on Program 7.2, which has a similar theme.
def main():
        infile = open('numbers.txt', 'r')

        file_contents = infile.read()

        infile.close()
    
        print(file_contents)
