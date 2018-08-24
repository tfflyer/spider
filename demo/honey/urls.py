from django.urls import path
from . import views

app_name = 'honey'
urlpatterns = [

    path('honey/', views.index, name='honey_page'),

]
