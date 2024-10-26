from django.contrib.auth.models import Group

def add_user_to_default_group(user):
    group, created = Group.objects.get_or_create(name='default_group')
    user.groups.add(group)
