from django.shortcuts import render

# Create your views here.
def pollworker(request):
    return render(request, 'pollworker.html')

def get_the_facts(request):
    return render(request, 'getthefacts.html')