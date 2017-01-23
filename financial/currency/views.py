from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from . models import Currency
import datetime


# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Currency
    template_name = 'currency/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Currency.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Currency
    template_name = 'currency/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Currency
    template_name = 'currency/create.html'
    fields = ['code', 'symbol', 'description', 'country']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('currency.add_currency'):
            raise Http404
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/currency')


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Currency
    template_name = 'currency/edit.html'
    fields = ['code', 'symbol', 'description', 'country']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('currency.change_currency'):
            raise Http404
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/currency')


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Currency
    template_name = 'currency/delete.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('currency.delete_currency'):
            raise Http404
        return super(DeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/currency')
