from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class CollectionPoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(default='flo@gmail.com')
    operating_hours = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    accepts_electronics = models.BooleanField(default=True)
    accepts_batteries = models.BooleanField(default=True)
    accepts_lamps = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CollectionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_point = models.ForeignKey(CollectionPoint, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    collection_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"Request #{self.id} - {self.user.username}"

class Payment(models.Model):
    request = models.OneToOneField(CollectionRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Request #{self.request.id}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
