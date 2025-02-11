import os
import django
from django.contrib.auth import get_user_model

# Django-Umgebung laden
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "truck_signs_designs.settings")
django.setup()

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if not username or not email or not password:
    print("Superuser data is missing. Please check environment variables.")
    exit(1)

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Superuser already exists.")
