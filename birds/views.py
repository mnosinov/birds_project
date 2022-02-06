from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Bird
from .forms import BirdFormSet


class BirdListView(ListView):
    model = Bird
    template_name = 'birds/bird_list.html'


class BirdAddView(TemplateView):
    template_name = 'birds/add_bird.html'

    def get(self, *args, **kwargs):
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})

    def post(self, *args, **kwargs):
        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('bird_list'))

        return self.render_to_response({'bird_formset': formset})
