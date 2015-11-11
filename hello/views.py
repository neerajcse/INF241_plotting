from django.shortcuts import render
from django.http import HttpResponse

# plotting library imports
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt

# scientific library imports
import numpy as np

# system imports
import datetime

# project imports
from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test_matplotlib(request):
    date = plt.figure()
    x = [datetime.datetime(2010, 12, 1, 10, 0),
         datetime.datetime(2011, 1, 4, 9, 0),
         datetime.datetime(2011, 5, 5, 9, 0)]
    y = [float(x) for x in request.GET.get('values').split(",")]
    ax = plt.subplot(111)
    ax.bar(x, y, width=10)
    ax.xaxis_date()
    canvas = FigureCanvasAgg(date)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    matplotlib.pyplot.close(f)
    return response

	
def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

