# JIFB/urls.py (seu arquivo urls.py principal)

"""
URL configuration for lancode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include 



from users.views import (
    UserProfile,
    EditarUserProfile,
    BloquearPerfil,
    ApagarComentariosUserProfile,
    ExcluirComentario
    )

from base.views import (
    RedirectToHome,
    HomePage,
    NotFoundPage,
    LoginPage,
    LogoutUser,
    RegisterUser,
    QuemSomosPage

)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),

    # Base APP URLs
    path('', HomePage, name='home'),
    path('404', NotFoundPage, name='404'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('register/', RegisterUser, name='register'),
    path('quem-somos/', QuemSomosPage, name='quem_somos'),
    
   
    path('noticias/', include('news.urls')), 


    path('noticia/', RedirectToHome), 
    
    # Users APP URLs
    path('u/', RedirectToHome),
    path('u/<str:pk>', UserProfile, name='user'),
    path('u/editar/<str:pk>', EditarUserProfile, name='editar_user'),
    path('u/excluir/<str:pk>', ExcluirComentario, name='excluir-comentario'),
    path('u/apagar_comentarios/<str:pk>', ApagarComentariosUserProfile, name='apagar-comentarios'),
    path('u/bloquear/<str:pk>', BloquearPerfil, name='bloquear-user'),

     path('noticias/', include('news.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)