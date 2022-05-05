from django import template
from posts.models import *
from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag(name='getusers')
def get_users(filter=None):
    return User_people.objects.all()


# @register.simple_tag(name='getboxing')
# def get_boxing(filter=None):
#     if not filter:
#         return Boxing.objects.all()
#     else:
#         return Boxing.objects.filter(pk=filter)

# @register.simple_tag(name='getwrestling')
# def get_wrestling(filter=None):
#     if not filter:
#         return Wrestling.objects.all()
#     else:
#         return Wrestling.objects.filter(pk=filter)

@register.simple_tag(name='getathletics')
def get_athletics(filter=None):
    if not filter:
        return Athletics.objects.all()
    else:
        return Athletics.objects.filter(pk=filter)

@register.simple_tag(name='getweightlifting')
def get_weightlifting(filter=None):
    if not filter:
        return Weightlifting.objects.all()
    else:
        return Weightlifting.objects.filter(pk=filter)

@register.simple_tag(name='getcycling')
def get_cycling(filter=None):
    if not filter:
        return Cycling.objects.all()
    else:
        return Cycling.objects.filter(pk=filter)

@register.simple_tag(name='getteam_sports')
def get_team_sports(filter=None):
    if not filter:
        return Team_sports.objects.all()
    else:
        return Team_sports.objects.filter(pk=filter)


@register.inclusion_tag('lists/show_boxing.html')
def show_boxing():
    sportsmans = Boxing.objects.all()
    return {'posts': sportsmans}

@register.inclusion_tag('lists/show_wrestling.html')
def show_wrestling():
    sportsmans = Wrestling.objects.all()
    return {'posts': sportsmans}
