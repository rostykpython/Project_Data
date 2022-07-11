from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import FileImage, CustomCreationForm, LoginForm
from .models import FileUploaded
from pathlib import Path
from .file_functions import open_file_handler, get_class_information
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login/')
def image_recognition(request):

    if request.method == 'POST':
        form = FileImage(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['image']

            model_file = FileUploaded(user=request.user, image=file)
            if not Path(f'./media/user_{request.user.id}').exists():
                model_file.save()

            user_files = list(Path(f'./media/user_{request.user.id}').iterdir())
            quantity_of_files = len(user_files)

            if quantity_of_files > 3 and user_files[0].name != str(file):
                user_files[0].unlink()

            for item in user_files:
                if item.name == str(file):
                    prediction_array = open_file_handler(f'./media/user_{request.user.id}/{file}',
                                                         model_name=request.POST['selection'],
                                                         request=request)

                    prediction = prediction_array[-1][0]
                    return render(
                        request, 'images_nn.html',
                        {
                            'form': form,
                            'img_path': f'./media/user_{request.user.id}/{file}',
                            'pred': prediction,
                            'pred_img': f'./static/image_labels/{prediction}.png',
                            'description': get_class_information(prediction),
                            'selected_model': request.POST['selection']
                        }
                    )

            model_file.save()
            prediction_array = open_file_handler(f'./media/user_{request.user.id}/{file}',
                                                 model_name=request.POST['selection'],
                                                 request=request)

            prediction = prediction_array[-1][0]
            return render(request, 'images_nn.html',
                          {
                              'form': form,
                              'img_path': f'./media/user_{request.user.id}/{file}',
                              'pred': prediction,
                              'pred_img': f'./static/image_labels/{prediction}.png',
                              'description': get_class_information(prediction),
                              'selected_model': request.POST['selection']
                          }
                          )
    else:
        form = FileImage()
    return render(request, 'images_nn.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = './login.html'
    fields = '__all__'

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = './register.html'
    form_class = CustomCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(request=self.request, user=user)
        return super(RegisterPage, self).form_valid(form)
