from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from .models import Show
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CreateShowForm, UpdateShowForm

# Create your views here.
def index(request):
    return redirect('show-list')

def view_shows(request):
    shows = Show.objects.all().order_by('title')

    context = {
        'shows' : shows,
    }

    return render(request, 'shows/show_list.html', context)

class ShowCreateView(CreateView):
    model = Show
    form_class = CreateShowForm
    success_url = reverse_lazy('show-list')

class ShowUpdateView(UpdateView):
    model = Show
    form_class = UpdateShowForm
    def get_success_url(self):
        # Assuming 'show-detail' is the name of your detail view
        # and 'pk' is the primary key field of your Show model
        return reverse('show-details', kwargs={'pk': self.object.pk})

class ShowDeleteView(DeleteView):
    model = Show
    success_url = reverse_lazy('show-list')

def show_details(request, pk):
    show = get_object_or_404(Show, pk=pk)
    context = {
        'show' : show,
    }
    return render(request, 'shows/show_details.html', context)