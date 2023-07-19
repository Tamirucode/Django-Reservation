from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

class Table(models.Model):
    
    TABLE_CATEGORIES = [
        ('A', 'Table for 3 people'),
        ('B', 'Table for 4 people'),
        ('C', 'Table for 6 people'),
        ('D', 'Table for 5 people'),
        ('E', 'Table for 2 people'),
        ('F', 'Table for 4 people'),
        ('G', 'Table for 6 people'),
        
    ]
    number = models.IntegerField(default=0)
    category = models.CharField(max_length=1, choices=TABLE_CATEGORIES)
    seats = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.number}. Table for {self.seats} people'   
    

class Booking(models.Model):  
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    
    time = models.TimeField()
    date = models.DateField()
    
    def __str__(self):
        return f'{self.user} booked {self.table}  Date {self.date} Time {self.time}'


def get_table_category(self):
    table_categories = dict(self.table.TABLE_CATEGORIES)
    table_category = table_categories.get(self.table.category)
    return table_category


def get_cancel_booking_url(self):
    return reverse_lazy('reservation:BookingCancelView', args=[self.pk, ])


