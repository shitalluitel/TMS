import pytz
from django import template
import datetime
import dateutil.relativedelta
from datetime import date

register = template.Library()


@register.filter
def datefilter(value):
    today_date = date.today()
    if value > 0:
        return_date = today_date - dateutil.relativedelta.relativedelta(months=value)
        return str(return_date)
    return str(today_date)


@register.filter
def hour_limit(hour):
    timediff = datetime.datetime.now(pytz.utc) - hour
    c_time = timediff.total_seconds() / 3600
    if c_time <= 24:
        return True
    else:
        return False
