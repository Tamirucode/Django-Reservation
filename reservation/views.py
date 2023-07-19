from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, View, DeleteView
from .models import Table, Booking
from django.urls import (get_resolver, get_urlconf, resolve, reverse_lazy,
                         reverse, NoReverseMatch)
from django.core.exceptions import ImproperlyConfigured
from .forms import AvailabilityForm
from reservation.availabilities import check_availability


def TableListView(request):
    table = Table.objects.all()[0]
    table_categories = dict(table.TABLE_CATEGORIES)
    #print('categories', table_categories)
    table_values = table_categories.values()
    
    #print('categories', table_values)
    table_list =[]

    for table_category in table_categories:
        table = table_categories.get(table_category)
        table_url = reverse('reservation:TableDetailView', kwargs={
                           'category': table_category,

                           })
        #print(table_url)
        table_list.append((table, table_url))
        context = {
            "table_list": table_list,
        }
        #print(table_list)
    return render(request, 'table_list_view.html', context)





class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        table_list = Table.objects.filter(category=category)
        form = AvailabilityForm()
        
        if len(table_list)>0 :
            table = table_list[0]
            table_category=dict(table.TABLE_CATEGORIES).get(table.category,None)
            
            context={
                'table_category':table_category,
                'form':form,
                 }
            
            return render(request, 'table_detail_view.html', context)
        else:
            
            return HttpResponse('category doesnot exist')
        
  
    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        
        table_list = Table.objects.filter(category=category)
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

        available_tables = []
        for table in table_list:
            data = form.cleaned_data
            if check_availability(table, data['time'], data['date']):
                available_tables.append(table)

        
            if len(available_tables)>0:
                table = available_tables[0]
                booking = Booking.objects.create(
                    user=self.request.user,
                    table=table,
                    time=data['time'],
                    date=data['date']
            )
                booking.save()
                return HttpResponse(booking)
            else:
                return HttpResponse("all categories of table are booked, attempt another one")


class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class BookingCancelView(DeleteView):
    
    model = Booking
    template_name ="booking_cancel_view.html"
    #success url mean here url to redirect  after  successfully deleting object
    success_url = reverse_lazy('reservation:BookingListView')

