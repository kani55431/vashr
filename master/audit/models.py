from django.db import models

# Create your models here.
from employee.models import Employee
from django.db import models


class AuditAttendance(models.Model):
    employee_code = models.CharField(max_length=100, blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, related_name="audit_attendance_employee", on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, null=True)
    department =models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    intime_direction = models.CharField(max_length=100, blank=True, null=True,)
    outtime = models.DateTimeField(blank=True, null=True)
    outtime_direction = models.CharField(max_length=100, blank=True, null=True,)
    shift = models.CharField(max_length=50, null=True, blank=True)
    total_working_hours=models.FloatField(default=0, blank=True, null=True)
    p1 = models.DateTimeField(blank=True, null=True)
    p1_direction = models.CharField(max_length=100, blank=True, null=True,)
    p2 = models.DateTimeField(blank=True, null=True)
    p2_direction = models.CharField(max_length=100, blank=True, null=True,)
    p3 = models.DateTimeField(blank=True, null=True)
    p3_direction = models.CharField(max_length=100, blank=True, null=True,)
    p4 = models.DateTimeField(blank=True, null=True)
    p4_direction = models.CharField(max_length=100, blank=True, null=True,)
    p5 = models.DateTimeField(blank=True, null=True)
    p5_direction = models.CharField(max_length=100, blank=True, null=True,)
    p6 = models.DateTimeField(blank=True, null=True)
    p6_direction = models.CharField(max_length=100, blank=True, null=True,)
    p7 = models.DateTimeField(blank=True, null=True)
    p7_direction = models.CharField(max_length=100, blank=True, null=True,)
    p8 = models.DateTimeField(blank=True, null=True)
    p8_direction = models.CharField(max_length=100, blank=True, null=True,)
    p9 = models.DateTimeField(blank=True, null=True)
    p9_direction = models.CharField(max_length=100, blank=True, null=True,)
    p10 = models.DateTimeField(blank=True, null=True)
    p10_direction = models.CharField(max_length=100, blank=True, null=True,)
    adjustment = models.BooleanField(default=False)
    adjustment_count = models.IntegerField(default=0)
    ot_hours = models.FloatField(default=0, blank=True, null=True)
    absent = models.CharField(max_length=4, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    user = models.CharField(max_length=4, blank=True, null=True)


    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['employee', 'date'], name='unique_audit_attendance_per_employee_per_day')
        ]
        verbose_name = 'Audit Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        if self.employee:
            return f"{self.employee.employee_code} - {self.date}"
        return f"Unknown Employee - {self.date}"


class Holiday(models.Model):
    HOLIDAY_CHOICES = [
        ('WH', 'Weekly Holiday'),
        ('NH', 'National Holiday'),
        ('FH', 'Festival Holiday')
    ]

    date = models.DateField()
    holiday_type = models.CharField(max_length=20, choices=HOLIDAY_CHOICES)
    festival_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.get_holiday_type_display()} {self.festival_name or ''}"

    class Meta:
        verbose_name = 'Holiday'
        verbose_name_plural = 'Holidays'
        ordering = ['date']


class WeekOff(models.Model):
    DAY_CHOICES = [
        ('1', 'Sunday'),
        ('2', 'Monday'),
        ('3', 'Tuesday'),
        ('4', 'Wednesday'),
        ('5', 'Thursday'),
        ('6', 'Friday'),
        ('7', 'Saturday'),
    ]
    
    employee_code = models.OneToOneField(
        Employee, blank=True, null=True, related_name="weekoff_employee", on_delete=models.CASCADE
    )
    days = models.CharField(max_length=20, choices=DAY_CHOICES)
    
    def __str__(self):
        return f"{self.employee_code} - {self.get_days_display()}"




from django.db import models

class PFAbstract(models.Model):
    month = models.CharField(max_length=50)  # Store the month as a string (e.g., 'January')
    year = models.IntegerField()  # Store the year as an integer
    department_name = models.CharField(max_length=255)  # Name of the department
    total_employees = models.IntegerField(default=0)  # Total number of employees
    shift_wages = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total shift wages
    total_per_day_salary = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total per day salary
    total_rent = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total rent
    total_ot_hours = models.IntegerField(default=0)  # Total overtime hours
    total_basic_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Basic salary amount
    total_da_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Dearness Allowance
    total_hra_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # House Rent Allowance
    total_pf_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Provident Fund
    total_esi_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Employee State Insurance
    total_paid_days = models.IntegerField(default=0)  # Total paid days
    advance_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Advance deductions
    mess_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Mess deductions
    store_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Store deductions
    others_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Other deductions
    total_deductions = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Total deductions
    net_salary_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Net salary
    total_gross_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Gross salary

    def __str__(self):
        return f"{self.department_name} ({self.month} {self.year})"
