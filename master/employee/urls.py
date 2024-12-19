from django.urls import path
from .views import EmployeeExportView
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import (
    LeaderListView, LeaderCreateView, LeaderUpdateView, LeaderDeleteView,
    LeaderCommissionWagesListView, LeaderCommissionWagesCreateView,
    LeaderCommissionWagesUpdateView, LeaderCommissionWagesDeleteView, LeaderDetailView,
    CommissionAttendanceView,
    ExtraDaysCommissionView,
    LeaderUploadView, LeaderCommissionWagesUploadView, EmployeeLeaderUploadView, NonPFCommissionAttendanceView
)

urlpatterns = [

# URLs for Employee model
    path('master_creation/', views.master_creation, name='master_creation'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee_idcard/<int:pk>/', views.employee_idcard, name='employee_idcard'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employees/inactive/', views.InactiveEmployeeListView.as_view(), name='inactive_employee_list'),
    path('employee/pfesi/upload/', views.employee_pfesi_upload_view, name='employee_pfesi_upload_view'),
    #####################################
    path('employees/export/', EmployeeExportView.as_view(), name='employee_export'),
    path('employees/upload-in-excel/', views.upload_employee_data, name='employee_upload'),
    path('upload_employee_dates/upload-in-excel/', views.upload_employee_dates, name='upload_employee_dates'),
    ###########
     # Designation URLs
    path('designations/', views.designation_list, name='designation_list'),
    path('designations/create/', views.designation_create, name='designation_create'),
    path('designations/edit/<int:pk>/', views.designation_edit, name='designation_edit'),
    path('designations/delete/<int:pk>/', views.designation_delete, name='designation_delete'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

     # Wages URLs
    
    path('wages_reports/', views.wages_reports, name='wages_reports'),
    path('wages/new/', views.wages_create_view, name='wages_create'),
    path('wages/<int:wage_id>/edit/', views.wages_update_view, name='wages_update'),
    path('wages/delete/<int:wage_id>/', views.wages_delete_view, name='wages_delete_view'),
    path('wages/', views.wages_list_view, name='wages_list'),
    path('upload-wages/', views.upload_wages, name='upload_wages'),

    ############
    path('incentives/', views.incentive_list_view, name='incentive_list'),
    path('incentives/new/', views.incentive_create_view, name='incentive_create'),
    path('incentives/<int:incentive_id>/edit/', views.incentive_update_view, name='incentive_update'),
    path('incentives/<int:incentive_id>/delete/', views.incentive_delete_view, name='incentive_delete'),
    ###########
    path('deductions/', views.deduction_list_view, name='deduction_list'),
    path('deductions/new/', views.deduction_create_view, name='deduction_create'),
    path('deductions/<int:deduction_id>/edit/', views.deduction_update_view, name='deduction_update'),
    path('deductions/<int:deduction_id>/delete/', views.deduction_delete_view, name='deduction_delete'),
    path('deduction_filterd_list/', views.deduction_filterd_list, name='deduction_filterd_list'),
    #upload deductions 
    path('bulk_upload_deductions/', views.bulk_upload_deductions, name='bulk_upload_deductions'),
    ###########
    
    path('employee_pf_salary_for_cover/', views.employee_pf_salary_for_cover, name='employee_pf_salary_for_cover'),

    path('salary_reports/', views.salary_reports, name='salary_reports'),
    path('salary_abstract_reports/', views.salary_abstract_reports, name='salary_abstract_reports'),
    



    path('non_pf_salary_view/', views.non_pf_salary_view, name='non_pf_salary_view'),
    path('non-pf-salary/download/excel/', views.non_pf_salary_download_excel, name='non_pf_salary_download_excel'),
    path('non-pf-salary/download/pdf/', views.non_pf_salary_download_pdf, name='non_pf_salary_download_pdf'),
    path('non_pf_salary_details_view/', views.non_pf_salary_details_view, name='non_pf_salary_details_view'),
    path('extra_days_salary_view/', views.extra_days_salary_view, name='extra_days_salary_view'),
    path('extra_salary_download_excel/', views.extra_salary_download_excel, name='extra_salary_download_excel'),
    path('extra_salary_download_pdf/', views.extra_salary_download_pdf, name='extra_salary_download_pdf'),
    path('extra_salary_details_view/', views.extra_salary_details_view, name='extra_salary_details_view'),

   

    path('non_pf_salary_department_view/', views.non_pf_salary_department_view, name='non_pf_salary_department_view'),
    




    
    ###########

    # Leader URLs
    path('leaders/', LeaderListView.as_view(), name='leader_list'),
    path('leaders/add/', LeaderCreateView.as_view(), name='leader_create'),
    path('leaders/<int:pk>/edit/', LeaderUpdateView.as_view(), name='leader_edit'),
    path('leaders/<int:pk>/delete/', LeaderDeleteView.as_view(), name='leader_delete'),
    path('leader/<int:pk>/', LeaderDetailView.as_view(), name='leader_detail'),
    path('leader/<int:pk>/export/', views.export_leader_to_excel, name='leader_export_excel'),

    
    # LeaderCommissionWages URLs
    path('commission-wages/', LeaderCommissionWagesListView.as_view(), name='commission_wages_list'),
    path('commission-wages/add/', LeaderCommissionWagesCreateView.as_view(), name='commission_wages_create'),
    path('commission-wages/<int:pk>/update/', LeaderCommissionWagesUpdateView.as_view(), name='commission_wages_update'),
    path('commission-wages/<int:pk>/delete/', LeaderCommissionWagesDeleteView.as_view(), name='commission_wages_delete'),



    path('commission-attendance/', CommissionAttendanceView.as_view(), name='commission_attendance'),
    path('non_pf_commission-attendance/', NonPFCommissionAttendanceView.as_view(), name='nonpf_commission_attendance'),
    
    path('commission-attendance/download/', CommissionAttendanceView.as_view(), name='download_commission_attendance'),
    path('extra-days-commission/', ExtraDaysCommissionView.as_view(), name='extra_days_commission_view'),


    #upload path
    path('leader/upload/', LeaderUploadView.as_view(), name='leader_upload'),
    path('leader_commission_wages/upload/', LeaderCommissionWagesUploadView.as_view(), name='leader_commission_wages_upload'),
    path('employee/leader/upload/', EmployeeLeaderUploadView.as_view(), name='employee_leader_upload'),




     #nonpfabstract
    path('category-department-salary/', views.category_totals_view, name='category_department_salary_view'),
    path('export-department-totals/', views.export_category_totals_excel, name='export_department_totals'),
    


    path('extra_days_department_totals_view/', views.extra_days_department_totals_view, name='extra_days_department_totals_view'),
    path('extra_days_export_department_totals_excel/', views.extra_days_export_department_totals_excel, name='extra_days_export_department_totals_excel'),



    #nonpfabstract save
    path('save-non-pf-abstract/', views.save_non_pf_abstract, name='save_non_pf_abstract'),
    #extradaysabstract save
    path('save-extra-days-abstract/', views.save_extra_days_abstract, name='save_extra_days_abstract'),



    #reports
    path('reports_list/', views.reports_list, name='reports_list'),
    path('extradays_abstract_list/', views.extradays_abstract_list, name='extradays_abstract_list'),
    path('extradays_abstract_details/<str:month>/<int:year>/', views.extradays_abstract_details,  name='extradays_abstract_details'),
    path('nonpf_abstract_list/', views.nonpf_abstract_list,  name='nonpf_abstract_list'),
    path('nonpf_abstract_details/<str:month>/<int:year>/', views.nonpf_abstract_details,  name='nonpf_abstract_details'),

    # URL for the PFAbstract list view
    path('pfabstract_list/', views.pfabstract_list, name='pfabstract_list'),

    # URL for the PFAbstract detail view
    path('pfabstract/<str:month>/<int:year>/', views.pfabstract_details, name='pfabstract_details'),





    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)