from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    BRANCH_CHOICES = [
        ('branch1', 'Branch 1'),
        ('branch2', 'Branch 2'),
        ('branch3', 'Branch 3'),
        # Add more branches as needed
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

    name = models.CharField(max_length=255, verbose_name="Name", null=True, blank=True)
    name_in_english = models.CharField(max_length=255, verbose_name="Name in English", null=True, blank=True)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, verbose_name="Branch")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    work_system = models.CharField(max_length=20, choices=WORK_SYSTEM_CHOICES, verbose_name="Work System")
    period_of_work = models.CharField(max_length=20, choices=PERIOD_OF_WORK_CHOICES, verbose_name="Period of Work")
    joining_date = models.DateField(verbose_name="Joining Date")
    start_date = models.DateField(null=True, blank=True, verbose_name="Start Date")
    contract_expiry_date = models.DateField(null=True, blank=True, verbose_name="Contract Expiry Date")
    national_id = models.CharField(max_length=20, verbose_name="National ID")
    fingerprint_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Fingerprint Number")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Base Salary")
    insurance_subscription_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Insurance Subscription Fee")
    insurance_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Insurance Number")
    title = models.CharField(max_length=50, choices=TITLE_CHOICES, verbose_name="Title")
    administration = models.CharField(max_length=50, choices=ADMINISTRATION_CHOICES, verbose_name="Administration")
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, null=True, blank=True, verbose_name="Section")
    subscribed_to_insurance = models.BooleanField(default=False, verbose_name="Subscribed to Insurance")
    subject_to_tax = models.BooleanField(default=False, verbose_name="Subject to Tax")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    
    
    # def __str__(self) -> str:
    #     return self.name
