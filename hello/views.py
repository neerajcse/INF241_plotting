from pylab import figure, axes, pie, title
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
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
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

