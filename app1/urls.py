from django.urls import path
from django.contrib import admin
from .import views
admin.site.site_header = "SNVETECH"
admin.site.site_header = "Welcome to SNVETECH Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staffing/', views.staffing, name='staffing'),
    path('pharmastaffing/', views.pharmastaffing, name='pharmastaffing'),
    path('mobiledevelopment/',views.md,name='md'),
    path('webdevelopment/',views.web,name='web'),
    path('dm/',views.digital,name='digital'),
    path('architectures/',views.arch,name='arc'),
    path('careers/', views.careers, name='career'),
    path('contact/', views.contacts, name='contact'),
]

