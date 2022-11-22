"""
days in months modified
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
    
    year = int(input("Enter a year"))
    month = int(input("Enter a month"))
    days = days_in_month(year, month)
    print(days)