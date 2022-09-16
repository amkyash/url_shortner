from django.db import models
# from django_mysql.models import ListCharField
# Create your models here.
# from binder.models import Dictionary
class LongToShort(models.Model):
	long_url=models.URLField(max_length=250)
	short_url=models.CharField(max_length=50,unique=True)
	date=models.DateField(auto_now_add=True)
	clicks=models.IntegerField(default=0)
	# os=models.CharField(max_length=50)