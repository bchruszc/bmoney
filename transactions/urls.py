from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^files/', views.files, name='files'),
    url('', views.transaction_list, name='transaction_list'),
]