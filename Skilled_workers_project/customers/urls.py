from django.urls import path
from . import views



urlpatterns = [
    path('',views.customer_dashboard,name='customer_dashboard'),
    path('update-info/', views.update_customer_info, name='update_customer_info'),
    path("delete-booking/<int:booking_id>/", views.delete_booking, name="delete_booking"),
    path('bookworker/<int:worker_id>/', views.book_worker, name='book_worker'),
    path('browse_workers/',views.browse_workers,name='browse_workers'),
    path('add_review/<int:booking_id>/', views.add_review, name='add_review'),


]