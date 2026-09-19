from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkerProfile, PreviousWork, SkillCategory
from customers.models import Booking, Review, CustomerProfile

@login_required
def worker_dashboard(request):
    profile = WorkerProfile.objects.get(user=request.user)
    previous_works = PreviousWork.objects.filter(worker=profile)
    reviews = Review.objects.filter(worker=profile)
    # all bookings related to worker
    bookings = Booking.objects.filter(worker=profile).select_related("customer").order_by('-booking_date')

    return render(request, 'workers/worker_dashboard.html', {
        'profile': profile,
        'previous_works': previous_works,
        'reviews': reviews,
        'bookings': bookings
    })


@login_required
def upload_previous_work(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        completed_on = request.POST['completed_on']

        profile = WorkerProfile.objects.get(user=request.user)
        PreviousWork.objects.create(
            worker=profile,
            title=title,
            description=description,
            image=image,
            completed_on=completed_on
        )

        # 👇 Add message here
        messages.success(request, "Previous work uploaded successfully!")

        return redirect('worker_dashboard')
    
    return render(request, 'workers/add_works.html')




@login_required
def create_or_update_profile(request):
    profile, created = WorkerProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.phone = request.POST['phone']
        profile.location = request.POST['location']
        profile.bio = request.POST.get('bio', '')
        profile.worker_type = request.POST['worker_type']

        if 'profile_photo' in request.FILES:
            profile.profile_photo = request.FILES['profile_photo']

        profile.save()
        return redirect('worker_dashboard')

    return render(request, 'workers/profile.html', {'profile': profile})


@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id, worker__user=request.user)
    if status in ["accepted", "ongoing", "underprocess", "completed"]:
        booking.status = status
        booking.save()
    return redirect('worker_dashboard')

@login_required
def view_customer_profile(request, customer_id):
    # Get the customer profile or return 404 if not found
    customer_profile = get_object_or_404(CustomerProfile, user__id=customer_id)

    return render(request, "workers/view_customer_profile.html", {
        "customer": customer_profile
    })
