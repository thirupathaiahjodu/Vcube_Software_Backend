# Generated by Django 5.0.6 on 2024-10-06 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_API', '0029_alter_studentweeklytestresults_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='N/A', max_length=255)),
                ('Course', models.CharField(default='N/A', max_length=255)),
                ('BatchName', models.CharField(default='N/A', max_length=255)),
                ('Date', models.CharField(default='N/A', max_length=255)),
                ('StudentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekly_test_request', to='Data_API.studentdata')),
            ],
        ),
    ]
