from django.shortcuts import render

# Create your views here.
def create_home(request):
    return render(request, 'index.html')