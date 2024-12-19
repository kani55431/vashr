from django.contrib import admin
from .models import Employee,Category, Department,Wages, Deduction, Designation, ExtraDaysAbstract, NonPFAbstract


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['employee_code']  # Replace these with the fields you want to be searchable

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Deduction)
admin.site.register(Designation)
admin.site.register(ExtraDaysAbstract)
admin.site.register(NonPFAbstract)
@admin.register(Wages)
class WagesAdmin(admin.ModelAdmin):
    list_display = ('employee', 'per_day')

