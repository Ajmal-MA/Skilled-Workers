from django.contrib import admin
from .models import Booking, Review

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'worker', 'service_type', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'customer', 'worker', 'rating')
    list_filter = ('rating',)
