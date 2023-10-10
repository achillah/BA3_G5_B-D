from django.urls import path
from .views import RequestListView, RequestDetailView, RequestUpdateView, RequestDeleteView
from . import views # Le "." désigne le fichier courant


# Liste de chemins qui a été importée
urlpatterns = [
    path('', RequestListView.as_view(), name='blog-home'), # localhost:8000/blog/
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request-detail'), #affiche les détails d'une Request
    #pk = primary key --> exemple : Request/1 = Request avec l'id 1, le int: sert à dire que le pk est de type int afin d'éviter que qlq mette un string par exemple
    path('request/<int:pk>/update/', RequestUpdateView.as_view(), name='request-update'), #modifier une Request
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request-delete'), #supprimer une Request
    path('request/new/', views.create_request, name='request-create'), #creation d'une requête
    path('about/', views.about, name='blog-about'), # localhost:8000/about/
    path('admin_panel/', views.admin_panel, name='admin-panel'),
    path('admin_panel/create_user/', views.create_account, name='create-user'),
    path('update_user/<int:pk>/', views.update_account, name='update-user'),
    #path('user/<int:pk>/', UserDetailView.as_view(), name='detail-user'),


]