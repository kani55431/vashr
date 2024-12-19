from django.urls import path
from . import views

urlpatterns = [
    path('home/payroll/', views.audit_home, name='audit_home'),
    path('import-attendance/', views.audit_import_attendance_view, name='audit_import_attendance'),
    path('audit-attendance-list/', views.audit_attendance_list_view, name='audit_attendance_list'),
    path('upload_attendance_employee_wise/', views.upload_attendance_employee_wise, name='pf_upload_attendance_employee_wise'),

    #shiftrotation


      
    #holidays
    path('holidays/', views.holiday_list_view, name='holiday_list_view'),
    path('holidays/create/', views.holiday_create_view, name='holiday_create_view'),
    path('holidays/<int:pk>/edit/', views.holiday_edit_view, name='holiday_edit_view'),
    path('holidays/<int:pk>/delete/', views.holiday_delete_view, name='holiday_delete_view'),
   
    #reports
    path('audit_punching_report/', views.audit_punching_report_view, name='audit_punching_report'),
    path('audit_single_punch_report/', views.audit_single_punch_report_view, name='audit_single_punch_report'),
    path('audit_absent_list/', views.audit_absent_list_view, name='audit_absent_list'),
    #get the details from employee model 
    path('audit_date_selection_view/', views.audit_date_selection_view, name='audit_date_selection_view'),
    path('audit_punchingattendance/adjustment/entry/view/<str:date>/', views.audit_adjustment_attendance_details_view, name='audit_adjustment_entry_view'),
    path('audit_monthly_attendance_view', views.audit_monthly_attendance_view, name='audit_monthly_attendance_view'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('audit_download-excel/', views.download_excel, name='download_excel'),
    path('audit_timecard_view', views.audit_timecard_view, name='audit_timecard_view'),

    #employeelist 
    path('audit_employees/', views.audit_employee_list, name='audit_employee_list'),
    path('audit_employees/<int:pk>/', views.audit_employee_detail, name='audit_employee_detail'),
    path('audit_employees/add/', views.audit_employee_create, name='audit_employee_create'),
    path('audit_employees/<int:pk>/edit/', views.audit_employee_update, name='audit_employee_update'),
    path('audit_employees/<int:pk>/delete/', views.audit_employee_delete, name='audit_employee_delete'),
    path('audit_employees/inactive/', views.InactiveEmployeeListView.as_view(), name='audit_inactive_employee_list'),
    #salary 
    ###########
    path('audit_salary_reports/', views.audit_salary_reports, name='audit_salary_reports'),
     path('audit_pf_salary_view/', views.audit_pf_salary_view, name='audit_pf_salary_view'),
    path('pf_salary_details_view/', views.pf_salary_details_view, name='pf_salary_details_view'),
    path('audit/pf-salary/pdf/', views.audit_pf_salary_pdf, name='audit_pf_salary_pdf'),
    path('audit/pf-salary/excel/', views.audit_pf_salary_excel, name='audit_pf_salary_excel'),
    path('pf_esi_statement_excel/', views.pf_esi_statement_excel, name='pf_esi_statement_excel'),
   
   
    path('employee-salary/', views.employee_salary_view, name='employee_salary_view'),
    path('bank_details_pf_salary/', views.bank_details_pf_salary, name='bank_details_pf_salary'),
    path('bank_audit_pf_salary_excel/', views.bank_audit_pf_salary_excel, name='bank_audit_pf_salary_excel'),
   
    path('generate-employee-salary-pdf/', views.employee_salary_download_pdf, name='generate_employee_salary_pdf'),


    path('pf_category_totals_view', views.pf_category_totals_view, name='pf_category_totals_view'),
    path('pf_export_department_totals_excel', views.pf_export_department_totals_excel, name='pf_export_department_totals_excel'),

    #pfabstractsave
    path('save_pf_abstract', views.save_pf_abstract, name='save_pf_abstract'),

    path('pf_ecr_form_statement_excel/', views.pf_ecr_form_statement_excel, name='pf_ecr_form_statement_excel'),

    



]