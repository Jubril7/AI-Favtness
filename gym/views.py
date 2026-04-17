from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date, timedelta
from .models import Package, Category, PackageType, Trainer, Equipment, Booking, ContactInquiry


def home(request):
    packages = Package.objects.filter(is_active=True).select_related('category', 'package_type')[:6]
    trainers = Trainer.objects.all()[:4]
    equipment = Equipment.objects.all()[:6]
    return render(request, 'gym/home.html', {
        'packages': packages,
        'trainers': trainers,
        'equipment': equipment,
    })


def packages_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    packages = Package.objects.filter(is_active=True).select_related('category', 'package_type')
    if selected_category:
        packages = packages.filter(category__id=selected_category)
    return render(request, 'gym/packages.html', {
        'packages': packages,
        'categories': categories,
        'selected_category': selected_category,
    })


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk, is_active=True)
    return render(request, 'gym/package_detail.html', {'package': package})


def trainers_view(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym/trainers.html', {'trainers': trainers})


def equipment_view(request):
    equipment = Equipment.objects.all()
    return render(request, 'gym/equipment.html', {'equipment': equipment})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactInquiry.objects.create(name=name, email=email, phone=phone, message=message)
            messages.success(request, 'Your inquiry has been submitted. We will contact you soon!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    return render(request, 'gym/contact.html')


@login_required
def book_package(request, pk):
    package = get_object_or_404(Package, pk=pk, is_active=True)
    if request.method == 'POST':
        start_date = date.today()
        end_date = start_date + timedelta(days=30 * package.duration_months)
        booking = Booking.objects.create(
            user=request.user,
            package=package,
            start_date=start_date,
            end_date=end_date,
            total_amount=package.price,
            amount_paid=0,
            payment_status='pending',
        )
        messages.success(request, f'Successfully booked {package.name}! Please complete your payment.')
        return redirect('booking_detail', pk=booking.pk)
    return render(request, 'gym/book_confirm.html', {'package': package})


@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'gym/booking_detail.html', {'booking': booking})


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).select_related('package').order_by('-booked_at')
    return render(request, 'gym/booking_history.html', {'bookings': bookings})
