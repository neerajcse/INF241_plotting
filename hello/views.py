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
    values = [float(x) for x in request.GET.get('values').split(",")]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    f = figure(figsize=(6,6))
    matplotlib.pyplot.plot(np.array(values), np.array(days))
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

