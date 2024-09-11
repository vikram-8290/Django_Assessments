from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    instance.username = 'updated_user'
    instance.save()
    print(f"Signal modified user in transaction: {transaction.get_autocommit()}")

def create_user():
    with transaction.atomic():
        user = User.objects.create(username="test_user")
        print(f"User created in transaction: {transaction.get_autocommit()}")
        raise Exception("Rolling back the transaction")

try:
    create_user()
except Exception as e:
    print("Transaction rolled back.")
