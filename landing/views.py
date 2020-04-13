import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max, Min
from django.views.decorators.csrf import csrf_exempt

from .models import PiData
from .models import Pi


def landing(request):
    context = {
        "pis": Pi.objects.all()
    }
    return render(request, 'landing/MainWebPage.html', context=context)


def login(request):
    return render(request, 'personal/home.html')


def data(request, pi_id):
    context = {"pi_id": pi_id}
    try:
        context["now"] = PiData.objects.filter(pi_id=pi_id).order_by("-time").first()
        min_time = datetime.datetime.now() - datetime.timedelta(days=1)
        last_24_hours = PiData.objects.filter(pi_id=pi_id, time__gte=min_time)
        context["dayHigh"] = last_24_hours.aggregate(Max('temperature'), Max('humidity'), Max('pressure'),
                                                     Max('wind_speed'))
        context["dayLow"] = last_24_hours.aggregate(Min('temperature'), Min('humidity'), Min('pressure'),
                                                    Min('wind_speed'))
        context["dayAvg"] = last_24_hours.aggregate(Avg('temperature'), Avg('humidity'), Avg('pressure'),
                                                    Avg('wind_speed'))
    except ObjectDoesNotExist:
        raise Http404("Ship not found")

    return render(request, "EnhancedData.html", context)


@csrf_exempt
def addDataPoint(request, pi_id):
    # Make sure the ID is in the database
    try:
        pi = Pi.objects.get(id=pi_id)
    except ObjectDoesNotExist:
        raise Http404

    r = json.loads(request.body.decode('utf-8'))

    data = PiData(pi_id=pi_id, time=datetime.datetime.now(), humidity=r["humidity"], temperature=r["ir_temp"],
                  wind_speed=0, pressure=r["pressure"])
    data.save()

    return HttpResponse(status=202)
