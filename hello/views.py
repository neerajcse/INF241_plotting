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
    y = [float(x) for x in request.GET.get('values').split(",")]
    date = plt.figure()
    N = len( y )
    x = np.arange(1, N+1)
    rotation = datetime.datetime.today().weekday()
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
    labels = days[-rotation:] + days[:-rotation] 
    width = 0.5
    bar1 = plt.bar( x, y, width, color="y" )
    plt.ylabel( 'Consumption' )
    plt.xticks(x + width/2.0, labels )
    
    canvas = FigureCanvasAgg(date)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(date)
    return response

	
def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

