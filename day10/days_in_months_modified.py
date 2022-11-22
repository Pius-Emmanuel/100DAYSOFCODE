"""
First, convert this function is_leap() so that instead of printing
'Leap year.' or 'Not leap year.' it should return True if it is a
leap year and return False if it is not a leap year.You are then going
to create a function called days_in_month() which will take a year and
a month as inputs, And it will use this information to work out the number
of days in the month, then return that as the output
"""


def is_leap(year):
    """_summary_

    Args:
        year (int): takes year as an argument
    Returns:
        Bool: If it's a leap year it returns True else False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Function to calculate days in month
def days_in_month(year, month):
    """_summary_

    Args:
        year (int): takes year as argument
        month (int): takes month as argument
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

choose_year = int(input("Enter a year: "))
choose_month = int(input("Enter a month: "))
days = days_in_month(choose_year, choose_month)
print(days)
    