import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received. Sleeping for 5 seconds...")
    time.sleep(5)  # Simulates a long-running process
    print("Signal processing done.")

# Create a user to trigger the signal
user = User.objects.create(username="test_user")
print("User created.")
