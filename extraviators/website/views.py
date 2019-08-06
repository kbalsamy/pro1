from django.shortcuts import render

# Create your views here.


def homePage_view(request):

    return render(request, 'website/home.html',)


def pageNavigation_view(request):

    context = {}

    path_params = {'/pets': 'website/pets.html',
                   '/excessbaggage': 'website/baggage.html',
                   '/repatriations': 'website/repatriations.html',
                   '/contact': 'website/contact.html'}

    if request.path in path_params.keys():

        return render(request, path_params[request.path], context)
