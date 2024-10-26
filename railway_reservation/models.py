from django.db import models

class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.train_number})"

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.name

class Reservation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Reservation {self.id} for {self.passenger.name}"
