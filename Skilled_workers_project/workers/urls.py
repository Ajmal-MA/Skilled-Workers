from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_dashboard, name='worker_dashboard'),
    path('profile/', views.create_or_update_profile, name='create_or_update_profile'),
    path('add-work/', views.upload_previous_work, name='upload_previous_work'),
    path('update-booking/<int:booking_id>/<str:status>/', views.update_booking_status, name='update_booking_status'),
    path("customer/<int:customer_id>/", views.view_customer_profile, name="view_customer_profile"),

]
