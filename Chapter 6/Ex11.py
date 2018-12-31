##Write a program that accepts as input a sentence
##in which all of the words are run together but the first
##character of each word is uppercase. Convert the sentence to a string
##in which the words are separated by spaces and only the first word starts
##with an uppercase letter.
##For example the string “StopAndSmellTheRoses.”
##would be converted to “Stop and smell the roses.”


def main():

    sent = raw_input('Enter a sentence: ')

    sent_sum = ' '

    for i in range(len(sent)):

        if sent[i] >= 65 and sent[i] <= 90 and i != 0:
            sent_sum[i] = ' '
            sent_sum += sent[i+1]
            
        else:
            sent_sum += sent[i]
            
    converted_sentence = sent_sum 


    print converted_sentence



main()
