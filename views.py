from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import View
from my_lab5.data import figures, figures_dict


class FiguresView(View):
    def get(self, request):
        return render(request, 'main_page.html', {'figures': figures})


class FigureView(View):
    def get(self, request, id):
        figure = figures_dict.get(int(id))
        return render(request, 'figure.html', {'figure': figure})
