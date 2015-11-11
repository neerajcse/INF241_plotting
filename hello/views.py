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
    N = len( data )
    x = np.arange(1, N+1)
    y = [float(x) for x in request.GET.get('values').split(",")]
    labels = [ "Monday", "Tuesday", "Wednesday" ]
    width = 1
    bar1 = plt.bar( x, y, width, color="y" )
    plt.ylabel( 'Consumption' )
    plt.xticks(x + width/2.0, labels )
    
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

