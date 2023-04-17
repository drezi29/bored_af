from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import InputForm

def activity(request):
    context ={}
    context['form']= InputForm()
    return render(request, 'activity_generator/activity.html', context)

def get_activity(request):
    activity_type = request.GET.get('activity_type')
    participants = request.GET.get('participants')
    response = requests.get('http://www.boredapi.com/api/activity/', data={'key': 'value'}).json()
    activity_name = response['activity']
    link = response['link']
    return render(request, 'activity_generator/result_activity.html', {'activity_name': activity_name, 'link': link, 'activity_type': activity_type, 'participants' : participants})
