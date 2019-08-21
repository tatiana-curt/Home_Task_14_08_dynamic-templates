from django import template

register = template.Library()

@register.filter
def stylize(value, row):
    if value:
        index = row.index(value)
        val = float(value)

        if index == len(row) - 1:
            return '#acacac'
        elif index != 0 and index != 13:
            if val <0:
                return '#bef2bc'
            elif 2 >= val > 1:
                return '#ffdfd4'
            elif 5 >= val > 2:
                return '#ff9e81'
            elif val > 5:
                return '#ff5232'

