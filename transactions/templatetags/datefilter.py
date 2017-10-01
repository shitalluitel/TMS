from django import template
from datetime import datetime
import datetime

# import calendar

register = template.Library()


@register.filter
def datefilter(value):
    today_date = datetime.datetime.today()
    date = int(value)
    print("Date: %s" % (date))
    date_cal = datetime.timedelta((today_date.year, today_date.month) - date)
    return (today_date - date_cal).strftime('%Y-%m-%d')