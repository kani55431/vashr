from django.db import models
from django.conf import settings
from django.utils import timezone  # Add this import statement

if settings.ENABLE_DEVICELOGS == "yes":
    class Devicelogs(models.Model):
        devicelogid = models.AutoField(db_column='DeviceLogId',primary_key=True)  # Field name made lowercase.
        downloaddate = models.DateTimeField(db_column='DownloadDate', blank=True, null=True)  # Field name made lowercase.
        deviceid = models.IntegerField(db_column='DeviceId')  # Field name made lowercase.
        userid = models.CharField(db_column='UserId', max_length=50)  # Field name made lowercase.
        logdate = models.DateTimeField(db_column='LogDate')  # Field name made lowercase.
        direction = models.CharField(db_column='Direction', max_length=255, blank=True, null=True)  # Field name made lowercase.
        attdirection = models.CharField(db_column='AttDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c1 = models.CharField(db_column='C1', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c2 = models.CharField(db_column='C2', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c3 = models.CharField(db_column='C3', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c4 = models.CharField(db_column='C4', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c5 = models.CharField(db_column='C5', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c6 = models.CharField(db_column='C6', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c7 = models.CharField(db_column='C7', max_length=255, blank=True, null=True)  # Field name made lowercase.
        workcode = models.CharField(db_column='WorkCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

        class Meta:
            # managed = False
            db_table = 'DeviceLogs'
            ordering = ['-logdate']


        @property    
        def getTime(self):
            time = self.logdate.time()
            return time
else:
    class Devicelogs(models.Model):
            devicelogid = models.AutoField(db_column='Sno',primary_key=True)  # Field name made lowercase.
            downloaddate = models.DateTimeField(db_column='DownloadDate', blank=True, null=True)  # Field name made lowercase.
            devicename = models.CharField(db_column='devicename', max_length=255, blank=True, null=True)   # Field name made lowercase.
            userid = models.CharField(db_column='EmpCode', max_length=50)  # Field name made lowercase.
            logdate = models.DateTimeField(db_column='datetime')  # Field name made lowercase.
            direction = models.CharField(db_column='direction', max_length=255, blank=True, null=True)  # Field name made lowercase.
            serialnumber = models.CharField(db_column='serianumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
            attdirection = models.CharField(db_column='AttDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c1 = models.CharField(db_column='C1', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c2 = models.CharField(db_column='C2', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c3 = models.CharField(db_column='C3', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c4 = models.CharField(db_column='C4', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c5 = models.CharField(db_column='C5', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c6 = models.CharField(db_column='C6', max_length=255, blank=True, null=True)  # Field name made lowercase.
            c7 = models.CharField(db_column='C7', max_length=255, blank=True, null=True)  # Field name made lowercase.
            workcode = models.CharField(db_column='WorkCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

            class Meta:
                # managed = False
                db_table = 'raw'
                ordering = ['-logdate']

            @property    
            def getTime(self):
                time = self.logdate.time()
                return time
if settings.ENABLE_DEVICELOGS:
    class DeviceLogs_Processed(models.Model):
        devicelogid = models.AutoField(db_column='DeviceLogId',primary_key=True)  # Field name made lowercase.
        downloaddate = models.DateTimeField(db_column='DownloadDate', blank=True, null=True)  # Field name made lowercase.
        deviceid = models.IntegerField(db_column='DeviceId')  # Field name made lowercase.
        userid = models.CharField(db_column='UserId', max_length=50)  # Field name made lowercase.
        logdate = models.DateTimeField(db_column='LogDate')  # Field name made lowercase.
        direction = models.CharField(db_column='Direction', max_length=255, blank=True, null=True)  # Field name made lowercase.
        attdirection = models.CharField(db_column='AttDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c1 = models.CharField(db_column='C1', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c2 = models.CharField(db_column='C2', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c3 = models.CharField(db_column='C3', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c4 = models.CharField(db_column='C4', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c5 = models.CharField(db_column='C5', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c6 = models.CharField(db_column='C6', max_length=255, blank=True, null=True)  # Field name made lowercase.
        c7 = models.CharField(db_column='C7', max_length=255, blank=True, null=True)  # Field name made lowercase.
        workcode = models.CharField(db_column='WorkCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

        class Meta:
            # managed = False
            db_table = 'DeviceLogs_Processed'
            ordering = ['-logdate']


        @property    
        def getTime(self):
            time = self.logdate.time()
            return time

class LocalDevicelogs(models.Model):
    devicelogid = models.AutoField(db_column='DeviceLogId',primary_key=True)  # Field name made lowercase.
    downloaddate = models.DateTimeField(db_column='DownloadDate', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId')  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=50)  # Field name made lowercase.
    logdate = models.DateTimeField(db_column='LogDate')  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attdirection = models.CharField(db_column='AttDirection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c1 = models.CharField(db_column='C1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c2 = models.CharField(db_column='C2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c3 = models.CharField(db_column='C3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c4 = models.CharField(db_column='C4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workcode = models.CharField(db_column='WorkCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'LocalDeviceLogs'
        ordering = ['-logdate']


    @property    
    def getTime(self):
        time = self.logdate.time()
        return time





APPLICABLE = [
    ('AB', 'AB'),
    ('P', 'P'),
]
from employee.models import Employee


class Attendance(models.Model):
    employee_code = models.CharField(max_length=100, blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, related_name="attendance_employee", on_delete=models.CASCADE)
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
    absent = models.CharField(max_length=4, blank=True, null=True, choices=APPLICABLE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    user = models.CharField(max_length=4, blank=True, null=True)
    # New field to indicate manual edits
    is_manual_edit = models.BooleanField(default=False, blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['employee', 'date'], name='unique_attendance_per_employee_per_day')
        ]
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return str(self.employee.employee_code) + "-" + str(self.date)

