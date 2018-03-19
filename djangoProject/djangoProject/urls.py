"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import tamilmatrimony
from tamilmatrimony import views as matrimonyviews
from django.core.urlresolvers import reverse


urlpatterns = [
    # url(r'^$', reverse(views.profile_list, name='list'),
    url(r'^$', matrimonyviews.profile_list, name='list'),
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('tamilmatrimony.urls',namespace='profiles')),
    url(r'^register/', matrimonyviews.register, name="register"),
    url(r'^login/',matrimonyviews.login_user,name= "login"),
    url(r'^logout/',matrimonyviews.logout_view,name= "logout"),
    url(r'^api/v1/',include('tamilmatrimony.v1.tamilmatrimony_api_urls',namespace= "tamilmatrimony-api"))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)