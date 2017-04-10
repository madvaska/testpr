from django.shortcuts import render

# Create your views here.

def dep_list(request):
	return render(request, 'skud/dep_list.html', {})


