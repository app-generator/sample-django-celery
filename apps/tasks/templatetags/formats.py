from django import template

register = template.Library()

def date_format(date):
    try:
        return  date.strftime(r'%Y-%m-%d-%H-%M-%S')
    except:
        return date

register.filter("date_format", date_format)