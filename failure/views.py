# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import Awaria

class AwariaList(ListView):
    model = Awaria
    ordering = ("status", "add_date")
    context_object_name = "awarie"
    paginate_by = 15

    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Zgłaszający').count() == 0, login_url='/dashboard'))
    def dispatch(self, *args, **kwargs):
        return super(AwariaList, self).dispatch(*args, **kwargs)

class AwariaCreate(CreateView):
    model = Awaria
    success_url = reverse_lazy('awarie_list')
    fields = ['description', 'maszyna', 'wydzial']
    template_name = 'awaria_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AwariaCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AwariaCreate, self).dispatch(*args, **kwargs)

class AwariaUpdate(UpdateView):
    model = Awaria
    success_url = reverse_lazy('awarie_list')
    fields = ['description', 'status', 'repair_date', 'remove_date', 'sur']
    template_name = 'awaria_form.html'

    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Zgłaszający').count() == 0, login_url='/dashboard'))
    def dispatch(self, *args, **kwargs):
        return super(AwariaUpdate, self).dispatch(*args, **kwargs)

@login_required
def awarie(request):
    awarie_list = Awaria.objects.filter(status__in=[1,2]).order_by('status','add_date')

    paginator = Paginator(awarie_list,15)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        awarie = paginator.page(page)
    except(EmptyPage, InvalidPage):
        awarie = paginator.page(paginator.num_pages)

    return render(request, 'awarie.html', {
        'awarie' : awarie
        })
        
@login_required
def awarie_all(request):

    awarie_all_list = Awaria.objects.all().order_by('status','-add_date')

    paginator = Paginator(awarie_all_list,15)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        awarie_all = paginator.page(page)
    except(EmptyPage, InvalidPage):
        awarie_all = paginator.page(paginator.num_pages)

    return render(request, 'awarie_all.html', {
        'awarie_all' : awarie_all
        })

@login_required
def ranking(request):

    ranking_list = Awaria.objects.all().order_by('status','-add_date')

    paginator = Paginator(ranking_list,15)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        ranking = paginator.page(page)
    except(EmptyPage, InvalidPage):
        ranking = paginator.page(paginator.num_pages)

    return render(request, 'ranking.html', {
        'ranking' : ranking
        })