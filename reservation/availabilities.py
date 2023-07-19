from datetime import date
from reservation.models import Table, Booking



def check_availability(table, time, date):
    avail_list = []
    booking_list = Booking.objects.filter(table=table)
    
    for booking in booking_list:
        if booking.time > time or booking.time < time:
            
            avail_list.append(True)
            
        else:
            avail_list.append(False)

        
    return all(avail_list)
    
    ##today = date.today()
####d2= today.strftime("%B %d, %Y")
###date=d2