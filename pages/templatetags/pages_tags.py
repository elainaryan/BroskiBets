import datetime
from datetime import date
from django import template
from picks.models import DailyPicks

register = template.Library()


@register.simple_tag
def get_todays_picks():
    return DailyPicks.objects.order_by("-pub_date").first()

@register.simple_tag
def get_todays_pick_date():
    date_obj = DailyPicks.objects.order_by("-pub_date").first().pub_date
    return str(date_obj.month) + "/" + str(date_obj.day) + "/" + str(date_obj.year)

@register.simple_tag
def get_scotts_picks(daily_pick_object):
    if daily_pick_object == None:
        return None
    pick_set = daily_pick_object.scottpick_set.all()
    return pick_set

@register.simple_tag
def get_kanes_picks(daily_pick_object):
    if daily_pick_object == None:
        return None
    pick_set = daily_pick_object.kanepick_set.all()
    return pick_set

@register.simple_tag()
def determine_larger_table(daily_pick_object):
    if daily_pick_object == None:
        return True
    if daily_pick_object.scottpick_set.count() > daily_pick_object.kanepick_set.count():
        return False
    return True

@register.simple_tag()
def days_since_day_1():
    start_date = date(2021, 3, 6)
    todays_date = date.today()
    return (todays_date - start_date).days