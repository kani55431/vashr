import datetime
from django.shortcuts import render, redirect
from attendance.models import Devicelogs
from employee.models import Employee, Department, Category
from .models import LocalDevicelogs
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import PunchingReportForm, SinglePunchReportForm, AbsentListForm, OtStatement
from django.shortcuts import render
from .forms import PunchingReportForm, SinglePunchReportForm, AbsentListForm
from .models import Attendance
from employee.models import Employee
from datetime import datetime
from django.utils.timezone import is_naive, make_aware
from django.shortcuts import render, redirect
from .models import Devicelogs, Employee, Attendance
from collections import defaultdict
from datetime import timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from collections import defaultdict
from datetime import timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from .models import Devicelogs, Employee, Attendance
import logging
from datetime import datetime, time, timedelta
from collections import defaultdict
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from .models import Devicelogs, Employee, Attendance
logger = logging.getLogger(__name__)
from django.shortcuts import render
from django.db.models import Q
from .forms import SinglePunchReportForm
from .models import Attendance
import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Attendance, Employee
from .forms import MonthlyAttendanceForm
import datetime
from datetime import datetime, timedelta  # Ensure you import timedelta correctly
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta  # Ensure you import timedelta correctly
from datetime import datetime, timedelta
from django.shortcuts import render
from .forms import MonthlyAttendanceForm
from .models import Attendance, Employee
import datetime

# Usage
now = datetime.datetime.now()
from .forms import DateForm  # Adjust import based on your app structure
#from .utils import calculate_shift, calculate_total_working_hours, calculate_ot_hours
from collections import defaultdict
from datetime import time, timedelta
from django.utils.timezone import make_aware
from django.shortcuts import render, redirect
from .models import Devicelogs, Employee, Attendance
import logging
import math
# Configure logging
logging.basicConfig(level=logging.DEBUG)


from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import math
from collections import defaultdict
from django.shortcuts import redirect, render

from collections import defaultdict
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from .forms import DateForm
from .models import Devicelogs, Employee, Attendance
from collections import defaultdict
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from .forms import DateForm
from .models import Devicelogs, Employee, Attendance

from collections import defaultdict
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from .forms import DateForm
from .models import Devicelogs, Employee, Attendance
import datetime
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive
from collections import defaultdict
from .models import Devicelogs, Employee, Attendance
from .forms import DateForm

# views.py
from django.shortcuts import render
from .models import Devicelogs
from django.core.paginator import Paginator
from django.db.models import Q
# views.py
from django.shortcuts import render
from .models import Devicelogs
from django.core.paginator import Paginator
from django.db.models import Q

def device_logs(request):
    # Get all device logs
    logs = Devicelogs.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '').strip()  # Ensure to strip any whitespace
    if search_query:
        # Filter logs based on user ID or work code
        logs = logs.filter(Q(userid__icontains=search_query) | Q(workcode__icontains=search_query))

    # Pagination
    paginator = Paginator(logs, 50)  # Show 31 logs per page
    page_number = request.GET.get('page')
    page_logs = paginator.get_page(page_number)

    return render(request, 'device_logs.html', {'logs': page_logs, 'search_query': search_query})


  


from collections import defaultdict
from datetime import datetime, timedelta
from django.utils.timezone import make_aware, is_naive
from django.shortcuts import render, redirect
from .models import Employee, Attendance, Devicelogs
from .forms import DateForm
from collections import defaultdict
from datetime import datetime, timedelta  # Make sure to import like this
import datetime  # This will require you to access `datetime.datetime.combine`
from collections import defaultdict
from datetime import datetime, timedelta, time
def calculate_shift(intime):
    """Calculate shift based on intime."""
    if not intime:
        return 'NA'  # If intime is not provided, return 'NA'

    # Convert intime to a float representing hours and minutes (e.g., 7:30 AM becomes 7.50)
    intime_hour = float(intime.strftime('%H.%M'))

    # Determine the shift based on intime ranges
    if 6.50 <= intime_hour < 8.20:
        return '1'  # Shift 1
    elif 8.45 <= intime_hour < 12.00:
        return 'G'  # General Shift
    elif 15.40 <= intime_hour < 16.30:
        return '2'  # Shift 2
    elif 19.45 <= intime_hour < 20.30:
        return 'N'  # Shift 2
    elif 23.45 <= intime_hour or intime_hour < 0.20:
        return '3'  # Shift 3

    # Default return value if no conditions match
    return '-'



def calculate_total_working_hours(intime, outtime):
    """Calculate total working hours between intime and outtime in HH.MM format."""
    if intime and outtime:
        # Ensure intime and outtime are aware datetime objects
        intime = make_aware(intime) if is_naive(intime) else intime
        outtime = make_aware(outtime) if is_naive(outtime) else outtime

        # Handle overnight shifts
        if outtime < intime:
            end_of_day = intime.replace(hour=23, minute=59, second=59, microsecond=999999)
            seconds_until_end_of_day = (end_of_day - intime).total_seconds()
            start_of_next_day = outtime.replace(hour=0, minute=0, second=0, microsecond=0)
            seconds_from_start_of_next_day = (outtime - start_of_next_day).total_seconds()
            total_seconds = seconds_until_end_of_day + seconds_from_start_of_next_day
        else:
            total_seconds = (outtime - intime).total_seconds()

        hours, minutes = divmod(total_seconds / 60, 60)
        return f"{int(hours)}.{int(minutes):02d}"

    return "0.00"


def calculate_ot_hours(total_working_hours, category_hours=None):
    """Calculate overtime hours based on total working hours and category hours."""
    
    # Ensure inputs are numeric
    total_working_hours = float(total_working_hours)
    
    # If category_hours is not provided, the calculation won't work as expected
    if category_hours is None:
        return 0  # No overtime if category_hours is not provided
    
    # Ensure category_hours is a valid number
    category_hours = float(category_hours)  # Convert category_hours to float
    
    # Calculate raw overtime hours
    ot_hours = total_working_hours - category_hours
    
    # Return 0 if the calculated overtime hours are less than or equal to 3 hours
    if ot_hours <= 3:
        return 0
    
    # Extract hours and minutes from ot_hours
    ot_hours_int = int(ot_hours)
    ot_minutes = (ot_hours - ot_hours_int) * 60  # Convert fractional hour to minutes
    
    # Round overtime: if minutes >= 30, round up to the next hour
    if ot_minutes >= 30:
        rounded_ot_hours = ot_hours_int + 1
    else:
        rounded_ot_hours = ot_hours_int

    return rounded_ot_hours  # Return the rounded integer value

def get_workday(log_datetime, category):
    """Determine the workday for a given log datetime based on category."""
    if category and category.name == 'WORKER-I':
        if log_datetime.time() < datetime.time(6, 30):
            return (log_datetime - timedelta(days=1)).date()
    return log_datetime.date()

from collections import defaultdict
from datetime import datetime, timedelta, time
from django.utils.timezone import make_aware, is_naive
from django.shortcuts import render, redirect

from .forms import DateForm

def import_punching_data_view(request):
    """View to handle punching data import from device logs."""
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            # Combine date and time into datetime objects
            start_datetime = datetime.combine(date, time(6, 30))
            end_date = date + timedelta(days=1)
            end_datetime = datetime.combine(end_date, time(8, 30))

            # Fetch device logs within the specified date range
            device_logs = Devicelogs.objects.using('attendance_db').filter(logdate__range=[start_datetime, end_datetime])
            logs_by_employee = defaultdict(list)

            # Group logs by employee ID
            for log in device_logs:
                logs_by_employee[log.userid].append(log)

            # Process each employee's logs
            for employee_code, logs in logs_by_employee.items():
                try:
                    # Fetch employee information
                    employee = Employee.objects.get(employee_code=employee_code)
                    # Fetch the full Category object based on the category name (now assuming category is a string)
                    category = Category.objects.get(name=employee.category)  # Ensure this is a Category object

                    # Now you can access category.hours
                    

                    # Use category.hours to get the working hours
                    category_hours = category.hours  # This should be an integer or float


                    # Sort logs by logdate
                    logs = sorted(logs, key=lambda log: log.logdate)
                    intime, outtime = None, None

                    # Identify the first IN and the last OUT timestamps along with their machines
                    for log in logs:
                        log_time = make_aware(log.logdate) if is_naive(log.logdate) else log.logdate
                        if log.devicename in ['IN 1', 'IN 2']:
                            if intime is None or log_time < intime:
                                intime = log_time
                        elif log.devicename in ['OUT 1', 'OUT 2']:
                            if outtime is None or log_time > outtime:
                                outtime = log_time

                    # Adjust outtime if it is earlier than intime (overnight shifts)
                    if intime and outtime and outtime <= intime:
                        outtime += timedelta(days=1)

                    # Determine the shift based on intime, outtime, and category
                    shift = calculate_shift(intime)
                    total_working_hours = calculate_total_working_hours(intime, outtime)
                    absent = 'P'
                    ot_hours = 0

                    # Directly set ot_hours = 0 for STAFF and STAFFS categories
                    if category  in ['OFFICE STAFF']:
                        ot_hours = 0
                        # Check attendance status
                        if float(total_working_hours) < (float(category.hours) - 1):
                            absent = 'AB'
                    else:
                        # For other categories, calculate OT hours if total working hours exceed category hours
                        
                        total_working_hours_float = float(total_working_hours) if total_working_hours else 0
                        if category  in ['OFFICE STAFF']:
                            ot_hours = 0

                        # Mark as absent if total working hours are less than category hours - 1
                        if total_working_hours_float < (category_hours - 1):
                            absent = 'AB'
                        elif total_working_hours_float > category_hours:
                            ot_hours = calculate_ot_hours(total_working_hours_float, category_hours)

                    # Determine the workday based on intime and category
                    if intime:
                        workday = get_workday(intime, category)

                        # Check for existing attendance records for the employee and workday
                        existing_record = Attendance.objects.filter(
                            employee=employee,
                            date=workday,
                        ).first()

                        if existing_record:
                            # Skip updating if the record is marked as manually edited
                            if existing_record.is_manual_edit:
                                print(f"Skipped manually edited record for {employee_code} on {workday}")
                                continue
                            else:
                                # Update the existing record if it is not manually edited
                                existing_record.intime = intime
                                existing_record.outtime = outtime
                                existing_record.shift = shift
                                existing_record.total_working_hours = total_working_hours
                                existing_record.ot_hours = ot_hours
                                existing_record.absent = absent
                                existing_record.save()
                                print(f"Updated record for {employee_code} on {workday}")
                        else:
                            # Create a new attendance record if no existing record is found
                            Attendance.objects.create(
                                employee=employee,
                                department=department,
                                category=category,
                                date=workday,
                                intime=intime,
                                outtime=outtime,
                                shift=shift,
                                total_working_hours=total_working_hours,
                                ot_hours=ot_hours,
                                absent=absent,
                            )
                            print(f"New record created for {employee_code} on {workday}")

                except Employee.DoesNotExist:
                    # Skip processing for employees not found in the database
                    continue

            # Redirect to a success page after processing
            return redirect('import_success')
    else:
        form = DateForm()

    # Render the form for date input
    return render(request, 'importpunchingdata/import_punching_data.html', {'form': form})

def import_success_view(request):
    return render(request, 'importpunchingdata/import_success.html')



def attendance_list_view(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

def attendance_reports(request):
    return render(request, 'attendance/attendance_reports.html', )


from django.shortcuts import render
from .forms import OTCalculationForm
from .models import Attendance, Employee
import math
def calculate_ot_hours_view(request):
    if request.method == 'POST':
        form = OTCalculationForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            
            # Fetch attendance records within the date range
            attendance_records = Attendance.objects.filter(date__range=[from_date, to_date])
            
            for record in attendance_records:
                employee = record.employee
                category = employee.department.category if employee.department else None
                
                # Skip OFFICE STAFF for OT calculation
                if category and category.name == 'STAFF':
                    ot_hours = 0
                else:
                    total_working_hours = float(record.total_working_hours)
                    fixed_working_hours = float(category.hours) if category and category.hours else 0
                    
                    # Calculate OT hours using the logic
                    ot_hours = max(total_working_hours - fixed_working_hours, 0)
                    
                    # Extract hours and minutes from ot_hours
                    ot_hours_int = int(ot_hours)
                    ot_minutes = (ot_hours - ot_hours_int) * 60
                    
                    # Apply rounding rule
                    if ot_minutes >= 45:
                        ot_hours = ot_hours_int + 1
                    else:
                        ot_hours = 0
                
                # Update the OT hours in the Attendance record
                record.ot_hours = ot_hours
                record.save()
            return render(request, 'attendance/ot_calculation_result.html', {'ot_results': ot_results})
    else:
        form = OTCalculationForm()
    
    return render(request, 'attendance/calculate_ot_hours.html', {'form': form})


def punching_report_view(request):
    if request.method == 'POST':
        form = PunchingReportForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            # Filter attendance records where absent is 'No'
            attendance_records = Attendance.objects.filter(date=date, absent='P').order_by('intime')
            logger.debug(f"Retrieved attendance records: {attendance_records}")
        else:
            logger.debug(f"Form errors: {form.errors}")
            attendance_records = None
    else:
        form = PunchingReportForm()
        attendance_records = None
    
    return render(request, 'reports/punching_report.html', {'form': form, 'attendance_records': attendance_records})


import openpyxl
from django.http import HttpResponse
from django.utils.timezone import localtime

def download_punching_report_excel(request, date):
    # Filter attendance records where absent is 'No'
    attendance_records = Attendance.objects.filter(date=date, absent='P').order_by('intime')

    # Create an in-memory Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = f"Punching Report {date}"

    # Add column headers
    sheet.append([
        'Sl', 'Employee Code', 'Employee', 'Category', 'Department',
        'Shift', 'Intime', 'Outtime', 'TWH', 'OTH', 'Absent'
    ])

    # Add attendance records to the Excel sheet
    for idx, attendance in enumerate(attendance_records, start=1):
         # Handle timezone-aware datetime fields (intime, outtime)
        intime = localtime(attendance.intime).replace(tzinfo=None) if attendance.intime else ''
        outtime = localtime(attendance.outtime).replace(tzinfo=None) if attendance.outtime else ''
        sheet.append([
            idx,
            attendance.employee.employee_code,
            attendance.employee.employee_name,
            attendance.employee.category.name,
            attendance.employee.department.name,
            attendance.shift,
            intime,
            outtime,
            attendance.total_working_hours,
            attendance.ot_hours,
            attendance.absent,
        ])

    # Prepare response for Excel download
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="Punching_Report_{date}.xlsx"'

    # Save workbook to the response
    workbook.save(response)
    return response



def single_punch_report_view(request):
    punch_and_absent_list = []
    if request.method == 'POST':
        form = SinglePunchReportForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            # Fetch records where either intime or outtime is present and matches the selected date
            punch_and_absent_list = Attendance.objects.filter(date=date).filter(
                Q(intime__isnull=False, outtime__isnull=True) | Q(intime__isnull=True, outtime__isnull=False)
            )

            logger.debug(f"Retrieved punch_and_absent_list: {punch_and_absent_list}")
        else:
            logger.debug(f"Form errors: {form.errors}")
    else:
        form = SinglePunchReportForm()

    context = {
        'form': form,
        'punch_and_absent_list': punch_and_absent_list,
    }
    
    return render(request, 'reports/single_punch_report.html', context)

import openpyxl
from django.http import HttpResponse
from django.utils.timezone import localtime

def download_single_punch_report_excel(request, date):
    # Fetch records where either intime or outtime is present and matches the selected date
    punch_and_absent_list = Attendance.objects.filter(date=date).filter(
        Q(intime__isnull=False, outtime__isnull=True) | Q(intime__isnull=True, outtime__isnull=False)
    )

    # Create an Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = f"Single Punch Report - {date}"
    
    # Add headers to the Excel sheet
    headers = ['Sl', 'Employee Code', 'Employee', 'Category', 'Department', 'Shift', 'Intime', 'Outtime', 'P/AB']
    sheet.append(headers)
    
    # Add punch and absent records to the Excel sheet
    for idx, attendance in enumerate(punch_and_absent_list, start=1):
        # Handle timezone-aware datetime fields (intime, outtime)
        intime = localtime(attendance.intime).replace(tzinfo=None) if attendance.intime else ''
        outtime = localtime(attendance.outtime).replace(tzinfo=None) if attendance.outtime else ''
        
        sheet.append([
            idx,
            attendance.employee.employee_code,
            attendance.employee.employee_name,
            attendance.employee.category.name,
            attendance.employee.department.name,  # Convert department model instance to string
            attendance.shift,
            intime,
            outtime,
             attendance.absent,
        ])
    
    # Create a response to download the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="Single_Punch_Report_{date}.xlsx"'
    
    # Save the workbook to the response
    workbook.save(response)
    
    return response


from django.shortcuts import render
from django.db.models import Q
from .forms import AbsentListForm
from .models import Attendance
import logging

logger = logging.getLogger(__name__)
from django.db.models import Q
from django.db.models import Q

def absent_list_view(request):
    attendance_absent_records = []
    absent_employees = []
    
    if request.method == 'POST':
        form = AbsentListForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            # Fetch attendance records where absent is 'Yes' for the selected date
            attendance_absent_records = Attendance.objects.filter(date=date, absent='AB')
            
            # Get all active employees
            active_employees = Employee.objects.filter(status='active')
            
            # Get employees who have attendance records for the selected date
            employees_with_attendance = Attendance.objects.filter(date=date).values_list('employee', flat=True)
            
            # Filter out active employees who do not have attendance records for the selected date
            absent_employees = active_employees.exclude(id__in=employees_with_attendance)

            logger.debug(f"Retrieved attendance_absent_records: {attendance_absent_records}")
            logger.debug(f"Retrieved absent_employees: {absent_employees}")
        else:
            logger.debug(f"Form errors: {form.errors}")
    else:
        form = AbsentListForm()

    context = {
        'form': form,
        'attendance_absent_records': attendance_absent_records,
        'absent_employees': absent_employees,
    }
    
    return render(request, 'reports/absent_list.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Employee, Attendance
from .forms import AdjustmentEntryForm




# views.py
from django.shortcuts import render, redirect
from .forms import AdjustmentDateForm

def date_selection_view(request):
    if request.method == 'POST':
        form = AdjustmentDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            return redirect('adjustment_entry_view', date=date.strftime('%Y-%m-%d'))  # Redirect to attendance details view with selected date
    else:
        form = AdjustmentDateForm()

    return render(request, 'entries/date_selection.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Employee, Attendance
from .forms import DateForm, AdjustmentEntryForm
import datetime
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Employee, Attendance
from .forms import AdjustmentEntryForm, DateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Employee, Attendance
from .forms import AdjustmentEntryForm, DateForm
import datetime

def adjustment_attendance_details_view(request, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    if request.method == 'POST':
        form = AdjustmentEntryForm(request.POST)
        if form.is_valid():
            employee_code = form.cleaned_data['employee_code']
            absent_status = form.cleaned_data['absent']
            employee = get_object_or_404(Employee, employee_code=employee_code)

            # Check if an attendance record already exists
            attendance_record = Attendance.objects.filter(employee=employee, date=date_obj).first()

            if attendance_record:
                # Update the existing record and mark as manual edit
                attendance_record.absent = absent_status
                attendance_record.category = employee.category.name if employee.category else ''
                attendance_record.department = employee.department.name if employee.department else ''
                attendance_record.is_manual_edit = True  # Set manual edit flag
                attendance_record.save()
            else:
                # Create a new attendance record and set manual edit flag
                Attendance.objects.create(
                    employee=employee,
                    date=date_obj,
                    absent=absent_status,
                    category=employee.category.name if employee.category else '',
                    department=employee.department.name if employee.department else '',
                    is_manual_edit=True  # Set manual edit flag
                )

            return redirect(reverse('adjustment_entry_view', kwargs={'date': date}))

    else:
        form = DateForm()

    attendance_records = Attendance.objects.filter(date=date_obj)
    active_employees = Employee.objects.filter(status='active')
    employees_with_attendance = Attendance.objects.filter(date=date_obj).values_list('employee_id', flat=True)
    absent_employees = active_employees.exclude(id__in=employees_with_attendance)

    context = {
        'attendance_records': attendance_records,
        'absent_employees': absent_employees,
        'date_obj': date_obj,
        'form': form,
        'adjustment_form': AdjustmentEntryForm(),
    }
    return render(request, 'entries/attendance_details.html', context)




def adjustment_report_view(request):
    punch_and_absent_list = []
    if request.method == 'POST':
        form = AdjustmentReportViewForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            # Fetch records where either intime or outtime is present and matches the selected date
            punch_and_absent_list = Attendance.objects.filter(date=date).filter(
                Q(intime__isnull=False, outtime__isnull=False) |Q(intime__isnull=True, outtime__isnull=False) |Q(intime__isnull=False, outtime__isnull=True)
            ).filter(absent="P")

            logger.debug(f"Retrieved punch_and_absent_list: {punch_and_absent_list}")
        else:
            logger.debug(f"Form errors: {form.errors}")
    else:
        form = SinglePunchReportForm()

    context = {
        'form': form,
        'punch_and_absent_list': punch_and_absent_list,
    }
    
    return render(request, 'reports/adjustment_entry_report.html', context)

    
from datetime import timedelta
from django.shortcuts import render
from django.utils.dateformat import DateFormat
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import MonthlyAttendanceForm
from .models import Employee, Attendance

from datetime import timedelta
from django.shortcuts import render
from django.utils.dateformat import DateFormat
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import MonthlyAttendanceForm
from .models import Employee, Attendance

def monthly_attendance_view(request):
    attendance_data = []
    dates = []
    start_date = None
    end_date = None

    if request.method == 'POST':
        form = MonthlyAttendanceForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            category = form.cleaned_data['category']
            department = form.cleaned_data['department']

            # Generate a list of dates between start_date and end_date
            dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

            # Get all active employees filtered by category and department if provided
            employees = Employee.objects.filter(status='active')
            if category:
                employees = employees.filter(category=category)
            if department:
                employees = employees.filter(department=department)

            # Fetch attendance records and organize by employee and date
            for employee in employees:
                employee_attendance = []
                present_days = 0
                absent_days = 0
                for date in dates:
                    attendance_record = Attendance.objects.filter(employee=employee, date=date).first()
                    if attendance_record:
                        if attendance_record.absent == 'AB':
                            attendance_record.absent = 'A'
                        employee_attendance.append(attendance_record.absent)
                        if attendance_record.absent == 'P':
                            present_days += 1
                        else:
                            absent_days += 1
                    else:
                        employee_attendance.append('A')
                        absent_days += 1
                attendance_data.append({
                    'employee': employee,
                    'attendance': employee_attendance,
                    'present_days': present_days,
                    'absent_days': absent_days,
                })

            # Save data to session for download purposes
            request.session['attendance_data'] = [
    {
        'employee_code': data['employee'].employee_code,
        'employee_name': data['employee'].employee_name,
        'category': data['employee'].category.name if data['employee'].category else '',
        'department': data['employee'].department.name if data['employee'].department else '',
        'attendance': data['attendance'],
        'present_days': data['present_days'],
        'absent_days': data['absent_days'],
    } for data in attendance_data

]
        
            request.session['dates'] = [date.strftime('%Y-%m-%d') for date in dates]
            request.session['start_date'] = start_date.strftime('%Y-%m-%d')
            request.session['end_date'] = end_date.strftime('%Y-%m-%d')

            return redirect(reverse('monthly_attendance_results'))
    else:
        form = MonthlyAttendanceForm()

    context = {
        'form': form,
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'entries/monthly_attendance.html', context)

    
from dateutil import parser

def monthly_attendance_results(request):
    attendance_data = request.session.get('attendance_data', [])
    dates = [parser.parse(date).date() for date in request.session.get('dates', [])]
    start_date = request.session.get('start_date', '')
    end_date = request.session.get('end_date', '')

    return render(request, 'entries/monthly_attendance_results.html', {
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    })

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)
    if not pdf.err:
        return result.getvalue()
    return None

def monthlyattendancedownload_pdf(request):
    attendance_data = request.session.get('attendance_data', [])
    dates = request.session.get('dates', [])
    start_date = request.session.get('start_date', '')
    end_date = request.session.get('end_date', '')

    context = {
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    }

    pdf = render_to_pdf('entries/monthly_attendance_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="monthly_attendance_report.pdf"'
        return response
    return HttpResponse("Error generating PDF", status=400)

import pandas as pd
from io import BytesIO
from django.http import HttpResponse

def monthly_attendance_download_excel(request):
    attendance_data = request.session.get('attendance_data', [])
    dates = request.session.get('dates', [])
     # Parse start and end dates from the session
    start_date = parser.parse(request.session.get('start_date')).strftime('%Y-%m-%d')
    end_date = parser.parse(request.session.get('end_date')).strftime('%Y-%m-%d')

    # Create a list of day numbers from 1 to n (based on the length of dates)
    day_numbers = list(range(1, len(dates) + 1))

    data = []
    # Add a serial number (sl_no) and calculate total working days for each employee
    for idx, data_entry in enumerate(attendance_data, start=1):
        total_working_days = data_entry['present_days']  # Total present days
        row = [
            idx,  # Serial number
            data_entry['employee_code'],
            data_entry['employee_name'],
            data_entry['category'],
            data_entry['department'],
            total_working_days  # Total working days
        ]
        row.extend(data_entry['attendance'])
        data.append(row)
    
    # Column headers: Serial No, Employee Details, Total Working Days, followed by day numbers (1, 2, 3, etc.)
    columns = ['Sl No', 'Employee Code', 'Employee Name', 'Category', 'Department', 'Total Working Days'] + day_numbers

    # Create a DataFrame with the columns and data
    df = pd.DataFrame(data, columns=columns)
    
    # Write the DataFrame to an Excel file
    with BytesIO() as buffer:
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Monthly Attendance')
        buffer.seek(0)
        
        # Customize the file name to include the start and end dates
        filename = f"monthly_attendance_report_{start_date}_to_{end_date}.xlsx"
        
        # Return the Excel file as a download response
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

#time card

from .forms import TimeCardForm
from .models import Attendance, Employee
from datetime import timedelta
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .forms import TimeCardForm
from .models import Attendance, Employee
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from collections import defaultdict
from .forms import TimeCardForm
from .models import Attendance, Employee
def timecard_view(request):
    form = TimeCardForm(request.POST or None)
    attendance_records = {}
    month = None
    days_in_month = []

    if form.is_valid():
        employee_code = form.cleaned_data.get('employee_code')
        category = form.cleaned_data.get('category')
        department = form.cleaned_data.get('department')
        month = form.cleaned_data.get('month')

        if month:
            # Ensure that `month` is properly converted to string format before storing
            first_day_of_month = month.replace(day=1)
            last_day_of_month = (month.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
            days_in_month = [first_day_of_month + timedelta(days=i) for i in range((last_day_of_month - first_day_of_month).days + 1)]

            filters = {'date__range': [first_day_of_month, last_day_of_month]}
            if employee_code:
                filters['employee__employee_code'] = employee_code.employee_code
            if category:
                filters['employee__department__category'] = category
            if department:
                filters['employee__department'] = department

            # Fetch attendance records and organize by employee and date
            attendance_data = Attendance.objects.filter(**filters).order_by('date')
            employees = Employee.objects.filter(status='active')
            if employee_code:
                employees = employees.filter(employee_code=employee_code.employee_code)
            if category:
                employees = employees.filter(department__category=category)
            if department:
                employees = employees.filter(department=department)

            for employee in employees:
                employee_days = []
                total_days = 0
                absent_days = 0
                total_hours = 0.0
                total_ot_hours = 0

                for date in days_in_month:
                    record = attendance_data.filter(employee=employee, date=date).first()
                    if record:
                        employee_days.append({
                            'date': date.strftime('%Y-%m-%d'),  # Convert date to string
                            'intime': record.intime,
                            'outtime': record.outtime,
                            'total_working_hours': record.total_working_hours,
                            'ot_hours': record.ot_hours,
                            'shift': record.shift,
                            'absent': record.absent,
                        })

                        if record.absent == 'AB':
                            absent_days += 1
                        if record.absent == 'P':
                            total_days += 1
                        if record.total_working_hours:
                            total_hours += record.total_working_hours
                        if record.ot_hours:
                            total_ot_hours += record.ot_hours
                    else:
                        employee_days.append({
                            'date': date.strftime('%d-%m-%Y'),  # Convert date to string
                            'shift_time': '',
                            'intime': '',
                            'outtime': '',
                            'total_working_hours': 0,
                            'ot_hours': 0,
                            'shift': '',
                            'absent': 'AB',
                        })
                        absent_days += 1

                attendance_records[employee] = {
                    'days': list(enumerate(employee_days, start=1)),
                    'total_days': total_days,
                    'absent_days': absent_days,
                    'total_hours': total_hours,
                    'total_ot_hours': total_ot_hours,
                }

           
    context = {
        'form': form,
        'attendance_records': attendance_records,
        'days_in_month': days_in_month if month else [],
        'month': month,
    }

    return render(request, 'entries/timecard.html', context)
def timecard_download_pdf(request):
    from datetime import datetime

    attendance_data = request.session.get('attendance_data', [])
    dates = [datetime.strptime(date, '%Y-%m-%d').date() for date in request.session.get('dates', [])]
    month = request.session.get('month', '')

    if not attendance_data:
        return HttpResponse("No attendance details to export.", status=400)

    context = {
        'attendance_data': attendance_data,
        'dates': dates,
        'month': month,
    }

    pdf = render_to_pdf('entries/timecard_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="TimeCard_{month}.pdf"'
        return response
    return HttpResponse("Error generating PDF", status=400)


from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee, Attendance
from .forms import OtStatement

def otstatement_view(request):
    attendance_data = []
    dates = []
    start_date = None
    end_date = None

    if request.method == 'POST':
        form = OtStatement(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            category = form.cleaned_data['category']
            department = form.cleaned_data['department']

            # Generate a list of dates between start_date and end_date
            dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

            # Get all active employees filtered by category and department if provided
            employees = Employee.objects.filter(status='active')
            if category:
                employees = employees.filter(category=category)
            if department:
                employees = employees.filter(department=department)

            # Fetch attendance records and organize by employee and date
            for employee in employees:
                employee_attendance = []
                present_days = 0
                absent_days = 0
                total_ot_hours = 0
                for date in dates:
                    attendance_record = Attendance.objects.filter(employee=employee, date=date).first()
                    if attendance_record:
                        ot_hours = attendance_record.ot_hours or 0
                        employee_attendance.append(ot_hours)
                        present_days += 1
                        total_ot_hours += ot_hours
                    else:
                        employee_attendance.append(0)  # Set OT hours to 0 if no attendance record
                        absent_days += 1
                attendance_data.append({
                    'employee': employee,
                    'attendance': employee_attendance,
                    'present_days': present_days,
                    'absent_days': absent_days,
                    'total_ot_hours': total_ot_hours,
                })

            # Save data to session for download purposes
            request.session['attendance_data'] = [
                {
                    'employee_code': data['employee'].employee_code,
                    'employee_name': data['employee'].employee_name,
                    'category': data['employee'].category.name if data['employee'].category else '',
                    'department': data['employee'].department.name if data['employee'].department else '',
                    'attendance': data['attendance'],
                    'present_days': data['present_days'],
                    'absent_days': data['absent_days'],
                    'total_ot_hours': data['total_ot_hours'],
                } for data in attendance_data
            ]
            request.session['dates'] = [date.strftime('%Y-%m-%d') for date in dates]
            request.session['start_date'] = start_date.strftime('%Y-%m-%d')
            request.session['end_date'] = end_date.strftime('%Y-%m-%d')
          
            # Redirect to the results page
            return redirect(reverse('ot_statement_results'))
    else:
        form = OtStatement()

    context = {
        'form': form,
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'entries/ot_statement_form.html', context)
from dateutil import parser

def ot_statement_results_view(request):
    attendance_data = request.session.get('attendance_data', [])
    dates = [parser.parse(date).date() for date in request.session.get('dates', [])]
    start_date = request.session.get('start_date', '')
    end_date = request.session.get('end_date', '')

    return render(request, 'entries/ot_statement_results.html', {
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    })


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)
    if not pdf.err:
        return result.getvalue()
    return None
def otstatement_download_pdf(request):
    from django.http import HttpResponse

    attendance_data = request.session.get('attendance_data', [])
    dates = [parser.parse(date).date() for date in request.session.get('dates', [])]
    start_date = request.session.get('start_date', '')
    end_date = request.session.get('end_date', '')

    if not attendance_data:
        return HttpResponse("No salary details to export.", status=400)

    context = {
        'attendance_data': attendance_data,
        'dates': dates,
        'start_date': start_date,
        'end_date': end_date,
    }

    pdf = render_to_pdf('entries/otstatement_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="OT_Statement_{start_date}_to_{end_date}.pdf"'
        return response
    return HttpResponse("Error generating PDF", status=400)


import pandas as pd

import pandas as pd
from io import BytesIO
from django.http import HttpResponse
from dateutil import parser
import pandas as pd
from io import BytesIO
from django.http import HttpResponse
from dateutil import parser

def otstatement_download_excel(request):
    # Retrieve OT data and dates from the session
    attendance_data = request.session.get('attendance_data', [])
    dates = request.session.get('dates', [])

    # Parse start and end dates from the session
    start_date = parser.parse(request.session.get('start_date')).strftime('%Y-%m-%d')
    end_date = parser.parse(request.session.get('end_date')).strftime('%Y-%m-%d')

    # Create a list of day numbers from 1 to n (based on the length of dates)
    day_numbers = list(range(1, len(dates) + 1))

    data = []
    # Loop through the attendance_data and build each row for the Excel sheet
    for idx, data_entry in enumerate(attendance_data, start=1):
        row = [
            idx,  # Serial number
            data_entry['employee_code'],
            data_entry['employee_name'],
            data_entry['category'],
            data_entry['department'],
            data_entry['total_ot_hours']  # Add total OT hours
        ]
        # Reference the correct key for OT adjustment data
        row.extend(data_entry['attendance'])  # OT adjustment data (for each date)
        data.append(row)

    # Column headers: Serial No, Employee Details, Total OT Hours, followed by day numbers (1, 2, 3, etc.)
    columns = ['Sl No', 'Employee Code', 'Employee Name', 'Category', 'Department', 'Total OT Hours'] + day_numbers

    # Create a DataFrame with the data and columns
    df = pd.DataFrame(data, columns=columns)

    # Write the DataFrame to an Excel file
    with BytesIO() as buffer:
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='OT Adjustment Statement')
        buffer.seek(0)

        # Customize the filename with start and end dates
        filename = f"ot_adjustment_report_{start_date}_to_{end_date}.xlsx"

        # Return the Excel file as an HTTP response for download
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response




from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import Employee, Attendance
from .forms import DateDepCatForm, OTAdjustmentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import Employee, Attendance
from .forms import DateDepCatForm, OTAdjustmentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from datetime import datetime  # Corrected import
from .models import Attendance, Employee
from .forms import DateDepCatForm
from django.urls import reverse

@csrf_exempt
def ot_adjustment_entry_view(request):
    form = DateDepCatForm()
    selected_date = None
    attendance_records = []

    if request.method == 'POST':
        if 'search_criteria' in request.POST:
            form = DateDepCatForm(request.POST)
            if form.is_valid():
                selected_date = form.cleaned_data['date']
                request.session['selected_date'] = selected_date.strftime('%Y-%m-%d')

        elif 'save' in request.POST:
            selected_date = request.session.get('selected_date')
            if selected_date:
                selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()  # Fixed reference

            # Handling the existing records
            attendance_ids = request.POST.getlist('attendance_ids')
            for attendance_id in attendance_ids:
                try:
                    attendance_id = int(attendance_id)
                    ot_hours = request.POST.get(f'ot_hours_{attendance_id}')
                    attendance = Attendance.objects.filter(id=attendance_id).first()
                    if attendance:
                        attendance.ot_hours = ot_hours
                        attendance.is_manual_edit = False  # Mark as a manual edit
                        attendance.save()
                except (ValueError, TypeError):
                    continue

            # Handling new employee entries for overtime adjustments
            employee_code = request.POST.get('new_employee_code')
            ot_hours = request.POST.get('new_ot_hours')
            if employee_code and ot_hours:
                employee = get_object_or_404(Employee, employee_code=employee_code)
                Attendance.objects.create(
                    employee=employee,
                    date=selected_date,
                    ot_hours=ot_hours,
                    is_manual_edit=True  # Mark new entry as a manual edit
                )

            return redirect(reverse('ot_adjustment_success'))

    elif request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        employee_code = request.GET.get('employee_code')
        selected_date = request.session.get('selected_date')

        if selected_date:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()  # Fixed reference

        employee = Employee.objects.filter(employee_code=employee_code).first()
        if employee:
            attendance_record = Attendance.objects.filter(employee=employee, date=selected_date).first()
            if attendance_record:
                employee_data = {
                    'employee_code': employee.employee_code,
                    'employee_name': employee.employee_name,
                    'category': employee.category.name if employee.category else '',
                    'department': employee.department.name if employee.department else '',
                    'attendance': {
                        'id': attendance_record.id,
                        'ot_hours': attendance_record.ot_hours
                    }
                }
            else:
                employee_data = {
                    'employee_code': employee.employee_code,
                    'employee_name': employee.employee_name,
                    'category': employee.category.name if employee.category else '',
                    'department': employee.department.name if employee.department else '',
                    'attendance': None
                }
            return JsonResponse({'employee': employee_data})
        else:
            return JsonResponse({'error': 'Employee not found'})

    context = {
        'form': form,
        'selected_date': selected_date,
        'attendance_records': attendance_records,
    }
    return render(request, 'entries/ot/ot_adjustment_form.html', context)


def ot_adjustment_success_view(request):
    return render(request, 'entries/ot/ot_adjustment_success.html')






################22.09.2024.#############################

###updation upload employee attemdance#######
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance, Employee
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance, Employee
import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Employee, Attendance
import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Employee, Attendance
import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Employee, Attendance

def bulk_upload_attendance_employee_wise(request):
    if request.method == 'POST':
        attendance_file = request.FILES.get('attendance_file')

        if attendance_file:
            try:
                # Read the Excel file into a DataFrame
                df = pd.read_excel(attendance_file)

                # Ensure the required columns exist
                required_columns = ['T NO'] + [col for col in df.columns if isinstance(col, str) and '/' in col]
                for col in required_columns:
                    if col not in df.columns:
                        messages.error(request, f"Missing required column: {col}")
                        return redirect('bulk_upload_attendance_employee_wise')

                # Transform the data from wide to long format
                long_df = pd.melt(
                    df,
                    id_vars=['T NO'],          # Columns to keep as-is
                    var_name='Date',           # New column for the date headers (e.g., "01/11/2024", "02/11/2024")
                    value_name='Absent'        # New column for the attendance values (e.g., "AB", "P")
                )

                # Rename columns to match your database schema
                long_df.rename(columns={
                    'T NO': 'employee_code',
                    'Date': 'date',
                    'Absent': 'absent'
                }, inplace=True)

                # Process each row
                records_processed = False
                for _, row in long_df.iterrows():
                    employee_code = row.get('employee_code')
                    date = row.get('date')
                    absent = row.get('absent')

                    # Skip rows without employee codes
                    if not employee_code:
                        messages.warning(request, "Employee Code is missing in a row. This row will be skipped.")
                        continue

                    # Check if the employee exists
                    try:
                        employee = Employee.objects.get(employee_code=employee_code)
                    except Employee.DoesNotExist:
                        messages.warning(request, f"Employee code {employee_code} not found. Record skipped.")
                        continue

                    # Update or create the attendance record
                    Attendance.objects.update_or_create(
                        employee=employee,
                        date=pd.to_datetime(date).date(),  # Convert to Python `date` object
                        defaults={
                            'absent': absent,
                            'is_manual_edit': True  # Mark as manually edited
                            }
                    )
                    records_processed = True

                if records_processed:
                    messages.success(request, "Attendance records processed successfully.")
                else:
                    messages.info(request, "No valid records were uploaded.")

            except Exception as e:
                messages.error(request, f"Error processing the file: {e}")

            return redirect('bulk_upload_attendance_employee_wise')  # Redirect to the upload page

    return render(request, 'entries/attendance/bulk_upload_attendance_employee_wise.html')

#updated 2.12.2024
from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance
from django.shortcuts import render
from .models import Attendance  # Replace with your actual model
from datetime import datetime
from django.shortcuts import render
from .models import Attendance  # Replace with your actual model
from datetime import datetime
from django.shortcuts import render
from .models import Attendance  # Replace with your actual model
from datetime import datetime

def update_ot_hours_view(request):
    records = None
    updated_count = 0
    from_date = None
    to_date = None

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        # Convert dates to datetime objects
        from_date_obj = datetime.strptime(from_date, '%Y-%m-%d')
        to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')

        # Query to get records within the date range
        records = Attendance.objects.filter(date__range=(from_date_obj, to_date_obj))
        
        # Update OT hours to 0 only for employees in the 'OFFICE STAFF' category and not already marked as manual edit
        for record in records:
            # Check if the employee's category is 'OFFICE STAFF' and 'is_manual_edit' is False
            if record.employee.category.name == 'OFFICE STAFF' and not record.is_manual_edit:
                record.ot_hours = 0  # Set OT hours to 0 for these employees
                record.is_manual_edit = True  # Mark as a manual edit
                record.save()  # Save the changes to the database
                updated_count += 1

    return render(request, 'attendance/update_ot_hours.html', {
        'records': records,
        'updated_count': updated_count,
        'from_date': from_date,
        'to_date': to_date,
    })
