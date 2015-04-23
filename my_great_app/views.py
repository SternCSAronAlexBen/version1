from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext, loader
from my_great_app.functions import bloomberg_stories

from my_great_app.functions import story_nomodel
# Create your views here.
from .models import story

def get_news(request):

    return render(request, 'my_beautiful_website/search_form.html')

def print_news(request):
    if 'q' in request.GET:

        search_term = request.GET['q']
        stories = bloomberg_stories(search_term)

        template = loader.get_template('my_beautiful_website/news_stories.html')
        my_news = {'summaries': [item for item in stories]}
        context = RequestContext(request, my_news)

        new_message = template.render(context)

    else:
        new_message = 'You submitted an empty form.'

    return HttpResponse(new_message)