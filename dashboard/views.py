import os

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from wkhtmltopdf.views import PDFTemplateView

from config import settings
from dashboard.models import MaintenanceModel
from django_xhtml2pdf.views import PdfMixin
import django_filters
from rest_framework import viewsets, filters

from .models import ConsumableModel
from .serializer import ConsumableSerializer

import logging
import pandas as pd
import pickle

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io




with open("tempml.pickle", mode="rb") as f:
    model = pickle.load(f)


class DashboardMainView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard_main.html'


class MachineMonitorView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/monitor.html'


class MaintenanceListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/maintenance_list.html'
    model = MaintenanceModel


class MaintenanceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/maintenance_detail.html'
    model = MaintenanceModel


class MaintenanceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/maintenance_update.html'
    model = MaintenanceModel
    fields = ('date', 'category', 'content', 'comment', 'author', 'images')
    success_url = reverse_lazy('dashboard:maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/maintenance_delete.html'
    model = MaintenanceModel
    success_url = reverse_lazy('dashboard:maintenance_list')


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/maintenance_create.html'
    model = MaintenanceModel
    fields = ('date', 'category', 'content', 'comment', 'author', 'images')
    success_url = reverse_lazy('dashboard:maintenance_list')

class ElectricPartsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/electric_parts.html'


class AlarmView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/alarm.html'



class ReportView(PdfMixin, TemplateView):
   template_name = 'home.html'


#グラフ作成
def setPlt():
    model = ConsumableModel.objects.all()
    print(model)
    print("ggggggg")
    x = [data.datetime for data in model]
        #data.datetime for data in model]
    y = [data.elapsed_days for data in model]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    model_result = model.predict([[2686, 2592, 2629, 2610, 2610, 2643, 2710, 2685, 2697, 2701]])
    html_model_result = "<p>" + str(model_result) + "</p>"
    response = HttpResponse(svg, content_type='image/svg+xml')
    #response = HttpResponse(html_model_result)
    return response

# Webapi
#class ConsumableFilter(django_filters.FilterSet):
#    class Meta:
#        model = ConsumableModel
#        fields = {'date': ['gte', ], }


class ConsumableViewSet(viewsets.ModelViewSet):
    queryset = ConsumableModel.objects.all()#.order_by("time")
    serializer_class = ConsumableSerializer
#    filter_class = ConsumableFilter

#    authentication_classes = (SessionAuthentication, BasicAuthentication)
#    permission_classes = (IsAuthenticated)

class ConsumablePartsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/consumable_parts.html'


