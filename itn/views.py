from django.shortcuts import render
from .utils import Calendar
from django.http import JsonResponse, HttpResponse, Http404

from django.conf import settings
from datetime import datetime, date, timedelta, time
from django.utils.safestring import mark_safe
from django.core import serializers

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone

import calendar
import pytz

from .forms import DayForm, NightForm, UploadFileForm
from .models import DayEvent, NightEvent, UploadFile

import os

nz_tz = pytz.timezone('Pacific/Auckland')

# Create your views here.
def main(request):
    d = get_date(request.GET.get('month', None))
    # d = d.replace(tzinfo=nz_tz)
    cal = Calendar(d.year, d.month)
    week = cal.formatmonth(withyear=True)

    tday = datetime.today().replace(tzinfo=nz_tz)
    year = str(d.year)
    month = str(d.strftime('%B'))
    
    context = { 
        'today': tday,
        'title': month + ' ' + year,
        'monthSet': d.month,
        'yearSet': d.year,
        'week': week,
        'prev_month': prev_month(d),
        'next_month': next_month(d),
        }
        
    return render(request, 'itn/main.html', context)

def get_date(req_day):
    if req_day:
        year, month, day = (int(x) for x in req_day.split('-'))
        if day == 0:
            return datetime.today()
        else:
            return date(year, month, day)
    return datetime.today()


def prev_month(d):
    previous_month = date(year=d.year, month=d.month, day=1) 
    previous_month = previous_month - timedelta(days=1)
    previous_month = date(year=previous_month.year, month=previous_month.month, day=1)
    return str(previous_month)

def next_month(d):
    last_day = calendar.monthrange(d.year, d.month)
    next_month = date(year=d.year, month=d.month, day=last_day[1])
    next_month = next_month + timedelta(days=1)
    next_month = date(year=next_month.year, month=next_month.month, day=1)
    return str(next_month)

@login_required(login_url='accounts:login_required')
def groups(request):
    if request.is_ajax and request.method == 'GET':
        date = request.GET['date']
        date_nz = get_date(date)

        daystart = timezone.make_aware(datetime.combine(date_nz, time(hour=5, minute=59, second=59)))
        dayend = timezone.make_aware(datetime.combine(date_nz + timedelta(days=1), time(hour=6, minute=0, second=0)))

        day_nums = DayEvent.objects.filter(create_date__range=[daystart, dayend]).values('group').annotate(nums_group=Count('group'))
        night_nums = NightEvent.objects.filter(create_date__range=[daystart, dayend]).values('group').annotate(nums_group=Count('group'))

        context = {'date': date, 'date_nz': date_nz, 'day_nums': day_nums, 'night_nums': night_nums}
        return render(request, 'itn/groups.html', context)  
    else:
        return JsonResponse({'error': 'itn groups error'}, status=400)

@login_required(login_url='accounts:login_required')
def forms(request):
    if request.is_ajax and request.method == 'GET':
        date_nz = get_date(request.GET['date'])
        
        daystart = timezone.make_aware(datetime.combine(date_nz, time(hour=5, minute=59, second=59)))
        dayend = timezone.make_aware(datetime.combine(date_nz + timedelta(days=1), time(hour=6, minute=0, second=0)))

        group_selected = request.GET['group']
        group_title = group_selected.replace('_', ' ').title()
        
        day_event = DayEvent.objects.filter(create_date__range=[daystart, dayend], group=group_selected).order_by('-edit_date').first()
        night_event = NightEvent.objects.filter(create_date__range=[daystart, dayend], group=group_selected).order_by('-edit_date').first()

        if daystart <= datetime.today().replace(tzinfo=nz_tz) and dayend >= datetime.today().replace(tzinfo=nz_tz):
            dayForm = DayForm(instance=day_event)
            nightForm = NightForm(instance=night_event)
            context = {'isToday': True, 'dayForm': dayForm, 'nightForm': nightForm, 'group_selected': group_selected, 'group_title': group_title, 'dayEvent': day_event, 'nightEvent': night_event}
            return render(request, 'itn/forms.html', context)
        else:
            context = {'isToday': False, 'dayEvent': day_event, 'nightEvent': night_event, 'group_title': group_title}
            return render(request, 'itn/forms.html', context)
    else:
        return JsonResponse({'error': 'itn forms error'}, status=400)

@login_required(login_url='accounts:login_required')
def post(request):
    if request.is_ajax and request.method == 'POST':
        
        if request.POST['formType'] == 'day':
            print(request.POST)
            form = DayForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.signed_by = request.user
                instance.group = request.POST['group']
                instance.save()

        if  request.POST['formType'] == 'night':
            form = NightForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.signed_by = request.user
                instance.group = request.POST['group']
                instance.save()

        context = {'message': 'The form has been entered.'}
        return JsonResponse({'instance': 'itn forms success'}, status=200)

@login_required(login_url='accounts:login_required')
def uploads(request):
    if request.is_ajax and request.method == 'GET':
        print('ajax files GET request')
        group_selected = request.GET['group']
        date_nz = get_date(request.GET['date'])

        daystart = timezone.make_aware(datetime.combine(date_nz, time(hour=5, minute=59, second=59)))
        dayend = timezone.make_aware(datetime.combine(date_nz + timedelta(days=1), time(hour=6, minute=0, second=0)))

        files = UploadFile.objects.filter(create_date__range=[daystart, dayend], group=group_selected).order_by('-create_date')

        form = UploadFileForm()
        if daystart <= datetime.today().replace(tzinfo=nz_tz) and dayend >= datetime.today().replace(tzinfo=nz_tz):
            return render(request, 'itn/uploads.html', {'form': form, 'files': files, 'isToday': True, 'group_selected': group_selected})
        else:
           return render(request, 'itn/uploads.html', {'files': files, 'isToday': False})

    elif request.is_ajax and request.method == 'POST':
        print('ajax image POST request')
        group_selected = request.POST['group']
        date_nz = datetime.today()
        form = UploadFileForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.signed_by = request.user
            instance.group = group_selected
            instance.save()

        files = UploadFile.objects.filter(create_date__date=date_nz, group=group_selected).order_by('-create_date')

        return render(request, 'itn/uploads.html', {'form': form, 'files': files, 'isToday': True})
    else:
        return JsonResponse({'error': 'itn image error'}, status=400)

@login_required(login_url='accounts:login_required')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

