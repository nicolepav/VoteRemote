from django.shortcuts import render
from home.models import state_key
# Create your views here.
def create_home(request):
    all_state_keys = state_key.objects.all()    
    return render(request, 'index.html', {"all_keys": all_state_keys} )