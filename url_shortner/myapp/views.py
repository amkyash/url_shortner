from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LongToShort

def hello_world(request):
	return HttpResponse("Hello world!")


def home_page(request):
	context = {
		"submitted": False,
		"error": False
	}

	if request.method == 'POST':
		data = request.POST 				# dict
		long_url = data['longurl']
		custom_name = data['custom_name']

		try:
			# CREATE
			obj = LongToShort(long_url = long_url, short_url = custom_name)
			obj.save()

			# READ
			date = obj.date
			clicks = obj.clicks

			context["long_url"] = long_url
			context["short_url"] = request.build_absolute_uri() + custom_name
			context["date"] = date
			context["clicks"] = clicks
			context["submitted"] = True

		except:
			context["error"] = True

	return render(request, "index.html", context)



def redirect_url(request, short_url):
	row = LongToShort.objects.filter(short_url = short_url)

	if len(row) == 0:
		return HttpResponse("No such short url exist")

	obj = row[0]
	long_url = obj.long_url
#meta
	# print(request.META)
	d=request.META
	# obj.os.append(d["OS"])
	# obj.os=d["OS"]
	# os=obj.os
	# print(os)
	

	obj.clicks = obj.clicks + 1
	obj.save()

	return redirect(long_url)


def task(request):

	context = {
		"my_name": "John",
		"x": 15
	}
	return render(request, "test.html", context)


def all_analytics(request):

	rows = LongToShort.objects.all()

	context = {
		"rows": rows
	}
	return render(request, "all-analytics.html", context)
def analy(request, short_url):
	
	row = LongToShort.objects.filter(short_url = short_url)
	context={}
	if len(row)==0:
		return HttpResponse("No such short url exists")	
	obj=row[0]
	# oss={}
	# for i in obj.os:
	# 	oss[i]=oss.get(i,0)+1
	# for i,j in oss.items():
	# 	context["os"]=i
	# 	context['clicky']=j
	# context["OS"]=obj.os
	context["long_url"] = obj.long_url
	context["short_url"] = obj.short_url
	context["date"] = obj.date
	context["clicks"] = obj.clicks
	
	# print(context["OS"])
	return render(request, "analytics.html",context)

