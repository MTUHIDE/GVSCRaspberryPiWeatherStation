import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.db.models import Avg, Max, Min

from .models import PiData
from .models import Pi


def landing(request):
    return render(request, 'landing/MainWebPage.html')


def login(request):
    return render(request, 'personal/home.html')


def data(request, pi_id):
    context = {}
    try:
        context["now"] = PiData.objects.filter(pi_id=pi_id).order_by("-time").first()
        min_time = datetime.datetime.now() - datetime.timedelta(days=1)
        last_24_hours = PiData.objects.filter(pi_id=pi_id, time__gte=min_time)
        context["dayHigh"] = last_24_hours.aggregate(Max('temperature'), Max('humidity'), Max('pressure'), Max('wind_speed'))
        context["dayLow"] = last_24_hours.aggregate(Min('temperature'), Min('humidity'), Min('pressure'), Min('wind_speed'))
        context["dayAvg"] = last_24_hours.aggregate(Avg('temperature'), Avg('humidity'), Avg('pressure'), Avg('wind_speed'))
    except ObjectDoesNotExist:
        raise Http404("Ship not found")

    print(context)

    return render(request, "EnhancedData.html", context)
