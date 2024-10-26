from django.shortcuts import render, get_object_or_404, redirect
from .models import Train, Reservation, Passenger
from django.contrib.auth.forms import UserCreationForm

def home(request):
    trains = Train.objects.all()
    return render(request, 'railway_reservation/home.html', {'trains': trains})

def train_detail(request, train_number):
    train = get_object_or_404(Train, train_number=train_number)
    return render(request, 'railway_reservation/train_detail.html', {'train': train})

def book_ticket(request, train_number):
    train = get_object_or_404(Train, train_number=train_number)
    
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        seat_number = request.POST['seat_number']
        
        passenger = Passenger.objects.create(name=name, age=age, gender=gender)
        reservation = Reservation.objects.create(train=train, passenger=passenger, seat_number=seat_number)
        
        return render(request, 'railway_reservation/confirmation.html', {'reservation': reservation})

    return render(request, 'railway_reservation/book_ticket.html', {'train': train})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def train_search(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    trains = Train.objects.filter(source=source, destination=destination)
    
    return render(request, 'railway_reservation/train_search_results.html', {'trains': trains, 'source': source, 'destination': destination, 'date': date})
