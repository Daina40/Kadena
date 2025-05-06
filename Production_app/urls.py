from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('daily_input', views.InputListView.as_view(), name='daily_input'),
    path('export_excel/', views.export_excel, name='export_excel'), 
    path('production', views. ProductionListView.as_view(), name='production'),
    path('summary_production', views. SummaryProductionListView.as_view(), name='summary_production'),
]