from django.contrib import admin
from .models import Devicelogs, LocalDevicelogs
from django.urls import path
from django.shortcuts import render
from import_export.admin import ImportExportMixin
from django.conf import settings
from django.contrib import admin
from .models import Attendance

from audit.models import AuditAttendance


class MultiDBModelAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('pk','devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7')
    list_display_links = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']
    search_fields = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']
    # A handy constant for the name of the alternate database.
    using = "attendance_db"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('print/', self.print_view, name='custom_print'),
        ]
        return custom_urls + urls

    def print_view(self, request):
        # Perform any necessary data processing based on the date filter
        date_filter = request.GET.get('date')
        
        # Example code to fetch filtered data
        queryset = self.get_queryset(request).filter(logdate__date=date_filter)
        # Pass the processed data to the custom_print.html template
        context = {
            'data': queryset,
            'date_filter': date_filter,
        }
        return render(request, 'admin/devicelogs_print.html', context)

admin.site.register(Devicelogs,MultiDBModelAdmin)

if settings.ENABLE_DEVICELOGS == "yes":
    class DevicelogsProcessedMultiDBModelAdmin(admin.ModelAdmin):
        list_display = ('pk','devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7')
        list_display_links = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']
        search_fields = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']
        # A handy constant for the name of the alternate database.
        using = "attendance_db"

        def save_model(self, request, obj, form, change):
            # Tell Django to save objects to the 'other' database.
            obj.save(using=self.using)

        def delete_model(self, request, obj):
            # Tell Django to delete objects from the 'other' database
            obj.delete(using=self.using)

        def get_queryset(self, request):
            # Tell Django to look for objects on the 'other' database.
            return super().get_queryset(request).using(self.using)

        def formfield_for_foreignkey(self, db_field, request, **kwargs):
            # Tell Django to populate ForeignKey widgets using a query
            # on the 'other' database.
            return super().formfield_for_foreignkey(
                db_field, request, using=self.using, **kwargs
            )

        def formfield_for_manytomany(self, db_field, request, **kwargs):
            # Tell Django to populate ManyToMany widgets using a query
            # on the 'other' database.
            return super().formfield_for_manytomany(
                db_field, request, using=self.using, **kwargs
            )

    admin.site.register(DeviceLogs_Processed,DevicelogsProcessedMultiDBModelAdmin)

class LocalDevicelogsModelAdmin(admin.ModelAdmin):
    list_display = ('pk','devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7')
    list_display_links = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']
    search_fields = ['devicelogid', 'userid','logdate','direction','attdirection','c1','c2','c3','c4','c5','c6','c7']


from django.contrib import admin
from django.db.models import Count
from .models import Attendance

from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Attendance
from django import forms
from django.contrib import admin
from .models import Attendance
from django.contrib import admin
from django.db.models import Count
from .models import Attendance

class DuplicateAttendanceFilter(admin.SimpleListFilter):
    title = 'Show Duplicates'
    parameter_name = 'duplicates'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Show Duplicates'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            # Query to find employees with multiple attendance records for the same date
            duplicates = Attendance.objects.values('employee', 'date') \
                .annotate(date_count=Count('id')) \
                .filter(date_count__gt=1) \
                .values('employee', 'date')

            # Use the above queryset to filter the main queryset to show only duplicates
            return queryset.filter(
                employee__in=[entry['employee'] for entry in duplicates],
                date__in=[entry['date'] for entry in duplicates]
            )
        return queryset

# Define the Admin class
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'employee', 'intime', 'outtime')  # Fields to display in the admin panel
    search_fields = ['employee__employee_code', 'date']  # Allow search by employee code and date
    list_filter = (DuplicateAttendanceFilter,)  # Apply the custom filter to show duplicates only

# Register the model with the custom admin class
admin.site.register(Attendance, AttendanceAdmin)


admin.site.register(LocalDevicelogs,LocalDevicelogsModelAdmin)


