# Generated by Django 5.0.2 on 2024-03-04 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_in_english', models.CharField(max_length=255)),
                ('branch', models.CharField(choices=[('branch1', 'Branch 1'), ('branch2', 'Branch 2'), ('branch3', 'Branch 3')], max_length=50)),
                ('employee_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], max_length=20)),
                ('date_of_birth', models.DateField()),
                ('work_system', models.CharField(choices=[('system1', 'System 1'), ('system2', 'System 2'), ('system3', 'System 3')], max_length=20)),
                ('period_of_work', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')], max_length=20)),
                ('joining_date', models.DateField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('contract_expiry_date', models.DateField(blank=True, null=True)),
                ('national_id', models.CharField(max_length=20)),
                ('fingerprint_number', models.CharField(blank=True, max_length=20, null=True)),
                ('base_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('insurance_subscription_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('insurance_number', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(choices=[('title1', 'Title 1'), ('title2', 'Title 2'), ('title3', 'Title 3')], max_length=50)),
                ('administration', models.CharField(choices=[('admin1', 'Administration 1'), ('admin2', 'Administration 2'), ('admin3', 'Administration 3')], max_length=50)),
                ('section', models.CharField(choices=[('section1', 'Section 1'), ('section2', 'Section 2'), ('section3', 'Section 3')], max_length=50)),
                ('subscribed_to_insurance', models.BooleanField(default=False)),
                ('subject_to_tax', models.BooleanField(default=False)),
            ],
        ),
    ]
