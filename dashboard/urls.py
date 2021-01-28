from django.urls import path
from wkhtmltopdf.views import PDFTemplateView
from . import views
from rest_framework import routers

from .views import ConsumableViewSet

app_name = 'dashboard'

urlpatterns = [
    path('main/', views.DashboardMainView.as_view(), name='dashboard_main'),
    #path('monitor/', views.MachineMonitorView.as_view(), name='monitor'),
    path('monitor/', views.MachineMonitorView.as_view(), name='monitor'),
    path('graf/', views.get_svg, name='graf'),
    path('maintenance/list/', views.MaintenanceListView.as_view(), name='maintenance_list'),
    path('maintenance/create/', views.MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('maintenance/detail/<int:pk>/', views.MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('maintenance/update/<int:pk>/', views.MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('maintenance/delete/<int:pk>/', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('parts/', views.ElectricPartsView.as_view(), name='electric_parts'),
    path('alarm/', views.AlarmView.as_view(), name='alarm'),
    path('consumable_parts/', views.ConsumablePartsView.as_view(), name='consumable_parts'),
    path('report/', views.ReportView.as_view(), name='report'),
    #path('report/', PDFTemplateView.as_view(template_name='dashboard/report.html', filename='report.pdf'), name='report'),
]

router = routers.DefaultRouter()
router.register(r'consumable', ConsumableViewSet)