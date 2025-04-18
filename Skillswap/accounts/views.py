from django.shortcuts import redirect, render
from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
class Register(View):
    template_name = 'registration/register.html'
    
    def get(self,request):
        context = {
            'form':CustomUserCreationForm()

        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user) 
            return redirect('home')
        context = {
        'form' : form
        }
        return render(request,self.template_name,context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')