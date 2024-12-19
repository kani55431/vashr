from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from django.core.exceptions import ValidationError



##employe model 
APPLICABLE = [
    ('yes', 'yes'),
    ('no', 'no'),
]

DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

SALARY_TYPE = [
    ('daily', 'daily'),
    ('monthly', 'monthly'),
]

AMOUNT_TRANSFER = [
    ('cash', 'cash'),
    ('bank', 'bank'),
]

STATUS = [
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('pending', 'pending'),
]
ACTIVE_STATUS = [
    ('yes','yes'),
    ('no','no'),
    ('pending','pending'),
]
ATTN_DIRECTION = [
    ('in', 'in'),
    ('out', 'no'),
]
GENDER = [
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
]
HANDICAPPED = [
    ('yes', 'yes'),
    ('no', 'no'),
]

MARITAL_STATUS = [
    ('unmarried', 'Unmarried'),
    ('married', 'Married'),
 
]


ADDRESS_TYPE = [
    ('present', 'present'),
    ('permananent', 'permananent'),
]
NOMINEE = [
    ('mother', 'mother'),
    ('father', 'father'),
    ('son', 'son'),
    ('daughter', 'daughter'),
    ('spouse', 'spouse'),
    ('husband', 'husband'),
    ('guardian', 'guardian'),
]

SHIFT_TYPE = [
    ('general', 'general'),
    ('shift', 'shift'),
    ('day', 'day'),
    ('halfnight', 'halfnight'),
    ('fullnight', 'fullnight'),
    ('x', 'x'),
    ('y', 'y'),
    ('staff', 'staff'),
]
MIGRANT_WORKER_SPECIFIC = [
    ('tamil', 'tamil'),
    ('hindi', 'hindi'),
    ('tamil-worker', 'tamil-worker'),
    ('hindi-worker', 'hindi-worker'),
    ('malayalam', 'malayalam'),
    ('telugu', 'telugu'),
    ('kannadam', 'kannadam'),
]# Define choices as a list of tuples
WORKING_MODE = [
    ('dayscholar', 'Day Scholar'),
    ('hostel', 'Hostel'),
    ('outsideworkers', 'Outside Workers'),
]

QUALIFICATION = [
    ('10thbelow', '10th Below'),
    ('10th', '10th'),
    ('12th', '12th'),
    ('ug', 'UG'),
    ('pg', 'pg'),
    ('diplamo', 'Diplamo'),

]
DEPARTMENT =[

]
CATEGORY=[
('OFFICE STAFF','OFFICE STAFF'),
('SUB STAFF','SUB STAFF'),
('SECURITY','SECURITY'),
('WORKERS-I','WORKERS-I'),
('WORKERS-II','WORKERS-II'),
]




class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True)
   

    def __str__(self):
        return self.name
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hours = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_code = models.IntegerField(default=0, blank=True, null=True, verbose_name="Employee Code", unique=True)
    employee_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Employee Name")
    employee_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="Employee Mobile")
    emergency_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="Emergency Mobile")
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Father or Husband Name")
    address_1 = models.TextField(blank=True, null=True, verbose_name="Address Line 1")
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name="Street")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="City")
    district = models.CharField(max_length=100, blank=True, null=True, verbose_name="District")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="State")
    pincode = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pincode")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    age = models.IntegerField(blank=True, null=True, verbose_name="Age")
    qualification = models.CharField(max_length=100, blank=True, null=True, choices=QUALIFICATION, verbose_name="Qualification")
    marital_status = models.CharField(max_length=100, blank=True, null=True,  verbose_name="Marital Status")
    blood_group = models.CharField(max_length=100, blank=True, null=True, verbose_name="Blood Group")
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER, default="male", verbose_name="Gender")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    designation =models.ForeignKey(Designation, on_delete=models.CASCADE,  null=True, blank=True, related_name='employees_by_designation', verbose_name="Designation")
    weekly_off = models.CharField(max_length=100, choices=DAYS_OF_WEEK, blank=True, null=True, verbose_name="Weekly Off")
    date_of_joining = models.DateField(blank=True, null=True, verbose_name="Date of Joining")
    date_of_re_joining = models.DateField(blank=True, null=True, verbose_name="Date of Re-joining")
    date_of_leaving = models.DateField(blank=True, null=True, verbose_name="Date of Leaving")
    pf_esi_applicable = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], default='no', verbose_name="PF/ESI Applicable")
    pf_date_of_joining = models.DateField(blank=True, null=True, verbose_name="PF Date of Joining")
    pf_no = models.CharField(max_length=100, blank=True, null=True, verbose_name="PF Number")
    esi_no = models.CharField(max_length=100, blank=True, null=True, verbose_name="ESI Number")
    bank_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Bank Name")
    account_holder = models.CharField(max_length=200, blank=True, null=True, verbose_name="Account Holder")
    account_no = models.CharField(max_length=100, null=True, blank=True, verbose_name="Account Number")
    ifsc_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="IFSC Code")
    branch = models.CharField(max_length=100, null=True, blank=True, verbose_name="Branch")
    nominee_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nominee Name")
    nominee_relationship = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nominee Relationship")
    nominee_age = models.IntegerField(blank=True, null=True, verbose_name="Nominee Age")
    employee_photo = models.ImageField(upload_to='photos/', null=True, blank=True,  verbose_name="Employee Photo")
    aadhar_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Aadhar Number")
    migrant_worker = models.CharField(max_length=20, blank=True, null=True, choices=APPLICABLE, default="no", verbose_name="Migrant Worker")
    migrant_worker_specific = models.CharField(max_length=20, blank=True, null=True, choices=MIGRANT_WORKER_SPECIFIC ,default="tamil", verbose_name="Migrant Worker Specific")
    food_expense=models.CharField(max_length=20, blank=True, null=True, choices=APPLICABLE, default="no", verbose_name="Food Expense")
    working_mode = models.CharField(max_length=40, blank=True, null=True, choices=WORKING_MODE, default="dayscholar", verbose_name="Working Mode")
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS, default="active", verbose_name="Status")
    ot_available=models.CharField(max_length=100, blank=True, null=True, choices=APPLICABLE, default="no", verbose_name="OT Applicable")

    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    # PF and ESI fields
    pf_percentage = models.FloatField(default=12.0, blank=True, null=True, verbose_name="PF Percentage")
    esi_percentage = models.FloatField(default=0.75, blank=True, null=True, verbose_name="ESI Percentage")
    pf_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, blank=True, null=True, verbose_name="PF Amount")
    esi_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, blank=True, null=True, verbose_name="ESI Amount")

    #new12.11.2024
    leader = models.ForeignKey('Leader', on_delete=models.SET_NULL, null=True, blank=True, related_name='commissioned_employees')
    
    def __str__(self):
        return str(self.employee_code) if self.employee_code else f"Employee {self.pk}"


    def calculate_pf_amount(self, basic_salary):
        """Calculate PF amount based on the basic salary."""
        self.pf_amount = (basic_salary * self.pf_percentage) / 100

    def calculate_esi_amount(self, gross_salary):
        """Calculate ESI amount based on the gross salary."""
        self.esi_amount = (gross_salary * self.esi_percentage) / 100

 
        
class Wages(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,  related_name='employee_wages')
    per_day = models.IntegerField(default=0,blank=True, null=True, verbose_name="Wages/Day")
    basic_precentage = models.IntegerField(default=60, blank=True, null=True, verbose_name="BASIC %")
    da_precentage = models.IntegerField(default=40, blank=True, null=True, verbose_name="DA %")
    hra_precentage = models.IntegerField(default=0, blank=True, null=True, verbose_name="HRA  %")
    other_allowance_precentage = models.IntegerField(default=0, blank=True, null=True, verbose_name="Other allowance %")
    basic_amount = models.IntegerField(default=0, blank=True, null=True, verbose_name="BASIC")
    da_amount = models.IntegerField(default=0, blank=True, null=True, verbose_name=" DA")
    hra_amount = models.IntegerField(default=0, blank=True, null=True, verbose_name="HRA")
    other_allowance = models.IntegerField(default=0, blank=True, null=True, verbose_name="Other allowance")
    rent =  models.IntegerField(default=0,blank=True, null=True, verbose_name="Rent")
    start_date = models.DateField(verbose_name="Start Date", null=True,)
    end_date = models.DateField(verbose_name="End Date", blank=True, null=True)

    def __str__(self):
        return f"{self.employee.employee_name} - {self.per_day}"


class Incentive(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_incentives')
    date = models.DateField(verbose_name="Date")
    incentive_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Incentive Amount")

    def __str__(self):
        return f"{self.employee.employee_code} - {self.date} - {self.incentive_amount}"


class Deduction(models.Model):
    DEDUCTION_TYPE_CHOICES = [
        ('advance', 'Advance'),
        ('mess', 'Mess'),
        ('store', 'Store'),
        ('others', 'Others'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    deduction_type = models.CharField(max_length=20, choices=DEDUCTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee.employee_name} - {self.date}"




from django.utils import timezone
from decimal import Decimal

class Leader(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    name = models.CharField(max_length=100)
    joining_date = models.DateField(default=timezone.now)
    relieving_date = models.DateField(null=True, blank=True)  # Optional if the leader is still active
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    def __str__(self):
        return self.name

class LeaderCommissionWages(models.Model):
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, related_name='commission_wages')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    from_date = models.DateField()
    to_date = models.DateField()
    
    def __str__(self):
        return f"{self.leader.name} - {self.amount} from {self.from_date} to {self.to_date}"




from django.db import models

class ExtraDaysAbstract(models.Model):
    month = models.CharField(max_length=50)  # Store the month as a string (e.g., 'January')
    year = models.IntegerField()  # Store the year as an integer
    department_name = models.CharField(max_length=255)  # Name of the department
    total_employees = models.IntegerField(default=0)  # Total employees
    extra_days_worked = models.IntegerField(default=0)  # Extra days worked
    incentives = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Incentives
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Rent
    total_gross_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Gross amount
    ot_hours = models.IntegerField(default=0)  # Overtime hours
    ot_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Overtime amount
    net_salary = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Net salary

    def __str__(self):
        return f"{self.department_name} ({self.month} {self.year})"



from django.db import models

class NonPFAbstract(models.Model):
    month = models.CharField(max_length=50)  # Store the month (e.g., 'January')
    year = models.IntegerField()  # Store the year
    department_name = models.CharField(max_length=255)  # Department name
    total_employees = models.IntegerField(default=0)  # Total employees
    total_paid_days = models.IntegerField(default=0)  # Total paid days
    total_ot_hours = models.IntegerField(default=0)  # Total overtime hours
    ot_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Overtime amount
    shift_wages = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Shift wages
    per_day_salary = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Per-day salary
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Rent
    advance_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Advance deductions
    canteen_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Canteen deductions
    mess_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Mess deductions
    store_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Store deductions
    others_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Other deductions
    total_deductions = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total deductions
    total_gross_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Gross amount
    net_salary = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Net salary
    total_incentives = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total incentives

    def __str__(self):
        return f"{self.department_name} ({self.month} {self.year})"
