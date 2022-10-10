from django import template

register = template.Library()

def date_format(date):
    return  date.strftime(r'%Y-%m-%d-%H-%M-%S')


register.filter("date_format", date_format)