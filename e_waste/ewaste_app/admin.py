from django.contrib import admin
from .models import CollectionPoint, CollectionRequest, Payment, Notification

@admin.register(CollectionPoint)
class CollectionPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email')
    search_fields = ('name', 'address')
    list_filter = ('accepts_electronics', 'accepts_batteries', 'accepts_lamps')

@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'collection_point', 'status', 'collection_date')
    list_filter = ('status', 'collection_point')
    search_fields = ('user__username', 'collection_point__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('request', 'amount', 'is_paid', 'payment_date')
    list_filter = ('is_paid',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('user__username', 'message')
