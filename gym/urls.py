from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('packages/', views.packages_list, name='packages'),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),
    path('packages/<int:pk>/book/', views.book_package, name='book_package'),
    path('trainers/', views.trainers_view, name='trainers'),
    path('equipment/', views.equipment_view, name='equipment'),
    path('contact/', views.contact_view, name='contact'),
    path('member/dashboard/', views.booking_history, name='member_dashboard'),
    path('member/bookings/', views.booking_history, name='booking_history'),
    path('member/bookings/<int:pk>/', views.booking_detail, name='booking_detail'),
]
