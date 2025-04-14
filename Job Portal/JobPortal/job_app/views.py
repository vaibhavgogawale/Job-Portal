
from django.shortcuts import render,redirect
from .forms import UserRegisterForm, AddITJobs, UpdateITJobs
from .models import ITjobs
from django.contrib.auth.decorators import login_required


# Create your views here.
# password = admin@123


def index(request):
    return render(request, 'index.html')


def user_register_view(request):
    if request.method == "POST":
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/login')
    else:
        forms = UserRegisterForm()

    return render(request, 'user.html', {'forms':forms})


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def add_it_jobs(request):
    if request.method == "POST":

        # print(request.POST or request.FILES)
        it_forms = AddITJobs(request.POST, request.FILES)

        if it_forms.is_valid():
            it_forms.save()
            return redirect('/view_it_jobs')

    else:
        it_forms = AddITJobs()

    return render(request, 'add_it_jobs.html', {'it_forms':it_forms})


# @login_required(login_url='login')
def view_it_jobs(request):
    data = ITjobs.objects.all()
    return render(request, 'view_it_jobs.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):
    id = ITjobs.objects.get(pk=id)
    id.delete()
    return redirect('/view_it_jobs')


@login_required(login_url='login')
def update_it_jobs(request, id):
    data = ITjobs.objects.get(pk=id)
    it_form = UpdateITJobs(instance=data)

    if request.method == "POST":
        it_form = UpdateITJobs(request.POST, instance=data)

        if it_form.is_valid():
            it_form.save()
            return redirect('/view_it_jobs')

    else:
        it_form = UpdateITJobs(instance=data)

    return render(request, 'update_it.html', {'it_form':it_form})




# def image_view(request):
#     img_form = AddImage()
#
#     if request.method == "POST":
#         img_form = AddImage(request.POST, request.FILES)
#         if img_form.is_valid():
#             img_form.save()
#
#     return render(request, 'image_view.html',{'img_form':img_form})
