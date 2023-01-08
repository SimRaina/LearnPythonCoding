
def is_leap(year):
    """ Returns if year is leap or not  """
    return year%4 == 0 and (year%100 !=0 or year%400==0)

test_cases=[2004, 2009, 1900, 1800, 1700]
for i in test_cases:
    # print('{} '.format(i), is_leap(i))
    if(is_leap(i)):
        print('{} is leap year'.format(i))
    else:
        print('{} is not a leap year'.format(i))
