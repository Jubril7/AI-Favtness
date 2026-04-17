from django.contrib import admin
from django.utils.html import format_html
from .models import Category, PackageType, Trainer, Equipment, Package, UserProfile, Booking, ContactInquiry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)


@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience_years')
    search_fields = ('name', 'specialization')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'description')
    search_fields = ('name',)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'package_type', 'duration_months', 'price', 'is_active')
    list_filter = ('category', 'package_type', 'is_active')
    search_fields = ('name',)
    list_editable = ('is_active',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'user__email')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'start_date', 'end_date', 'total_amount', 'amount_paid', 'payment_status', 'booking_status', 'booked_at')
    list_filter = ('payment_status', 'booking_status', 'booked_at')
    search_fields = ('user__username', 'package__name')
    date_hierarchy = 'booked_at'
    readonly_fields = ('booked_at',)

    def get_balance(self, obj):
        return obj.balance
    get_balance.short_description = 'Balance'


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email')
    list_editable = ('is_read',)
    readonly_fields = ('submitted_at',)
