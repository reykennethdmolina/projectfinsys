from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from . models import Companyparameter
from customertype.models import Customertype
from creditterm.models import Creditterm
from currency.models import Currency
from bankaccount.models import Bankaccount
from industry.models import Industry
import datetime


# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Companyparameter
    template_name = 'companyparameter/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Companyparameter.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Companyparameter
    template_name = 'companyparameter/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Companyparameter
    template_name = 'companyparameter/create.html'
    fields = ['code', 'description', 'address', 'telno1', 'telno2', 'zipcode', 'contactperson_acctg1',
              'contactperson_acctg2', 'contactperson_it1', 'contactperson_it2', 'contactperson_other1',
              'contactperson_other2', 'sssnum', 'tinnum', ''
              'tin', 'pagerno', 'payterms', 'creditlimit', 'creditstatus', 'creditrating', 'contactperson',
              'contactposition', 'contactemail', 'remarks', 'multiplestatus', 'beg_amount', 'beg_code', 'beg_date',
              'end_amount', 'end_code', 'end_date', 'bankaccount', 'creditterm', 'currency', 'customertype', 'industry']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('customer.add_customer'):
            raise Http404
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/customer')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['customertype'] = Customertype.objects.filter(isdeleted=0).order_by('description')
        context['creditterm'] = Creditterm.objects.filter(isdeleted=0).order_by('description')
        context['currency'] = Currency.objects.filter(isdeleted=0).order_by('description')
        context['bankaccount'] = Bankaccount.objects.filter(isdeleted=0).order_by('bank')
        context['industry'] = Industry.objects.filter(isdeleted=0).order_by('description')
        return context


# @method_decorator(login_required, name='dispatch')
# class UpdateView(UpdateView):
#     model = Customer
#     template_name = 'customer/edit.html'
#     fields = ['code', 'name', 'address1', 'address2', 'address3', 'telno1', 'telno2', 'telno3', 'faxno1', 'faxno2',
#               'tin', 'pagerno', 'payterms', 'creditlimit', 'creditstatus', 'creditrating', 'contactperson',
#               'contactposition', 'contactemail', 'remarks', 'multiplestatus', 'beg_amount', 'beg_code', 'beg_date',
#               'end_amount', 'end_code', 'end_date', 'bankaccount', 'creditterm', 'currency', 'customertype', 'industry']
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.has_perm('customer.change_customer'):
#             raise Http404
#         return super(UpdateView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.enterby = self.request.user
#         self.object.modifyby = self.request.user
#         self.object.save()
#         return HttpResponseRedirect('/customer')
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateView, self).get_context_data(**kwargs)
#         context['customertype'] = Customertype.objects.filter(isdeleted=0).order_by('description')
#         context['creditterm'] = Creditterm.objects.filter(isdeleted=0).order_by('description')
#         context['currency'] = Currency.objects.filter(isdeleted=0).order_by('description')
#         context['bankaccount'] = Bankaccount.objects.filter(isdeleted=0).order_by('bank')
#         context['industry'] = Industry.objects.filter(isdeleted=0).order_by('description')
#         return context
#
#
# @method_decorator(login_required, name='dispatch')
# class DeleteView(DeleteView):
#     model = Customer
#     template_name = 'customer/delete.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.has_perm('customer.delete_customer'):
#             raise Http404
#         return super(DeleteView, self).dispatch(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.modifyby = self.request.user
#         self.object.modifydate = datetime.datetime.now()
#         self.object.isdeleted = 1
#         self.object.status = 'I'
#         self.object.save()
#         return HttpResponseRedirect('/customer')

