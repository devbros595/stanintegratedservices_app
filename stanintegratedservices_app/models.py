from django.db import models

class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('Painting & Decorating', 'Painting & Decorating'),
        ('Wallpaper Installation', 'Wallpaper Installation'),
        ('General Cleaning', 'General Cleaning'),
        ('Gardening', 'Gardening'),
        ('Lawn Care', 'Lawn Care'),
        ('Weed Control', 'Weed Control'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"



