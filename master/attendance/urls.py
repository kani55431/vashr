from django.urls import path
from attendance import views
urlpatterns = [
     path('device-logs/', views.device_logs, name='device_logs'),
    path('import_punching_data/', views.import_punching_data_view, name='import_punching_data'),
    path('import_success/', views.import_success_view, name='import_success'),
    path('attendance_list/', views.attendance_list_view, name='attendance_list'),
    path('attendance_reports/', views.attendance_reports, name='attendance_reports'),
    path('calculate_ot_hours_view/', views.calculate_ot_hours_view, name='calculate_ot_hours_view'),
    path('bulk_upload_attendance_employee_wise/', views.bulk_upload_attendance_employee_wise, name='bulk_upload_attendance_employee_wise'),
    
    
    #reports
    path('punching_report/', views.punching_report_view, name='punching_report'),
    path('punching-report/download/<date>/', views.download_punching_report_excel, name='download_punching_report_excel'),
    path('single_punch_report/', views.single_punch_report_view, name='single_punch_report'),
    path('single-punch-report/download/<str:date>/', views.download_single_punch_report_excel, name='download_single_punch_report_excel'),
    path('absent_list/', views.absent_list_view, name='absent_list'),
    #get the details from employee model 
    path('date_selection_view/', views.date_selection_view, name='date_selection_view'),
    path('punchingattendance/adjustment-entry-view/<str:date>/', views.adjustment_attendance_details_view, name='adjustment_entry_view'),
    path('monthly_attendance_view', views.monthly_attendance_view, name='monthly_attendance_view'),
    path('monthly_attendance_results', views.monthly_attendance_results, name='monthly_attendance_results'),
    path('monthly_attendance_download_pdf/', views.monthlyattendancedownload_pdf, name='monthly_attendance_download_pdf'),
    path('monthly_attendance_download_excel/', views.monthly_attendance_download_excel, name='monthly_attendance_download_excel'),


    path('timecard_view', views.timecard_view, name='timecard_view'),
    #path('timecard/results/', views.timecard_results_view, name='timecard_results'),
    path('timecard/download/', views.timecard_download_pdf, name='timecard_download_pdf'),


    path('otstatement/', views.otstatement_view, name='otstatement'),
    path('ot-statement/results/', views.ot_statement_results_view, name='ot_statement_results'),
    path('otstatement/download/', views.otstatement_download_excel, name='otstatement_download_excel'),
    path('otstatement_download_pdf/', views.otstatement_download_pdf, name='otstatement_download_pdf'),
    path('ot_adjustment_entry/', views.ot_adjustment_entry_view, name='ot_adjustment_entry'),
    path('ot_adjustment_success/', views.ot_adjustment_success_view, name='ot_adjustment_success'),



    #updated 2.12.2024
    path('update_ot_hours_view/', views.update_ot_hours_view, name='update_ot_hours_view'),
   




]