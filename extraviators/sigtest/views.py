from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def sigtesthome(request):

    return render(request, 'website/testpage1.html')


@csrf_exempt
def ajaxrequest(request):
    print('checked')
    return JsonResponse({'result': 'sucesss'})
