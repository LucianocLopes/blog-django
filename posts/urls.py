from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
]