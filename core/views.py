from django.shortcuts import render

from .chart import MyBarGraph, Chart2, ChartLine

def index(request): return render(request, 'index.html')

def chart1(request):
    NewChart = MyBarGraph()
    NewChart.data.label = "My Favourite Numbers"      # can change data after creation

    ChartJSON = NewChart.get()
    return render(request=request, template_name='chart1.html', context={"chartJSON": ChartJSON})


def chart2(request):
    NewChart = Chart2()
    NewChart.data.label = "My Second Chart"      # can change data after creation

    ChartJSON = NewChart.get()
    return render(request=request, template_name='chart1.html', context={"chartJSON": ChartJSON})


def chart3(request):
    NewChart = ChartLine()
    ChartJSON = NewChart.get()
    return render(request=request, template_name='chart1.html', context={"chartJSON": ChartJSON})

