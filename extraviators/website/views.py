from django.shortcuts import render, redirect
from .forms import ExcessBaggageForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def homePage_view(request):

  return render(request, 'website/home.html',)


def pageNavigation_view(request):

  context = {'bagform': ExcessBaggageForm}

  path_params = {'/pets': 'website/pets.html',
                 '/excessbaggage': 'website/baggage.html',
                 '/repatriations': 'website/repatriations.html',
                 '/contact': 'website/contact.html', }

  if request.path in path_params.keys():

    return render(request, path_params[request.path], context)


@csrf_exempt
def processPostView(request):

  form = ExcessBaggageForm(request.POST)
  if form.is_valid():
    form.save()
    return JsonResponse({'result': 'Success'})
  else:
    return JsonResponse({'result': 'Error'})
