from django import forms
from django_select2.forms import Select2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import Employee, Wages,Deduction, Incentive, Department, Category
from django.core.exceptions import ValidationError 

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
                'status',
                'migrant_worker_specific',
                'food_expense'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )

    class Media:
        js = ('assets/js/calculate_age.js',)  # Define the path to your JavaScript file


class EmployeeUploadForm(forms.Form):
    file = forms.FileField()

from django import forms
from .models import Designation, Category, Department
from django.forms import TextInput

class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'account_no': TextInput(attrs={'placeholder': 'Enter account number'}),  # or another appropriate widget
        }





class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'hours']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'category']






class WagesForm(forms.ModelForm):
    class Meta:
        model = Wages
        fields = ['employee', 'per_day',   'basic_precentage', 'da_precentage', 'hra_precentage','other_allowance_precentage',  'rent', 'start_date', 'end_date']
        widgets = {
            'employee': Select2Widget,
            'start_date':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
          
        }

    


class WagesEditForm(forms.ModelForm):
    class Meta:
        model = Wages
        fields = ['employee', 'per_day', 'basic_precentage', 'da_precentage', 'hra_precentage','other_allowance_precentage' ,  'rent', 'start_date', 'end_date']

        widgets = {
            'employee': Select2Widget,
            'per_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


# forms.py
from django import forms

class WagesUploadForm(forms.Form):
    file = forms.FileField()


class IncentiveForm(forms.ModelForm):
    class Meta:
        model = Incentive
        fields = ['date',]
        widgets = {  
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
         }


class IncentiveAmountForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)





class DeductionForm(forms.Form):
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    deduction_type = forms.ChoiceField(choices=[
        ('advance', 'Advance'),
        ('mess', 'Mess'),
        ('store', 'Store'),
        ('others', 'Others')
    ], required=True)


class DeductionAmountForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)



from django import forms
from .models import Deduction

class DeductionEditForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['employee', 'date', 'deduction_type', 'amount']


       
from django import forms
from django import forms
from .models import Category, Department
from django import forms
from .models import Category, Department

class NonPfSalaryForm(forms.Form):
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




class ExtraDaysSalaryForm(forms.Form):
    month = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2024, 2100)),  # Adjust year range as needed
        label='Month',
        required=True
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Category",
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        label="Department",
    )



class DeductionFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Start Date")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="End Date")
    deduction_type = forms.ChoiceField(
        choices=[('', 'All')] + Deduction.DEDUCTION_TYPE_CHOICES,
        required=False,
        label="Deduction Type"
    )



# forms.py

from django import forms

class EmployeePFESIUploadForm(forms.Form):
    excel_file = forms.FileField(label="Select Excel File")



from django import forms
#for dates
class EmployeeDatesUploadForm(forms.Form):
    excel_file = forms.FileField(label="Select Excel File")


class NonPfCategorySalaryForm(forms.Form):
    month = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2024, 2100)),  # Adjust year range as needed
        label='Month',
        required=True
    )
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='',
        widget=forms.Select(attrs={'style': 'display:none;'}),  # Hides the category field
    )
    
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        label='',
        widget=forms.Select(attrs={'style': 'display:none;'}),  # Hides the department field
    )






######################commiosnm and leaders ############

# forms.py
from django import forms
from .models import Leader, LeaderCommissionWages
# forms.py
from django import forms
from .models import Leader, LeaderCommissionWages

class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        fields = ['name', 'joining_date', 'relieving_date', 'status']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'relieving_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class LeaderCommissionWagesForm(forms.ModelForm):
    class Meta:
        model = LeaderCommissionWages
        fields = ['leader', 'amount', 'from_date', 'to_date']
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }





from django import forms
from .models import Leader
from django import forms
from .models import Leader  # Ensure to import your Leader model

class CommissionAttendanceForm(forms.Form):
    leader = forms.ModelChoiceField(
        queryset=Leader.objects.filter(status='active'),  # Ensure 'active' is a string or constant
        label='Select Leader',
        required=True
    )
    month = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'month',
                'class': 'form-control',  # Add Bootstrap classes for styling (optional)
                'placeholder': 'YYYY-MM'   # Optional placeholder
            }
        ),
        label='Select Month',
        required=True,
        input_formats=['%Y-%m']  # Specify input format for better parsing
    )



from django import forms

class ExtraDaysCommissionForm(forms.Form):
    leader = forms.ModelChoiceField(
        queryset=Leader.objects.filter(status='active'),  # Ensure 'active' is a string or constant
        label='Select Leader',
        required=True
    )
    month = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'month',
                'class': 'form-control',  # Add Bootstrap classes for styling (optional)
                'placeholder': 'YYYY-MM'   # Optional placeholder
            }
        ),
        label='Select Month',
        required=True,
        input_formats=['%Y-%m']  # Specify input format for better parsing
    )
    



# forms.py
from django import forms

class LeaderUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File for Leaders")

class LeaderCommissionWagesUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File for Leader Commission Wages")


class EmployeeLeaderUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File for Employees")




class MonthForm(forms.Form):
    month = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2024, 2100)),  # Adjust year range as needed
        label='Month',
        required=True
    )