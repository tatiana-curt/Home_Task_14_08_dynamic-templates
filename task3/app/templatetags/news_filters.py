from django import template
from datetime import datetime, timedelta
# import datetime

register = template.Library()


@register.filter
def format_date(value):
    data = datetime.fromtimestamp(value)
    past_10 = datetime.now() - timedelta(minutes=10)
    past_24_hours = datetime.now() - timedelta(hours=24)

    if data <= past_24_hours:
        newvalue = data.date().strftime("%Y-%m-%d")
    elif data > past_24_hours and data < past_10:
        hour = data.hour
        if hour == 0:
            minute = data.minute
            newvalue = f'{minute} минут назад'
        else:
            newvalue = f'{hour} часов назад'
    elif data >= past_10:
        newvalue = 'только что'

    return newvalue


@register.filter
def format_score(value):

    if value <= 5:
        value = 'Плохо'
    elif 5 < value < 10:
        value = 'Норм тема'
    elif value >= 10:
        value = 'Отлично'

    return value
#
@register.filter
def format_num_comments(value):

    if value == 0:
        value = 'Оставьте комментарий'
    elif value >= 50:
        value = '50+'
    return value


@register.filter
def sformat_elftext(value, count):

    value_list = value.split(' ')
    value = f'{" ".join(value_list[:count])} . . . . . {" ".join(value_list[-count:])}'

    return value


