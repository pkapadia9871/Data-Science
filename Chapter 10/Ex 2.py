##Write a program that creates a dictionary containing the U.S. states as keys and their capitals
##as values. (Use the Internet to get a list of the states and their capitals.)
##The program should then randomly quiz the user by displaying the
##name of a state and asking the user to enter that state’s capital.
##The program should keep a count of the number of correct and
##incorrect responses.
##Here, instead, quiz them on countries instead of states:

def main():

        countries = {'France': 'Paris', 'UK' : 'London', 'Italy': 'Rome'}

        correct = 0
        for key in countries:
            key_in = raw_input('What is the capital of: ' + key +'\n')
            if key_in == countries[key]:
                correct = correct + 1
        print 'You got ', correct, ' answers correct and ', (3-correct), ' answers incorrect.'
        
main()
