# Generated by Django 3.1.5 on 2021-01-26 08:17

from django.db import migrations, models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.management import create_permissions

ADMIN_PERMS = [
    "change_organization",
    "view_organization",
    "add_user",
    "change_user",
    "delete_user",
    "view_user"
]

VIEWER_PERMS = [
    "view_organization",
    "view_user"
]

USER_PERMS = [
    "add_organization",
    "view_organization",
    "change_user",
    "view_user"
]


def create_group_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    # Administrator group
    group, created = Group.objects.get_or_create(name='Administrator')
    if created:
        permissions_qs = Permission.objects.filter(
            codename__in=ADMIN_PERMS
        )
        group.permissions.set(permissions_qs)
        group.save()

    # Viewer group
    group, created = Group.objects.get_or_create(name='Viewer')
    if created:
        permissions_qs = Permission.objects.filter(
            codename__in=VIEWER_PERMS
        )
        group.permissions.set(permissions_qs)
        group.save()

    # User group
    group, created = Group.objects.get_or_create(name='User')
    if created:
        permissions_qs = Permission.objects.filter(
            codename__in=USER_PERMS
        )
        group.permissions.set(permissions_qs)
        group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_group_permissions),
    ]
