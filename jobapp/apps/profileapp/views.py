from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditForm, WorkHistoryForm, EducationForm
from django.shortcuts import render, redirect
from apps.jobsapp.models import WorkExperience
from django.core.exceptions import ValidationError


#retrieve current user data
def get_user_data(request):
    return {
        "email": request.user.email,
        "id": request.user.id,
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "profile_summary": request.user.profile_summary,
    }
   
# retrieve all the work experience of user
def get_user_work_experience(request):
    user = request.user.id
    work_experience = WorkExperience.objects.filter(user=user)
    return work_experience


@login_required(login_url="login")
def index(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)  # instance of the current user
        work_history_form = WorkHistoryForm(request.POST)  # Pass request.POST here, not just request
        education_form = EducationForm(request.POST)
        
        if form.is_valid():  # checking if there's an error
            try:
                form.save()  # update the data of the current user
                messages.success(request, 'Profile updated successfully.')
                return redirect('index')  # direct only to the profile again
            except Exception as e:
                messages.error(request, 'Profile update failed. An error occurred.')
        else:
            messages.error(request, 'Profile update failed. Please check the form.')

    else:
        form = EditForm(instance=request.user)
        work_history_form = WorkHistoryForm()  # Create a blank instance for rendering in the template
        education_form = EducationForm()

    # data of the current user to be displayed on the profile section
    template = "profile.html"
    user_data = get_user_data(request)
    work_experiences = get_user_work_experience(request)
    context = {
        "user_data": user_data, 
        "form": form, 
        "work_form": work_history_form,
        "work_experiences": work_experiences,
        "education":education_form,
        }
    
    return render(request, template, context)



def addWorkExp(request):
    if request.method == 'POST':
        work_history_form = WorkHistoryForm(request.POST)  # Pass request.POST here, not just request
        
        if work_history_form.is_valid():
            try:
                
                #work history form data field
                start_month = request.POST.get('started_month')
                start_year = request.POST.get('started_year')
                start_date = f"{start_month}, {start_year}"

                end_month = request.POST.get('end_month')
                end_year = request.POST.get('end_year')
                end_date = f"{end_month}, {end_year}"
                position = request.POST.get('position')
                company_name = request.POST.get('company_name')
                
                #add new data to the database
                work_experience = work_history_form.save(commit=False)
                work_experience.start_date = start_date
                work_experience.position = position
                work_experience.end_date = end_date
                work_experience.user = request.user
                work_experience.company_name = company_name
                
                work_experience.save() #add the new work experience
                
                messages.success(request, 'Work experience added successfully.')
                return redirect('index')
            except ValidationError as e:
                 messages.error(request, 'Profile update failed. An error occurred.')
                 print(e)
                 
    else:
        work_history_form = WorkHistoryForm()  # Create a blank instance for rendering in the template
        
        
    # data of the current user to be displayed on the profile section
    user_data = get_user_data(request)
    template = "profile.html"
    context = {"user_data": user_data, "work_form": work_history_form}
    return render(request, template, context)


def addEducation(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)  # instance of the current user
        work_history_form = WorkHistoryForm(request.POST)  # Pass request.POST here, not just request
        education_form = EducationForm(request.POST)
        
        if education_form.is_valid():
            try:
                #add new record of education
                new_education = education_form.save(commit=False)
                new_education.user = request.user
                new_education.save()

                messages.success(request, 'Education added successfully.')
                print(education_form.cleaned_data)
                return redirect('index')  # Redirect to the profile again
            except Exception as e:
                messages.error(request,'Education update failed')
                print(e)
                pass
            
    user_data = get_user_data(request)
    template = 'profile.html'
    work_experiences = get_user_work_experience(request)
    context = {
        "user_data": user_data, 
        "form": form, 
        "work_form": work_history_form,
        "work_experiences": work_experiences,
        "education":education_form,
        }
    
    return render(request,template,context)