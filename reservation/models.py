from django.db import models
from django.conf import settings


class Table(models.Model):
    
    TABLE_CATEGORY = [

        ('B', 'BAR'),
        ('D', 'DINING'),
    ]
    number = models.IntegerField(default=0)
    category = models.CharField(max_length=1, choices=TABLE_CATEGORY)
    seats = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Table{self.number}.inside {self.category} for {self.seats}  people'   
    

class Booking(models.Model):  
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    
    time = models.TimeField()
    date = models.DateField()
    
    def __str__(self):
        return f'{self.user} booked {self.table}  Date {self.date} Time {self.time}'



