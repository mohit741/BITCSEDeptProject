from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegForm, UserForm, SCIForm, UnpaidScopusForm, PaidScopusForm, OthersJournalsForm
from .models import Profile, SCIJournals, UnpaidScopus, PaidScopus, OtherJournals
from .tables import SCITable, UserTable, UnpaidScopusTable, PaidScopusTable, OtherJournalTable
from django_tables2 import RequestConfig


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        return redirect('/login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        return render(request, 'registration/login.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/profile', {'user': user})
    else:
        return render(request, 'registration/login.html', {'err': 'User credentials not valid!'})


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        details_form = RegForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile.objects.get(user=user)
            details_form = RegForm(request.POST, instance=profile)
            details_form.save()
            login(request, user)
            return redirect('/profile')
    else:
        user_form = UserForm()
        details_form = RegForm()
    return render(request, 'register.html', {'user_form': user_form, 'details_form': details_form})


@login_required
def show_profile(request):
    if request.user.is_authenticated:
        other_user = None
        return render(request, 'profile.html', {'other_user': other_user})
    else:
        return redirect('/login')


def show_other_profile(request, username):
    if request.user.is_staff:
        other_user = User.objects.filter(username=username).first()
        return render(request, 'profile.html', {'other_user': other_user})
    else:
        return redirect('/profile')


def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        if request.method == 'POST':
            details_form = RegForm(request.POST, instance=profile)
            if details_form.is_valid():
                details_form.save()
                return redirect('/profile')
        else:
            details_form = RegForm(instance=profile)
            return render(request, 'update_profile.html', {'details_form': details_form, 'user': user})
    else:
        return redirect('/login')


def logout_user(request):
    logout(request)
    return redirect('/login')


def papers_view(request):
    if request.user.is_authenticated:
        user = request.user
        sci = SCITable(SCIJournals.objects.filter(user=user))
        RequestConfig(request).configure(sci)
        up = UnpaidScopusTable(UnpaidScopus.objects.filter(user=user))
        RequestConfig(request).configure(up)
        p = PaidScopusTable(PaidScopus.objects.filter(user=user))
        RequestConfig(request).configure(p)
        oj = OtherJournalTable(OtherJournals.objects.filter(user=user))
        RequestConfig(request).configure(oj)
        table = {'sci': sci, 'up': up, 'p': p, 'oj': oj}
        return render(request, 'papers_view.html', {'user': user, 'table': table})
    else:
        return redirect('/login')


def others_papers_view(request, user):
    if request.user.is_authenticated and request.user.is_staff:
        user = User.objects.get(username=user)
        sci = SCITable(SCIJournals.objects.filter(user=user))
        sci.exclude = ('edit', 'delete')
        RequestConfig(request).configure(sci)
        up = UnpaidScopusTable(UnpaidScopus.objects.filter(user=user))
        up.exclude = ('edit', 'delete')
        RequestConfig(request).configure(up)
        p = PaidScopusTable(PaidScopus.objects.filter(user=user))
        p.exclude = ('edit', 'delete')
        RequestConfig(request).configure(p)
        oj = OtherJournalTable(OtherJournals.objects.filter(user=user))
        oj.exclude = ('edit', 'delete')
        RequestConfig(request).configure(oj)
        table = {'sci': sci, 'up': up, 'p': p, 'oj': oj}
        user = request.user
        return render(request, 'other_papers_view.html', {'user': user, 'table': table})
    else:
        return redirect('/login')


def profiles_view(request):
    if request.user.is_staff:
        user = request.user
        users = Profile.objects.all()
        users = users.exclude(user=user)
        table = UserTable(users)
        RequestConfig(request).configure(table)
        return render(request, 'all_profiles.html', {'user': user, 'users_table': table})
    else:
        return redirect('/profile')


def add_papers(request, paper_type):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            if paper_type == 'SCI':
                papers_form = SCIForm(request.POST)
            elif paper_type == 'unpaid_scopus':
                papers_form = UnpaidScopusForm(request.POST)
            elif paper_type == 'paid_scopus':
                papers_form = PaidScopusForm(request.POST)
            else:
                papers_form = OthersJournalsForm(request.POST)
            if papers_form.is_valid():
                paper = papers_form.save(commit=False)
                paper.user = user
                paper.save()
            return redirect('/papers')
        else:
            if paper_type == 'SCI':
                papers_form = SCIForm()
            elif paper_type == 'unpaid_scopus':
                papers_form = UnpaidScopusForm()
            elif paper_type == 'paid_scopus':
                papers_form = PaidScopusForm()
            else:
                papers_form = OthersJournalsForm()
            return render(request, 'papers_edit.html',
                          {'papers_form': papers_form, 'user': user, 'paper_type': paper_type})
    else:
        return redirect('/login')


def edit_papers(request, paper_type, pk):
    if request.user.is_authenticated:
        user = request.user
        if paper_type == 'SCI':
            paper = SCIJournals.objects.filter(pk=pk).first()
        elif paper_type == 'unpaid_scopus':
            paper = UnpaidScopus.objects.filter(pk=pk).first()
        elif paper_type == 'paid_scopus':
            paper = PaidScopus.objects.filter(pk=pk).first()
        else:
            paper = OtherJournals.objects.filter(pk=pk).first()
        if request.method == 'POST':
            if paper_type == 'SCI':
                papers_form = SCIForm(request.POST, instance=paper)
            elif paper_type == 'unpaid_scopus':
                papers_form = UnpaidScopusForm(request.POST, instance=paper)
            elif paper_type == 'paid_scopus':
                papers_form = PaidScopusForm(request.POST, instance=paper)
            else:
                papers_form = OthersJournalsForm(request.POST, instance=paper)
            if papers_form.is_valid():
                papers_form.save()
            return redirect('/papers')
        else:
            if paper_type == 'SCI':
                papers_form = SCIForm(instance=paper)
            elif paper_type == 'unpaid_scopus':
                papers_form = UnpaidScopusForm(instance=paper)
            elif paper_type == 'paid_scopus':
                papers_form = PaidScopusForm(instance=paper)
            else:
                papers_form = OthersJournalsForm(instance=paper)
            return render(request, 'papers_edit.html',
                          {'papers_form': papers_form, 'user': user, 'paper_type': paper_type})
    else:
        return redirect('/login')


@login_required
def delete_papers(request, paper_type, pk):
    if request.method == 'GET':
        if paper_type == 'SCI':
            SCIJournals.objects.filter(pk=pk).delete()
        elif paper_type == 'unpaid_scopus':
            UnpaidScopus.objects.filter(pk=pk).delete()
        elif paper_type == 'paid_scopus':
            PaidScopus.objects.filter(pk=pk).delete()
        else:
            OtherJournals.objects.filter(pk=pk).delete()
        return redirect('/papers')
