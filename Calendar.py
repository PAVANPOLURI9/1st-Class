import calendar

def display_calendar(year, month):
    # Create a plain text calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Format the month and year
    cal_str = cal.formatmonth(year, month)
    print(cal_str)
