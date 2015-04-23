from django.conf.urls import include, url
from django.contrib import admin
from my_great_app import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'my_beautiful_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^my_great_app/',include('my_great_app.urls',namespace='my_great_app')),
    url(r'^search/',views.print_headlines,name="print_headlines"),
    url(r'^admin/', include(admin.site.urls)),
]
#in general: plug in url here
#function goes in views
#