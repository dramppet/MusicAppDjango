from django.urls import reverse_lazy
from django.views.generic import CreateView

from albums.forms import AlbumCreateForm
from albums.models import Album
from common.utils import get_profile


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url=reverse_lazy('home')
    template_name='album-add.html'

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)

