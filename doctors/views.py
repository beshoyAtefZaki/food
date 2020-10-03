from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import DoctorProfile
# Create your views here.
from django.contrib.auth import authenticate, login
@login_required(login_url='/logindc/')
def profile_page(request):
	doctor = None
	if request.user.is_authenticated : 
		
		doctor = DoctorProfile.objects.get(user=request.user)

		return render(request,'home.html',{'doctor':doctor})
	return render(request,'home.html')





def loginpage(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None :
			login(request ,user)
			return redirect('profile')

		
	return render(request ,'login.html' )