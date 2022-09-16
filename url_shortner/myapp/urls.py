from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('', views.home_page),
    path('task', views.task),
    path('all-analytics', views.all_analytics),
    # path('short_url',vierws.analy),
    # path('analytics/slug:',views.analy),
    path('analytics/<slug:short_url>',views.analy),
    path('<slug:short_url>', views.redirect_url)
]
