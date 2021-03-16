from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from main_gusto.models import Message
from main_gusto.models import Category
from main_gusto.forms import CategoryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import GroupRequiredMixin

def is_member(user):
    return user.groups.filter(name='manager').exists() or \
           user.is_staff


# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_messages(request):
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={'messages':messages})



def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')

def list_of_categories(request):
    items = Category.objects.all().order_by("category_order")
    return render(request,"categories.html", context={"items": items})


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно создана!'

class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)

class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно добавлена!'
