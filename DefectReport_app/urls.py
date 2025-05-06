from DefectReport_app import views
from django.urls import path

urlpatterns = [
    path('midline_defect/', views.midline, name='midline_defect'),
    path('add/', views.add, name="add"),
    path("addnow/", views.addnow, name="addnow"),
    path('midline_defect/export/', views.export_midline_defect_excel, name='midline_defect_export'),
    path('update/<int:id>/', views.update, name='update_defect'),
    path('delete/<int:id>/', views.delete, name='delete_defect'),
]
