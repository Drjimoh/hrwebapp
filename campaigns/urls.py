from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required



app_name = 'campaigns'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('campaign', login_required(views.CampaignView.as_view()), name='campaign'),
    #path('results/', views.ResultsView.as_view(), name='results'),
    path('results/', views.results, name='results'),
]
