from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Index"),
    path('<str:link>', views.short_link, name='short_link')
]