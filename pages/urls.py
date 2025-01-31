from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('abouts/<str:get_about>/', views.about_team, name='about_team'),
    path('about', views.about, name='about'),
    path('service-details', views.service_details, name='service_details'),
    path('services', views.services, name='services'),
    path('blog-details', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('portfolio', views.portfolio, name='portfolio'),
]
