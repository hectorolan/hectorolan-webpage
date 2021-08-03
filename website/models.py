from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    """A topic the user is learning about."""
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    mesage = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text