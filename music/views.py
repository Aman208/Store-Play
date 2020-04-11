from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView , View
from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse_lazy
from .models import Album 
from django.contrib.auth import authenticate , login ,logout
from .forms import LoginForm ,UserForm 

################## Album ####################
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(View):
    
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs['pk'])
        context = {'album': album}
        return render(request, 'music/album_detail.html', context)

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):

        form = self.form_class(None)

        return render(request, self.template_name,{ 'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()


            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('index')



        else:
            return render(request, self.template_name, {'form': form})


def LogOut(request):
    form=LoginForm(None)
    logout(request)
    return redirect('login')


class UserLogin(View):

    form_class=LoginForm

    template_name='music/login.html'

    def get(self,request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self,request):
            form = self.form_class(None)
            username = request.POST['username']
            password = request.POST['password']

            user=authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
            else:
                return render(request, self.template_name, {'form': form})    
    