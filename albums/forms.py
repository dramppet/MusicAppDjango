from django import forms

from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']

class AlbumCreateForm(AlbumBaseForm):
    ...

class AlbumEditForm(AlbumBaseForm):
    ...