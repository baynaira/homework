from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NameForm






def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect(reverse('greet:greet_user', kwargs={'name': name}))
    else:
        form = NameForm()

    return render(request, 'name_form.html', {'form': form})
