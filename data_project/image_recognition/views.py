from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import FileUploaded
from .file_functions import upload_file_handle


def index(request):
    return HttpResponse('heellowowjf')


def files(request):
    if request.method == 'POST':
        form = FileUploaded(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            request.FILES['file'].read()

            return render(request, 'home.html', {'f': request, 'form': form, 'img':request.FILES['file']})
    else:
        form = FileUploaded()
    return render(request, 'home.html', {'f': request, 'form': form})