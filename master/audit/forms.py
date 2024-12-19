from employee.models import Employee, Department, Deduction, Designation, Category
from django import forms
from .models import Holiday
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from .models import AuditAttendance
from attendance.models import Attendance
import logging
import logging
from datetime import datetime, time, timedelta
import random
from collections import defaultdict
from django import forms

# Set up logging
logging.basicConfig(level=logging.DEBUG)
import logging
import random
from datetime import datetime, timedelta, time
from collections import defaultdict
from django import forms

# Set up logging
logging.basicConfig(level=logging.DEBUG)
import logging
import random
from datetime import datetime, timedelta, time
from collections import defaultdict
from django import forms

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Days of the week choices
DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]
from django import forms
from datetime import datetime, time, timedelta
from collections import defaultdict
import random

import logging
import logging
import random
from collections import defaultdict
from datetime import datetime, timedelta, time
from django import forms

import logging
import random
from collections import defaultdict
from datetime import datetime, timedelta, time
from django import forms

import logging
import random
from collections import defaultdict
from datetime import datetime, timedelta, time
from django import forms


from datetime import datetime, timedelta, time
import random
import logging
from django.db import transaction, IntegrityError
import logging
import random
from collections import defaultdict
from datetime import datetime, timedelta, time
from django import forms
import logging
import random
from collections import defaultdict
from datetime import datetime, timedelta, time
from django import forms

from datetime import datetime, timedelta, time
import random
import logging

class AttendanceImportForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label="Start Date",
    )
    end_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label="End Date",
    )

    def import_attendance(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        # Log the import range
        logging.debug(f"Importing attendance from {start_date} to {end_date}.")

        # Query attendance records for the specified date range
        attendances = Attendance.objects.filter(
            date__range=[start_date, end_date],
            employee__pf_esi_applicable='yes'
        )

        if not attendances.exists():
            logging.warning("No attendance records found for the selected date range.")
            return False, "No attendance records found for the selected date range."

        # Function to randomize in-time and out-time
        def random_time_within_range(base_time, range_minutes=5):
            minute_offset = random.randint(-range_minutes, range_minutes)
            return base_time + timedelta(minutes=minute_offset)

        # Shift rotation for workers and security
        shift_cycle = ['1', '3', '2']
        employee_shift_tracker = {}

        # Generate the list of all dates in the specified range
        date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

        # Fetch holidays within the date range
        holidays = Holiday.objects.filter(date__range=[start_date, end_date])
        holiday_dates = {holiday.date: holiday.holiday_type for holiday in holidays}

        for date in date_range:
            daily_attendance = attendances.filter(date=date)

            for attendance in daily_attendance:
                employee = attendance.employee
                attendance_day = date.strftime('%A')
                weekly_off_day = employee.weekly_off

                # Initialize variables
                intime = None
                outtime = None
                base_intime = None
                base_outtime = None
                shift = None

                # Check for holiday
                if date in holiday_dates:
                    holiday_type = holiday_dates[date]
                    attendance.absent = holiday_type  # NH or FH
                    shift = None  # No shift for holidays
                    logging.info(f"Marked {employee.employee_code} as {holiday_type} for {date}.")
                elif attendance_day == weekly_off_day:
                    # Weekly off logic
                    shift = 'WO'
                    attendance.absent = 'WO'
                    current_shift = employee_shift_tracker.get(employee.employee_code, shift_cycle[0])
                    current_shift_index = shift_cycle.index(current_shift)
                    new_shift_index = (current_shift_index + 1) % len(shift_cycle)
                    employee_shift_tracker[employee.employee_code] = shift_cycle[new_shift_index]
                elif attendance.absent == 'P':
                    # Handle present employees
                    if employee.category.name.upper() in ['OFFICE STAFF', 'SUB STAFF']:
                        shift = 'G'
                        base_intime = datetime.combine(date, time(9, 30))
                        base_outtime = datetime.combine(date, time(18, 30))
                    
                    elif employee.category.name.upper() in ['WORKERS-I', 'WORKERS-II','SECURITY']:
                        current_shift = employee_shift_tracker.get(employee.employee_code, shift_cycle[0])
                        shift = current_shift
                        if shift == '1':
                            base_intime = datetime.combine(date, time(7, 0))
                            base_outtime = datetime.combine(date, time(15, 0))
                        elif shift == '2':
                            base_intime = datetime.combine(date, time(15, 0))
                            base_outtime = datetime.combine(date, time(23, 0))
                        elif shift == '3':
                            base_intime = datetime.combine(date, time(23, 0))
                            base_outtime = datetime.combine(date, time(7, 0))
                        else:
                            logging.warning(f"Unknown shift {shift} for {employee.employee_code}. Skipping.")
                            continue
                    else:
                        logging.warning(f"Unknown category for employee {employee.employee_code}. Skipping.")
                        continue

                    # Randomize in-time and out-time
                    intime = random_time_within_range(base_intime) if base_intime else None
                    outtime = random_time_within_range(base_outtime) if base_outtime else None
                else:
                    # Absent employees
                    shift = 'AB'
                    attendance.absent = 'AB'
                    intime, outtime = None, None

                # Calculate total working hours
                total_working_hours = 0
                if intime and outtime:
                    total_working_hours = round((outtime - intime).seconds / 3600.0)

                # Update or create AuditAttendance record
                AuditAttendance.objects.update_or_create(
                    employee_code=attendance.employee_code,
                    employee=attendance.employee,
                    category=attendance.employee.category.name,
                    department=attendance.employee.department,
                    date=date,
                    defaults={
                        'intime': intime if shift not in ['WO', 'AB', 'NH', 'FH'] else None,
                        'outtime': outtime if shift not in ['WO', 'AB', 'NH', 'FH'] else None,
                        'shift': shift,
                        'total_working_hours': total_working_hours,
                        'ot_hours': 0,
                        'absent': attendance.absent,
                        'user': attendance.user,
                    }
                )

        return True, f'Successfully imported {attendances.count()} records from {start_date} to {end_date}.'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'dob-input'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'date_of_re_joining': forms.DateInput(attrs={'type': 'date'}),
            'date_of_leaving': forms.DateInput(attrs={'type': 'date'}),
            'pf_date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'department': Select2Widget,
            'category': Select2Widget,
            'designation': Select2Widget,
            'user': Select2Widget,
            'qualification': Select2Widget,
            'marital_status': Select2Widget,
            'gender': Select2Widget,
            'pf_esi_applicable': Select2Widget,
            'nominee_relationship': Select2Widget,
            'migrant_worker': Select2Widget,
            'working_mode': Select2Widget,
            'weekly_off': Select2Widget,
            'status': Select2Widget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Employee Details',
                'employee_code',
                'employee_name',
                'employee_mobile',
                'emergency_mobile',
                'father_or_husband_name',
                'address_1',
                'street',
                'city',
                'district',
                'state',
                'pincode',
                'date_of_birth',
                'age',
                'qualification',
                'marital_status',
                'blood_group',
                'gender',
                'department',
                'category',
                'designation',
                'weekly_off',
                'date_of_joining',
                'date_of_re_joining',
                'date_of_leaving',
                'pf_esi_applicable',
                'pf_date_of_joining',
                'pf_no',
                'esi_no',
                'bank_name',
                'account_holder',
                'account_no',
                'ifsc_code',
                'branch',
                'nominee_name',
                'nominee_relationship',
                'nominee_age',
                'employee_photo',
                'aadhar_number',
                'migrant_worker',
                'working_mode',
                'status'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )

    class Media:
        js = ('assets/js/calculate_age.js',)  # Define the path to your JavaScript file


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['date', 'holiday_type', 'festival_name']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'holiday_type': forms.Select(),
            'festival_name': forms.TextInput(attrs={'placeholder': 'Optional if not Festival'}),
        }
# forms.py



class PunchingReportForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
# forms.py

class SinglePunchReportForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# forms.py

class AbsentListForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class AuditAdjustmentDateForm(forms.Form):
    date = forms.DateField(label='Select Date', widget=forms.DateInput(attrs={'type': 'date'}))

class AuditAdjustmentEntryForm(forms.Form):
    employee_code = forms.CharField(label='Employee Code', max_length=100)
    absent = forms.ChoiceField(label='P/AB', choices=[('AB', 'AB'), ('P', 'P')])

class AuditAdjustmentReportViewForm(forms.Form):
    date = forms.DateField(label='Select Date', widget=forms.DateInput(attrs={'type': 'date'}))



class MonthlyAttendanceForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)


class TimeCardForm(forms.Form):
    employee_code = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        to_field_name='employee_code',
        required=False,
        label='Employee Code'
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        label='Department'
    )
    month = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=True,
        label='Month'
    )

    month = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 2030)), label='Month', required=True)



class PfSalaryForm(forms.Form):
    month = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2024, 2100)),  # Adjust year range as needed
        label='Month',
        required=True
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Category'
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        label='Department'
    )



class EmployeeSalaryForm(forms.Form):
    employee_code = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        to_field_name='employee_code',  # Use employee_code for the selection
        required=False,  # Not required to allow "All Employees" selection
        label='Employee Code',
        empty_label='All Employees'  # Allows an option for all employees
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Category'
    )
    month = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 2050)), required=True, label='Month')





class MonthForm(forms.Form):
    month = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2024, 2100)),  # Adjust year range as needed
        label='Month',
        required=True
    )