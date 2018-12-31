def main():
    
        score1 = input('Enter score 1: ')
        letter_grade1 = determine_grade(score1)
        print 'Letter grade for score 1', letter_grade1
        score2 = input('Enter score 2: ')
        letter_grade2 = determine_grade(score2)
        print 'Letter grade for score 2', letter_grade2
        score3 = input('Enter score 3: ')
        letter_grade3 = determine_grade(score3)
        print 'Letter grade for score 3', letter_grade3
        score4 = input('Enter score 4: ')
        letter_grade4 = determine_grade(score4)
        print 'Letter grade for score 4', letter_grade4
        score5 = input('Enter score 5: ')
        letter_grade5 = determine_grade(score5)
        print 'Letter grade for score 5', letter_grade5
    
        avg_score = calc_average(score1, score2, score3, score4, score5)

        print 'The class average score is %.2f' % avg_score

def calc_average(score1, score2, score3, score4, score5):

    sum_score = score1 + score2 + score3 + score4 + score5
    avg_score = sum_score / 5
    return avg_score

def determine_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60  and score < 70:
        return 'D'
    elif score < 60:
        return 'F'
        
main()
