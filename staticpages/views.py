from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from csvfile.models import StateInformation

# Create your views here.
def pollworker(request):
    return render(request, 'pollworker.html')

def get_the_facts(request):
    return render(request, 'getthefacts.html')

def voting_view(request, state_name):
    state_info = model_to_dict(StateInformation.objects.get(name=state_name))
    return render(request, 'stateinfo.html', state_info)