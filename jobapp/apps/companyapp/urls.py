from django.urls import path
from . import views

app_name = "companyapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("createCompany/", views.createCompany, name="createCompany"),
    # TODO: change this to dynamic url
    path("companyId/", views.companyProfile, name="companyProfile"),
    path("myCompany/jobListings", views.companyJobList, name="companyJobList"),
    path("myCompany/jobListings/createJob", views.createJob, name="createJob"),
    path("myCompany/jobListings/editJob/<int:job_id>/", views.createJob, name="editJob"),
    path("myCompany/jobListings/deleteJob/<int:job_id>/", views.deleteJob, name="deleteJob"),
    path("myCompany/jobListings/jobApplicants/<int:job_id>/", views.jobApplicants, name="jobApplicants"),
    path("myCompany/applicants", views.companyApplicants, name="companyApplicants"),
    path("myCompany/", views.companyProfileSettings, name="companyProfileSettings")
]
