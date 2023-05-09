# Generated by Django 4.2 on 2023-05-07 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('role', models.IntegerField(choices=[('ADMIN', 1), ('EMPLOYEE', 2)], default=2)),
                ('status', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('abn', models.CharField(blank=True, max_length=100, null=True)),
                ('bussiness_name', models.CharField(blank=True, max_length=64, null=True)),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('search_address', models.CharField(blank=True, max_length=500, null=True)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('bsb', models.CharField(blank=True, max_length=50, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('file_name', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='uploads/EmployeeDocuments')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_authentication.profile')),
            ],
        ),
    ]
