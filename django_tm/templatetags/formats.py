from django import template
import json

register = template.Library()


def date_format(date):
    """
    Returns a formatted date string
    Format:  `Year-Month-Day-Hour-Minute-Second`
    Example: `2022-10-10-00-20-33`
    :param date datetime: Date object to be formatted
    :rtype: str
    """
    try:
        return date.strftime(r'%Y-%m-%d-%H-%M-%S')
    except:
        return date


register.filter("date_format", date_format)


def get_result_field(result, field: str):
    """
    Returns a field from the content of the result attibute in result 
    Example: `result.result['field']`
    :param result AbortableAsyncResult: Result object to get field from
    :param field str: Field to return from result object
    :rtype: str
    """
    result = json.loads(result.result)
    if result:
        return result.get(field)


register.filter("get_result_field", get_result_field)
