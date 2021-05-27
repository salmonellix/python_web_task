from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django import template
from django.db.models import Count

register = template.Library()

# Create your views here.
def home(request):

    addresses = Addresses.objects.values('city','state').annotate(dcount=Count('city')).order_by('-dcount')
    states = Addresses.objects.values('state').annotate(dcount=Count('state')).order_by('state')

    # addresses = Addresses.objects.order_by('state')

    context = {'states':states, 'addresses':addresses}
    return render(request, 'main.html', context)


def list_details(request,state, city):

    addresses = Addresses.objects.values('city','state').annotate(dcount=Count('city')).order_by('-dcount')
    states = Addresses.objects.values('state').annotate(dcount=Count('state')).order_by('state')
    people = Addresses.objects.values('city','state','first_name','last_name','email').order_by('first_name').filter(state= state, city=city)

    context = {'states': states, 'addresses': addresses, 'people': people, 'state':state, 'city':city}
    return render(request, 'extended.html', context)



@register.filter
def in_category(addresses, state):

    return addresses.filter(state=state)


