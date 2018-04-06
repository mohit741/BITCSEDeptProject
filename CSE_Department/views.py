from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from .tables import *
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


def seminars_view(request, ):
    if request.user.is_authenticated:
        user = request.user
        ca = ConferencesAttendedTable(ConferencesAttended.objects.filter(user=user))
        RequestConfig(request).configure(ca)
        sa = SeminarsAttendedTable(SeminarsAttended.objects.filter(user=user))
        RequestConfig(request).configure(sa)
        wa = WorkshopsAttendedTable(WorkshopsAttended.objects.filter(user=user))
        RequestConfig(request).configure(wa)
        tpa = TrainingProgAttendedTable(TrainingProgAttended.objects.filter(user=user))
        RequestConfig(request).configure(tpa)
        co = ConferencesOrgTable(ConferencesOrg.objects.filter(user=user))
        RequestConfig(request).configure(co)
        wo = WorkshopsOrgTable(WorkshopsOrg.objects.filter(user=user))
        RequestConfig(request).configure(wo)
        so = SeminarsOrgTable(SeminarsOrg.objects.filter(user=user))
        RequestConfig(request).configure(wo)
        table = {'ca': ca, 'sa': sa, 'wa': wa, 'tpa': tpa, 'co': co, 'wo': wo, 'so': so}
        return render(request, 'seminars_view.html', {'user': user, 'table': table})
    else:
        return redirect('/login')


def other_seminars_view(request, user):
    if request.user.is_authenticated and request.user.is_staff:
        user = User.objects.get(username=user)
        ca = ConferencesAttendedTable(ConferencesAttended.objects.filter(user=user))
        ca.exclude = ('edit', 'delete')
        RequestConfig(request).configure(ca)
        sa = SeminarsAttendedTable(SeminarsAttended.objects.filter(user=user))
        sa.exclude = ('edit', 'delete')
        RequestConfig(request).configure(sa)
        wa = WorkshopsAttendedTable(WorkshopsAttended.objects.filter(user=user))
        wa.exclude = ('edit', 'delete')
        RequestConfig(request).configure(wa)
        tpa = TrainingProgAttendedTable(TrainingProgAttended.objects.filter(user=user))
        tpa.exclude = ('edit', 'delete')
        RequestConfig(request).configure(tpa)
        co = ConferencesAttendedTable(ConferencesAttended.objects.filter(user=user))
        co.exclude = ('edit', 'delete')
        RequestConfig(request).configure(co)
        wo = WorkshopsOrgTable(WorkshopsOrg.objects.filter(user=user))
        wo.exclude = ('edit', 'delete')
        RequestConfig(request).configure(wo)
        so = SeminarsOrgTable(SeminarsOrg.objects.filter(user=user))
        so.exclude = ('edit', 'delete')
        RequestConfig(request).configure(wo)
        table = {'ca': ca, 'sa': sa, 'wa': wa, 'tpa': tpa, 'co': co, 'wo': wo, 'so': so}
        user = request.user
        return render(request, 'other_seminars_view.html', {'user': user, 'table': table})
    else:
        return redirect('/login')


def add_seminars(request, sem_type, code):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            if code == 0:
                sem_form = ConfAttendedForm(request.POST)
            elif code == 1:
                sem_form = SemAttendedForm(request.POST)
            elif code == 2:
                sem_form = WorkshopAttendedForm(request.POST)
            elif code == 3:
                sem_form = TPAttendedForm(request.POST)
            elif code == 4:
                sem_form = ConfOrgForm(request.POST)
            elif code == 5:
                sem_form = WorkOrgForm(request.POST)
            else:
                sem_form = SemOrgForm(request.POST)
            if sem_form.is_valid():
                paper = sem_form.save(commit=False)
                paper.user = user
                paper.save()
            return redirect('/seminars')
        else:
            if code == 0:
                sem_form = ConfAttendedForm()
            elif code == 1:
                sem_form = SemAttendedForm()
            elif code == 2:
                sem_form = WorkshopAttendedForm()
            elif code == 3:
                sem_form = TPAttendedForm()
            elif code == 4:
                sem_form = ConfOrgForm()
            elif code == 5:
                sem_form = WorkOrgForm()
            else:
                sem_form = SemOrgForm()
            return render(request, 'seminars_edit.html',
                          {'sem_form': sem_form, 'user': user, 'sem_type': sem_type, 'code': code})
    else:
        return redirect('/login')


def edit_seminars(request, sem_type, code, pk):
    if request.user.is_authenticated:
        user = request.user
        if code == 0:
            item = ConferencesAttended.objects.filter(pk=pk).first()
        elif code == 1:
            item = SeminarsAttended.objects.filter(pk=pk).first()
        elif code == 2:
            item = WorkshopsAttended.objects.filter(pk=pk).first()
        elif code == 3:
            item = TrainingProgAttended.objects.filter(pk=pk).first()
        elif code == 4:
            item = ConferencesOrg.objects.filter(pk=pk).first()
        elif code == 5:
            item = WorkshopsOrg.objects.filter(pk=pk).first()
        else:
            item = SeminarsOrg.objects.filter(pk=pk).first()
        if request.method == 'POST':
            if code == 0:
                sem_form = ConfAttendedForm(request.POST, instance=item)
            elif code == 1:
                sem_form = SemAttendedForm(request.POST, instance=item)
            elif code == 2:
                sem_form = WorkshopAttendedForm(request.POST, instance=item)
            elif code == 3:
                sem_form = TPAttendedForm(request.POST, instance=item)
            elif code == 4:
                sem_form = ConfOrgForm(request.POST, instance=item)
            elif code == 5:
                sem_form = WorkOrgForm(request.POST, instance=item)
            else:
                sem_form = SemOrgForm(request.POST, instance=item)
            if sem_form.is_valid():
                sem_form.save()
            return redirect('/seminars')
        else:
            if code == 0:
                sem_form = ConfAttendedForm(instance=item)
            elif code == 1:
                sem_form = SemAttendedForm(instance=item)
            elif code == 2:
                sem_form = WorkshopAttendedForm(instance=item)
            elif code == 3:
                sem_form = TPAttendedForm(instance=item)
            elif code == 4:
                sem_form = ConfOrgForm(instance=item)
            elif code == 5:
                sem_form = WorkOrgForm(instance=item)
            else:
                sem_form = SemOrgForm(instance=item)
            return render(request, 'seminars_edit.html',
                          {'sem_form': sem_form, 'user': user, 'sem_type': sem_type, 'code': code})
    else:
        return redirect('/login')


@login_required
def delete_seminars(request, sem_type, code, pk):
    if request.method == 'GET':
        if code == 0:
            ConferencesAttended.objects.filter(pk=pk).delete()
        elif code == 1:
            SeminarsAttended.objects.filter(pk=pk).delete()
        elif code == 2:
            WorkshopsAttended.objects.filter(pk=pk).delete()
        elif code == 3:
            TrainingProgAttended.objects.filter(pk=pk).delete()
        elif code == 4:
            ConferencesOrg.objects.filter(pk=pk).delete()
        elif code == 5:
            WorkshopsOrg.objects.filter(pk=pk).delete()
        else:
            SeminarsOrg.objects.filter(pk=pk).delete()
        return redirect('/seminars')


def journals_filter_view(request):
    if request.method == 'POST':
        form = JournalsFilterForm(request.POST)
        if form.is_valid():
            options = form.cleaned_data.get('selections')
            serve_filter_forms(request, options)
            return redirect('/papers/filter/form')

    else:
        filter_form = JournalsFilterForm()
        form = filter_form
    return render(request, 'journals_filter_view.html', {'form': form})


def seminars_filter_view(request):
    if request.method == 'POST':
        form = SeminarsFilterForm(request.POST)
        if form.is_valid():
            options = form.cleaned_data.get('selections')
            forms = serve_filter_forms(options)
            request.sessions['paper_filter_form'] = forms
            return redirect('/papers/filter/form')
    else:
        filter_form = SeminarsFilterForm()
        form = filter_form
    return render(request, 'seminars_filter_view.html', {'form': form})


def papers_filter_form_view(request):
    forms = {}
    tables = {}
    if request.method == 'POST':
        if request.session['sci']:
            authors = request.POST.get('sci-authors')
            corresAuthors = request.POST.get('sci-corresAuthors')
            name = request.POST.get('sci-name')
            paperTitle = request.POST.get('sci-paperTitle')
            year = request.POST.get('sci-year1')
            qs = getPapersQuerySet(SCIJournals, authors, corresAuthors, paperTitle, name, year)
            sciTable = SCITable(qs)
            RequestConfig(request).configure(sciTable)
            tables['sciTable'] = sciTable
        if request.session['ups']:
            authors = request.POST.get('upd-authors')
            corresAuthors = request.POST.get('ups-corresAuthors')
            name = request.POST.get('ups-name')
            paperTitle = request.POST.get('ups-paperTitle')
            year = request.POST.get('ups-year1')
            qs = getPapersQuerySet(UnpaidScopus, authors, corresAuthors, paperTitle, name, year)
            upsTable = UnpaidScopusTable(qs)
            RequestConfig(request).configure(upsTable)
            tables['upsTable'] = upsTable
        if request.session['ps']:
            authors = request.POST.get('ps-authors')
            corresAuthors = request.POST.get('ps-corresAuthors')
            name = request.POST.get('ps-name')
            paperTitle = request.POST.get('ps-paperTitle')
            year = request.POST.get('ps-year1')
            qs = getPapersQuerySet(PaidScopus, authors, corresAuthors, paperTitle, name, year)
            psTable = PaidScopusTable(qs)
            RequestConfig(request).configure(psTable)
            tables['psTable'] = psTable
        if request.session['o']:
            authors = request.POST.get('o-authors')
            corresAuthors = request.POST.get('o-corresAuthors')
            name = request.POST.get('o-name')
            paperTitle = request.POST.get('o-paperTitle')
            year = request.POST.get('o-year1')
            qs = getPapersQuerySet(OtherJournals, authors, corresAuthors, paperTitle, name, year)
            oTable = OtherJournalTable(qs)
            RequestConfig(request).configure(oTable)
            tables['oTable'] = oTable
        return render(request, 'filtered_papers_view.html', {'tables': tables})
    else:
        if request.session['sci']:
            sci = PapersFilterForm(prefix='sci')
            forms['sci'] = sci
        if request.session['ups']:
            ups = PapersFilterForm(prefix='ups')
            forms['ups'] = ups
        if request.session['ps']:
            ps = PapersFilterForm(prefix='ps')
            forms['ps'] = ps
        if request.session['o']:
            o = PapersFilterForm(prefix='o')
            forms['o'] = o
    return render(request, 'papers_filter_form.html', {'forms': forms})


def serve_filter_forms(request, options):
    print(options)
    if '0' in options:
        request.session['sci'] = True
    else:
        request.session['sci'] = False
    if '1' in options:
        request.session['ups'] = True
    else:
        request.session['ups'] = False
    if '2' in options:
        request.session['ps'] = True
    else:
        request.session['ps'] = False
    if '3' in options:
        request.session['o'] = True
    else:
        request.session['o'] = False
    if '4' in options:
        request.session['sa'] = True
    else:
        request.session['ss'] = False
    if '5' in options:
        request.session['ca'] = True
    else:
        request.session['ca'] = False
    if '6' in options:
        request.session['wa'] = True
    else:
        request.session['wa'] = False
    if '7' in options:
        request.session['tpa'] = True
    else:
        request.session['tpa'] = False
    if '8' in options:
        request.session['co'] = True
    else:
        request.session['co'] = False
    if '9' in options:
        request.session['wo'] = True
    else:
        request.session['wo'] = False
    if '10' in options:
        request.session['so'] = True
    else:
        request.session['so'] = False


def getPapersQuerySet(obj, authors, corresAuthors, paperTitle, name, year):
    q = Q(authors__icontains='dummy')
    if authors is not None:
        al = authors.split(' ')
        if al[0] != '':
            for i in al:
                q = q | Q(authors__icontains=i)
    if corresAuthors is not None:
        ca = corresAuthors.split(' ')
        if ca[0] != '':
            for i in ca:
                q = q | Q(corresAuthors__icontains=i)
    if paperTitle is not None:
        n = paperTitle.split(' ')
        if n[0] != '':
            for i in n:
                q = q | Q(paperTitle__icontains=i)
    if name is not None:
        pt = name.split(' ')
        if pt[0] != '':
            for i in pt:
                q = q | Q(name__icontains=i)
    if ',' in year and year is not None:
        y = year.split(',')
        print(y)
        Y = list()
        for i in y:
            Y.append(int(i))
        if Y[0] != '':
            for i in Y:
                q = q | Q(year__icontains=i)
    elif '-' in year and year is not None:
        y = year.split('-')
        print(y)
        Y = list()
        for i in y:
            Y.append(i)
        if len(Y) > 1:
            q = q | (Q(year__gte=Y[0]) & Q(year__lte=Y[1]))
    elif len(year) == 4:
        Y = [int(year)]
        q = q | Q(year__icontains=Y[0])
    print(q)
    return obj.objects.filter(q)
