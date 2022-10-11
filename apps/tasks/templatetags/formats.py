from django import template
import json

register = template.Library()

def date_format(date):
    try:
        return  date.strftime(r'%Y-%m-%d-%H-%M-%S')
    except:
        return date

register.filter("date_format", date_format)

def get_result_field(result,field:str):
    result = json.loads(result.result)
    if result:
        return result.get(field)
    

register.filter("get_result_field", get_result_field)
