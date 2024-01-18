from django.urls import path

from .views import index, chart1, chart2, chart3

urlpatterns = [
    path('', index, name='index'),
    path('chart/1/', chart1, name='chart1'),
    path('chart/2/', chart2, name='chart2'),
    path('chart/3/', chart3, name='chart3'),
]
