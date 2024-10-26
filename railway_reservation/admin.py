# railway_reservation/admin.py
from django.contrib import admin
from .models import Train, Reservation, Passenger

admin.site.register(Train)
admin.site.register(Reservation)
admin.site.register(Passenger)


# Register your models here.
