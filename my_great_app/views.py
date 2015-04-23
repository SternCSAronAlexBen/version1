from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext, loader
from my_great_app.functions import bloomberg_stories
from my_great_app.functions import story
# Create your views here.
from .models import story


def index(request):
    return HttpResponse("Welcome! You will be miserable here!")


def index2(request):
    return HttpResponse("Welcome Ben!")


def get_news(request):
    '''
    latest_news = story.objects.order_by('headline')
    template = loader.get_template("my_beautiful_website/index.html")
    context = RequestContext(request, {
        'latest_news': latest_news
    })
    return HttpResponse(template.render(context))'''
    return render(request, 'my_beautiful_website/search_form.html')


def print_headlines(request):
    if 'q' in request.GET:
        message = 'Search Term %r' % request.GET['q'] + ' Entered'
        search_term = request.GET['q']
        stories = bloomberg_stories(search_term)
        headlines = {item.headline for item in stories}
        summaries = {item.story for item in stories}
        times = {item.time for item in stories}
        context = RequestContext(request, {
        'headlines': headlines,
        'summaries': summaries,
        'times': times,
        })
        template = loader.get_template('my_beautiful_website/test.html')

        new_message = template.render(context)

    else:
        new_message = 'You submitted an empty form.'

    return HttpResponse(new_message)

def print_news(request):
    if 'q' in request.GET:
        message = 'Search Term %r' % request.GET['q'] + ' Entered'
        search_term = request.GET['q']
        stories = bloomberg_stories(search_term)
        # message = message + str(stories[0].headline)


        template = loader.get_template('my_beautiful_website/test_two.html')
        my_news = {'summaries': item for item in stories}
        context = RequestContext(request, my_news)

        new_message = template.render(context)

    else:
        new_message = 'You submitted an empty form.'

    return HttpResponse(new_message)