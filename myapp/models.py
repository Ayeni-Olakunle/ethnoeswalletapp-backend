from django.db import models

# Create your models here.
class Transaction(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name