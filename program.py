"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif ((month == 2) and ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))):
        return 29
    else:
        return 28
 
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if ((year < datetime.MINYEAR) or (year > datetime.MAXYEAR)):
        return False
    elif ((month < 1) or (month > 12)) or ((day < 1) or (day > days_in_month(year, month))):
        return False
    else:
        return True
   
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """    
    if ((is_valid_date(year1, month1, day1)) is False):
        return 0
    elif ((is_valid_date(year2, month2, day2)) is False):
        return 0
    elif ((datetime.date(year1, month1, day1)) > (datetime.date(year2, month2, day2))):
        return 0
    else:
        return ((datetime.date(year2, month2, day2)) - (datetime.date(year1, month1, day1))).days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if ((is_valid_date(year, month, day)) is False):
        return 0
    elif ((datetime.date(year, month, day)) > datetime.date.today()):
        return 0
    else:
        year1 = datetime.date.today().year
        month1 = datetime.date.today().month
        day1 = datetime.date.today().day
        
        return days_between(year, month, day, year1, month1, day1)