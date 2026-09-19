from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile
from django.contrib import messages
from .forms import CustomerProfileForm
from.models import Booking,Review
from workers.models import WorkerProfile



@login_required
def customer_dashboard(request):
    # Ensure customer has profile
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('customer_dashboard')
    else:
        form = CustomerProfileForm(instance=profile)

    # Get worker list
    workers = WorkerProfile.objects.all()
    bookings = Booking.objects.filter(customer=request.user)

    return render(request, 'customers/customers_dashboard.html', {
        'form': form,
        'profile': profile,
        'workers': workers,
        'bookings': bookings,
    })
@login_required
def update_customer_info(request):
    customer = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('customer_dashboard')
    else:
        form = CustomerProfileForm(instance=customer)
    return render(request, 'customer_dashboard.html', {'form': form, 'customer': customer})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    booking.delete()
    return redirect('customer_dashboard')

@login_required
def browse_workers(request):
    workers = WorkerProfile.objects.all()
    return render(request,'customers/browse_worker.html',{'workers':workers})

@login_required
def book_worker(request,worker_id):
    worker = get_object_or_404(WorkerProfile, id=worker_id)

    if request.method == 'POST':
        service_type = request.POST['service_type']
        description = request.POST['description']
        location = request.POST['location']
        booking_date = request.POST['booking_date']

        Booking.objects.create(customer=request.user,worker=worker,service_type = service_type,description = description,location = location, booking_date = booking_date)
        return redirect('customer_dashboard')
    return render(request,'customers/book_worker.html',{'worker':worker})

@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']

        # prevent duplicate reviews
        if Review.objects.filter(booking=booking).exists():
            return redirect('customer_dashboard')

        Review.objects.create(
            booking=booking,
            customer=request.user,
            worker=booking.worker,
            rating=rating,
            comment=comment
        )
        return redirect('customer_dashboard')

    return render(request, 'customers/add_review.html', {'booking': booking})
