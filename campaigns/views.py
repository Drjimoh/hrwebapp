from django.shortcuts import render
from rest_framework.views import  APIView
from .models import Campaign, Category, Job
from .serializers import CampaignSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
from .forms import JobSearchForm
from django.forms import ModelForm


class CampaignView(APIView):

	def get(self, response):
		campaigns = Campaign.objects.all()
		serializer = CampaignSerializer(campaigns, many=True)
		return Response(serializer.data)

	def post(self, response):
		serializer = CampaignSerializer(data=response.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class IndexView(generic.ListView):
	template_name = 'campaigns/index.html'
	model = Category
	form = JobSearchForm()
	contexts = {'form':form}

	def get_queryset(self):
		categories = Category.objects.all() 
		return categories






def results(request):
	if request.method == 'GET':
		results = Job.objects.filter(
			category__category=request.GET['Category'], 
			title__icontains=request.GET['keywords'],
			 location__icontains=request.GET['location'])
	return render(request, 'campaigns/results.html', {'results':results})
