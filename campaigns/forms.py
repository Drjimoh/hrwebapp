from . models import Job
from django.forms import ModelForm


class JobSearchForm(ModelForm):

	class Meta:
		model = Job
		fields = '__all__'