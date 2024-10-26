from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='default_group')
        instance.groups.add(group)
