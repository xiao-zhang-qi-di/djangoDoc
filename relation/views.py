from django import http
from django.shortcuts import render
from . models import *
import datetime
# Create your views here.

def tes(request):

    grp = Group.objects.get(name='The Beatles')
    per = Person.objects.get(name='Paul')
    obj = Membership.objects.get(person=per, group=grp)
    return http.JsonResponse({'name': obj.invite_reason})

    # objs = Membership.objects.filter(group__name="The Beatles")
    # person_list = []
    # for obj in objs:
    #     person_list.append(obj.person.name)
    # return http.JsonResponse({'person_list': person_list})

    # objs = Membership.objects.filter(group_id=1)
    # invite_reason_list = []
    # for obj in objs:
    #     invite_reason_list.append(obj.invite_reason)
    # return http.JsonResponse({'invite_reason_list': invite_reason_list})


    # obj = Person.objects.filter(group__name='The Beatles', membership__date_joined__gt=datetime.date(1993, 12, 12))
    # print(obj)
    # name_list = []
    # for i in obj:
    #     name_list.append(i.name)
    # print(name_list)
    # return http.JsonResponse({'name_list':name_list})

