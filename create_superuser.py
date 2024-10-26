# from django.contrib.auth import get_user_model

# User = get_user_model()
# username = "sujit.pashine"
# email = "sujit.pashine@gmail.com"
# password = "sujit.pashine"

# if not User.objects.filter(username=username).exists():
#     User.objects.create_superuser(username=username, email=email, password=password)
#     print("Superuser created successfully!")
# else:
#     print("Superuser already exists.")

from django.contrib.auth.models import User
user = User.objects.get(username="sujit.pashine")
user.set_password("sujit.pashine")
user.save()