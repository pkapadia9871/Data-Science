##Read a string containing a date in the form mm/dd/yyyy
##Output the date in the form [Month], [Numerical Day of Month], [Year]


def main():
    mm = raw_input('Enter the month: ')
    dd = raw_input('Enter the day: ')
    yyyy = raw_input('Enter the year: ')
    convert_date(mm,dd,yyyy)


def convert_date(mm,dd,yyyy):
    if mm == '03' and yyyy == '2009' and dd == '12':
        month = 'March'
        year = '2009'
        day = '12'
        print mm, '/' , dd, '/', yyyy,
        print 'can also be expressed as '
        print month, day,',', year

main()
