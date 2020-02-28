from django.shortcuts import render, redirect
from .models import Contestant
from .forms import EntryForm


def home(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        contestants = Contestant.objects.order_by('-points')
        if form.is_valid():
            contestant = Contestant()
            twitter_handle = form.cleaned_data.get('twitter_handle')
            email = form.cleaned_data.get('email')
            contestant.twitter_handle = twitter_handle
            contestant.email = email
            contestant.save()
            return redirect('/')
    else:
        form = EntryForm()
        contestants = Contestant.objects.order_by('-points')
    context = {
        'form': form,
        'contestants': contestants,
    }

    return render(request, "play_ground/home.html", context)
