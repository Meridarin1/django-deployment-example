from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'basic_app/index.html')

def other(request):
    data = "this is filtred by Djagno"
    data_dict = {'insert': data,'number':100}
    return render(request, 'basic_app/other.html', context=data_dict)

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')