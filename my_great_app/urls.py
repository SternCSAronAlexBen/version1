__author__ = 'ben'
#copied this over from my_beautiful_website urls.py
from django.conf.urls import include, url
from my_great_app import views
#changed utl pattern below and import statement above
#then modify views.py
urlpatterns = [
    # Examples:
    # url(r'^$', 'my_beautiful_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'news',views.get_news,name="get_news"),

]
