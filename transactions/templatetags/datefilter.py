from django import template
from datetime import datetime
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