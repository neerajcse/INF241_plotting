from pylab import figure, axes, pie, title
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test_matplotlib(request):
    f = figure(figsize=(6,6))
    radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
    matplotlib.pyplot.plot(radius, area)
    title('Weekly Overview', bbox={'facecolor':'0.8', 'pad':5})
    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    matplotlib.pyplot.close(f)
    return response

	
def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

