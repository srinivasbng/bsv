from django.conf.urls import include, url
from django.contrib import admin
from myapp import views
#from django.urls import path


urlpatterns = [
    # Examples:
    # url(r'^$', 'runner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.index,name='index'),
    url('show', views.show),
    url('index', views.index),
    #path('admin/', admin.site.urls),
    #path('index/', views.index),

]