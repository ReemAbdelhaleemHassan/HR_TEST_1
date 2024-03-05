from django.db import models

# Create your models here.
class Employee(models.Model):
    BRANCH_CHOICES = [
        ('branch1', 'Branch 1'),
        ('branch2', 'Branch 2'),
        ('branch3', 'Branch 3'),
        # Add more branches as needed
    ]

    EMPLOYEE_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        # Add more statuses as needed
    ]

    WORK_SYSTEM_CHOICES = [
        ('system1', 'System 1'),
        ('system2', 'System 2'),
        ('system3', 'System 3'),
        # Add more work systems as needed
    ]

    PERIOD_OF_WORK_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        # Add more periods of work as needed
    ]

    TITLE_CHOICES = [
        ('title1', 'Title 1'),
        ('title2', 'Title 2'),
        ('title3', 'Title 3'),
        # Add more titles as needed
    ]

    ADMINISTRATION_CHOICES = [
        ('admin1', 'Administration 1'),
        ('admin2', 'Administration 2'),
        ('admin3', 'Administration 3'),
        # Add more administrations as needed
    ]

    SECTION_CHOICES = [
        ('section1', 'Section 1'),
        ('section2', 'Section 2'),
        ('section3', 'Section 3'),
        # Add more sections as needed
    ]

    name = models.CharField(max_length=255)
    name_in_english = models.CharField(max_length=255)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    employee_status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES)
    date_of_birth = models.DateField()
    work_system = models.CharField(max_length=20, choices=WORK_SYSTEM_CHOICES)
    period_of_work = models.CharField(max_length=20, choices=PERIOD_OF_WORK_CHOICES)
    joining_date = models.DateField()
    start_date = models.DateField(null=True, blank=True)
    contract_expiry_date = models.DateField(null=True, blank=True)
    national_id = models.CharField(max_length=20)
    fingerprint_number = models.CharField(max_length=20, null=True, blank=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    insurance_subscription_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    insurance_number = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=50, choices=TITLE_CHOICES)
    administration = models.CharField(max_length=50, choices=ADMINISTRATION_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    subscribed_to_insurance = models.BooleanField(default=False)
    subject_to_tax = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name
