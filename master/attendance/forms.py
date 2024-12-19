
from django import forms
from employee.models import Employee
from attendance.models import Devicelogs, Attendance
from attendance.models import Devicelogs
from employee.models import Employee
from attendance.models import Devicelogs
from employee.models import Employee, Category, Department
from django.utils.timezone import make_aware
from datetime import datetime, time, timedelta
from .models import Devicelogs, Attendance
from django.utils.timezone import make_aware
from datetime import timedelta
from django import forms
from .models import Devicelogs
from datetime import timedelta
from django import forms
from .models import Devicelogs, Employee
from datetime import timedelta, datetime, time
from django import forms
from .models import Devicelogs, Employee
from datetime import timedelta, datetime, time
from django import forms
from .models import Devicelogs, Employee

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def get_employee_punching(self):
        if not self.is_valid():
            return None

        date = self.cleaned_data['date']
        start_datetime = datetime.combine(date, time(0, 0))  # Start from midnight
        end_datetime = datetime.combine(date + timedelta(days=1), time(9, 0))  # Up to 9:00 AM next day

        # Fetch device logs for the date range
        user_punching = Devicelogs.objects.using('attendance_db').filter(
            logdate__range=[start_datetime, end_datetime]
        ).order_by('logdate', 'userid')

        employee_punching_data = {}
        for log in user_punching:
            try:
                employee = Employee.objects.get(employee_code=log.userid)
                if log.userid not in employee_punching_data:
                    employee_punching_data[log.userid] = {
                        'employee': employee,
                        'punching_data': []
                    }
                employee_punching_data[log.userid]['punching_data'].append(log)
            except Employee.DoesNotExist:
                continue
        
        return employee_punching_data



class PunchingReportForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
# forms.py

class SinglePunchReportForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# forms.py

class AbsentListForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class AdjustmentDateForm(forms.Form):
    date = forms.DateField(label='Select Date', widget=forms.DateInput(attrs={'type': 'date'}))

class AdjustmentEntryForm(forms.Form):
    employee_code = forms.CharField(label='Employee Code', max_length=100)
    absent = forms.ChoiceField(label='P/AB', choices=[('AB', 'AB'), ('P', 'P')])

class AdjustmentReportViewForm(forms.Form):
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
    month = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=True,
        label='Month'
    )

    month = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 2030)), label='Month', required=True)

class OtStatement(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)


class DateDepCatForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)

class OTAdjustmentForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['ot_hours']



from django import forms

class OTCalculationForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date =  forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



