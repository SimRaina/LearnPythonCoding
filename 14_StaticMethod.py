class ReturnWorkday:

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime

my_date = datetime.date(2022, 6, 23)
print(ReturnWorkday.is_workday(my_date))
