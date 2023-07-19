from django.urls import path
from .views import TableListView, BookingListView, TableDetailView, BookingCancelView


app_name ='reservation'

urlpatterns = [
    
    path('', TableListView, name='TableListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    
    path('table/<category>', TableDetailView.as_view(), name='TableDetailView'),
    path('booking_cancel/<pk>', BookingCancelView.as_view(),
         name='BookingCancelView'),
]

