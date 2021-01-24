from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def edit(request, list_id):
    pass

def complete(request, list_id):
    status = List.objects.get(pk=list_id)
    status.completed = True
    status.save()
    return redirect('home')


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'An Item has been removed from your List!')
    return redirect('home')


def add_item(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListForm()
        messages.success(request, 'An Item has been added to your List!')
    return render(request, 'add_item.html', {'form': form,})


def home(request):
    from todo_list.app_name import app_name
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items, 'app_name': app_name})

    


def about(request):
    from todo_list.app_name import app_name
    return render(request, 'about.html', {'app_name': app_name})