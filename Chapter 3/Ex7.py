def main():
    fatgrams = input('Enter the number of fat grams: ')
    carbgrams = input('Enter the number of carb grams: ')
    fat(fatgrams)
    carbs(carbgrams)
    

def fat(fatgrams):
    cal_fat = fatgrams * 9
    print 'Calories from fat = ', cal_fat

def carbs(carbgrams):
    cal_carb = carbgrams * 4
    print 'Calories from carb = ', cal_carb

main()
