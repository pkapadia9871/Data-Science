def main():

    correct_answers = [0]*20

    for index in range(20):
        print 'If you are the exam writer, start creating the correct answers: '
        print index
        correct_answers[index] = input( '.')
        
    your_answers = [0]*20

    for index in range(20):
        print 'If you are the exam taker, start entering your own answers'
        print index
        your_answers[index] = input( '.')

    print 'Let us see how many correct answers you got: '

    correct = 0

    for index in range(20):
        if correct_answers[index] == your_answers[index] :
            correct = correct + 1

    if correct >= 15:
        print 'You passed the exam'
    else:
        print 'You failed the exam'

    print 'You answered ', correct, ' answers correctly and ', (20-correct), 'answers incorrectly.'

    print 'You answered the following question numbers incorrectly: '
    for index in range(20):
        if correct_answers[index] != your_answers[index] :
            print (index+1)

main()
