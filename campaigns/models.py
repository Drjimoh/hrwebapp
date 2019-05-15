from django.db import models
import json


class Campaign(models.Model):
	campaignTitle = models.CharField('campaignTitle', max_length=500, blank=True)
	amountRaised = models.CharField('amountRaised', max_length=100, blank=True)
	goal = models.CharField(max_length=100, blank=True)
	currencyType = models.CharField('currencyType', max_length=100, blank=True)
	endDate = models.CharField('endDate', max_length=100, blank=True)
	numberContributors =models.CharField('numberContributors', max_length=100, blank=True)
	story = models.TextField(blank=True)
	url = models.CharField(max_length=200, blank=True)


	def __str__(self):
		return str(self.campaignTitle) + ' ' + str(self.amountRaised)


class Category(models.Model):
	category = models.CharField(max_length=200, blank=False, null=False)

	def __str__(self):
		return self.category

class Job(models.Model):
	title = models.CharField(max_length=300, blank=False, null=False)
	location = models.CharField(max_length=200, blank=False, null=False)
	category = models.ForeignKey(Category(), on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title