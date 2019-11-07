from django.conf.urls import url
from .views import MyFileView

urlpatterns = [
  	url(r'^$', MyFileView.as_view(), name='file-upload'),
]