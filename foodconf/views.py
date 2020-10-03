from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Createfrom your views here.
from .models import Unit
from django.core.paginator import Paginator
from .serializers import AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





@login_required(login_url='/logindc/')
def home(request , itm=None):
	units = Unit.objects.all() 
	if request.GET.get('itm') :
		kwrd = request.GET.get('itm')
		units = Unit.objects.filter(description__icontains=kwrd)	
		
	
	home = 'home.html'
	return render(request ,home ,{'units' : units})





def admin_home(request):


	return render(request , 'starter.html')




def api_test_view(request):
	snippets = Unit.objects.all()
	serializer = AccountSerializer(snippets, many=True)
	return render( request,'api-view.html' ,{'data':serializer.data})

class UnitsList(APIView):
	template_name = 'api-view.html'

	queryset = Unit.objects.all()
	def get(self, request, format=None):
		snippets = Unit.objects.all()
		serializer = AccountSerializer(snippets, many=True)
		return Response(serializer.data)