from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one),
    path('two/', views.two),
    path('num/pull/', views.workshop2),
    path('num/push/', views.workshop),
    path('static_example2/', views.static_example2),
    path('static_example/', views.static_example),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('result/', views.result),
    path('search/', views.search),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('student/<str:name>/<int:age>/', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]
