from django.shortcuts import render
from .forms import FileImage
from pathlib import Path
from .file_functions import open_file_handler
from .apps import ImageRecognitionConfig


def index(request):
    return render(request, 'home.html')


def image_recognition(request):
    print(request.GET, end='\n')
    print(request.POST, end='\n')
    print(request.FILES, end='\n')
    if request.method == 'POST':
        form = FileImage(request.POST, request.FILES)
        print('fff')
        if form.is_valid():
            file = request.FILES['file']
            print('fff')
            for item in Path('./media/upload').iterdir():
                if item.name == str(file):
                    return render(
                        request, 'images_nn.html',
                        {
                            'f': request,
                            'form': form,
                            'img_path': f'./media/upload/{file}',
                            'pred': open_file_handler(f'./media/upload/{file}',
                                                      model=ImageRecognitionConfig.pretrained_model)
                        }
                    )
            form.save()
            return render(request, 'images_nn.html',
                          {'f': request,
                           'form': form,
                           'img_path': f'./media/upload/{file}',
                           'pred': open_file_handler(f'./media/upload/{file}',
                                                     model=ImageRecognitionConfig.pretrained_model)
                           }
                          )
    else:
        form = FileImage()
    return render(request, 'images_nn.html', {'f': request, 'form': form})
