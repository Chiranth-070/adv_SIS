import datetime


def get_month_shortform(month_number):
    # Dictionary mapping month numbers to their short forms
    month_shortforms = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    return month_shortforms.get(month_number)


def getpass(date: datetime.date):
    day = str(date.day)
    if len(day) == 1:
        day = '0' + day
    month = get_month_shortform(date.month)
    year = str(date.year)

    return day,month,year
