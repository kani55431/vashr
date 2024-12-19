from django.contrib import admin
from django.db.models import Count
from .models import AuditAttendance, PFAbstract


# Custom Filter to Show Duplicate AuditAttendance Records
class DuplicateAuditAttendanceFilter(admin.SimpleListFilter):
    title = 'Show Duplicates'
    parameter_name = 'duplicates'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Show Duplicates'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            # Query to find duplicate records (employee, date)
            duplicates = AuditAttendance.objects.values('employee', 'date') \
                .annotate(record_count=Count('id')) \
                .filter(record_count__gt=1)

            # Extract employee and date pairs to filter duplicates
            duplicate_employees = [entry['employee'] for entry in duplicates]
            duplicate_dates = [entry['date'] for entry in duplicates]

            # Return only duplicate records
            return queryset.filter(employee__in=duplicate_employees, date__in=duplicate_dates)
        return queryset


# Admin Configuration for AuditAttendance
class AuditAttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'employee', 'intime', 'outtime')  # Fields displayed in the list view
    search_fields = ['employee__employee_code', 'date']  # Search by employee code and date
    list_filter = (DuplicateAuditAttendanceFilter,)  # Custom filter to show duplicates





admin.site.register(PFAbstract)

admin.site.register(AuditAttendance, AuditAttendanceAdmin)





