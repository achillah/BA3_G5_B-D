from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Request
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserCreationForm,RequestCreationForm, UserCreationUpdateForm


# Fichier qui va contenir toutes les vues de notre application

# la fonction home prend en paramètre une requête http --> return une réponse http contenant un code html
@login_required
def home(request):
    context = {
        'requests' : Request.objects.all()
    }
    return render(request, 'blog/home.html', context) #requête en paramètre, nomDuRepertoire/nomDuTemplate

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'The request has been created successfully !')
            return redirect('blog-home')
    else:
        form = RequestCreationForm()

    return render(request, 'blog/request_form.html', {'form':form})

@login_required
def admin_panel(request):
    context = {
        'users' : User.objects.all()
    }

    return render(request, 'blog/admin_panel.html', context)

@login_required
def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('admin-panel') #une fois le compte créer, redirection vers la page de login
    else:
        form = UserCreationForm()

    return render(request, 'blog/create_user.html', {'form':form})


#méthode concernant la modification des utilisateurs
@login_required
def update_account(request, pk):
    user = User.objects.get(id=pk)
    u_form = UserCreationUpdateForm(instance=user)

    if request.method == 'POST':
        form = UserCreationUpdateForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'The account has been modified !')
            return redirect('admin-panel') #redirection vers la page d'admin


    context = {
        'u_form': u_form,
    }

    return render(request,'blog/user_account_update.html', context)



class RequestListView(LoginRequiredMixin, ListView): #affichage de tous les requests (home.html)
    model = Request
    template_name = 'blog/home.html'#<app>/<model>_<viewtype>.html
    context_object_name = 'requests'
    ordering = ['-date_requested'] #permet d'afficher les requests du plus récent au plus ancien (grâce au '-' devant date_Requested)
    #paginate_by = 5 #nombre de requests qui vont être affichés sur une page

class RequestDetailView(LoginRequiredMixin, DetailView): #quand on clique sur un Request, le Request va être afficher de manière bcp + détaillée
    model = Request

class RequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # création d'un Request
    model = Request
    fields = ['title','reference_number','start_date','deadline','priority' ,'budget', 'status','faction', 'consultant', 'main_skills', 'consultant_level', 'attachment']

    def form_valid(self, form):
        form.instance.author = self.request.user  # auteur de la requête = l'utilisateur actuellement connecté
        return super().form_valid(form)

    def test_func(self):
        Request = self.get_object() #enregistre le Request que l'on veut actuellement modifier
        if self.request.user.is_staff: #si l'utilsateur connecté correspond à l'auteur du Request alors il peut modifier le Request (return True)
            return True
        return False

class RequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #quand on clique sur un Request, le Request va être afficher de manière bcp + détaillée
    model = Request
    success_url = '/'

    def test_func(self):
        Request = self.get_object() #enregistre le Request que l'on veut actuellement supprimer
        if self.request.user.is_staff: #si l'utilsateur connecté correspond à l'auteur du Request alors il peut supprimer le Request (return True)
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title' : 'My About Page'})

