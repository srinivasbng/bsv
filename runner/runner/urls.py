from django.conf.urls import include, url
from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Examples:
    # url(r'^$', 'runner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myapp.urls')),
    url(r'^$',include('myapp.urls')),
    #path('admin/', admin.site.urls),

]
