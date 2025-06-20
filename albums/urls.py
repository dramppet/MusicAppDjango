from django.urls import path,include

from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='create-album'),
    path('<int:id>/', include([
        path('edit', views.AlbumEditView.as_view(), name='edit-album'),
        path('details', views.AlbumDetailView.as_view(), name='album-details'),
    ])),
]