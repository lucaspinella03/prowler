from contextvars import Context
from django.shortcuts import render, redirect

from .models import entry
from .forms import entryForm
# Create your views here.

def prowler_entry(request):
    """The home page for learning log."""
    entries = entry.objects.order_by('-date_added')
    context = {'entries': entries}
    return render(request,'prowler_post/prowler_entry.html', context)

def new_prowler_entry(request):
    if request.method != "POST":
        form = entryForm()
    else:
        form = entryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('prowler_post:prowler_entry')
    context = {'form': form}
    return render(request,'prowler_post/new_prowler_entry.html', context)