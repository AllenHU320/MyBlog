from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.get_blogs,name='get_blogs'),
    url(r'^detail/(\d+)/$',views.get_details ,name='get_details'),
]