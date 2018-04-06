from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, SCIJournals, UnpaidScopus, PaidScopus, OtherJournals, ConferencesOrg, WorkshopsOrg
from .models import ConferencesAttended, SeminarsAttended, WorkshopsAttended, TrainingProgAttended, SeminarsOrg
import datetime

YEAR_CHOICES = []
for r in range(1970, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))

DESGNCHOICES = [
    ('Professor', 'Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Assistant Professor', 'Assistant Professor'),
    ('Others', 'Others'),
]


class UserForm(UserCreationForm):
    username = forms.CharField(label='Employee ID',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RegForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    dept = forms.CharField(label='Department',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
    desgn = forms.ChoiceField(label='Designation', choices=DESGNCHOICES,
                              widget=forms.Select(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))

    class Meta:
        model = Profile
        fields = (
            'name',
            'dept',
            'desgn',
            'phone',
        )

    def save(self, commit=True):
        profile = super(RegForm, self).save(commit=False)
        profile.name = self.cleaned_data["name"]
        profile.dept = self.cleaned_data["dept"]
        profile.desgn = self.cleaned_data["desgn"]
        profile.phone = self.cleaned_data["phone"]
        if commit:
            profile.save()
        return profile


class PapersForm(forms.ModelForm):
    authors = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by comma'}))
    corresAuthors = forms.CharField(label='Corresponding Authors', widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by comma'}))
    paperTitle = forms.CharField(label='Paper Title',
                                 widget=forms.Textarea(
                                     attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Paper Title'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    impactFac = forms.CharField(label='Impact Factor',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Impact Factor'}))
    volume = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Volume'}))
    pp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PP'}))
    year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


class SCIForm(PapersForm):
    class Meta:
        model = SCIJournals
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class UnpaidScopusForm(PapersForm):
    class Meta:
        model = UnpaidScopus
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class PaidScopusForm(PapersForm):
    class Meta:
        model = PaidScopus
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class OthersJournalsForm(PapersForm):
    class Meta:
        model = OtherJournals
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class SemConForm(forms.ModelForm):
    authors = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by comma'}))
    paperTitle = forms.CharField(label='Paper Title',
                                 widget=forms.Textarea(
                                     attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Paper Title'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place'}))
    orgInstitute = forms.CharField(label='Organising Institute', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Organising Institute'}))
    duration = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))


class ConfAttendedForm(SemConForm):
    class Meta:
        model = ConferencesAttended
        fields = (
            'authors',
            'paperTitle',
            'name',
            'orgInstitute',
            'place',
            'duration',
        )


class SemAttendedForm(SemConForm):
    class Meta:
        model = SeminarsAttended
        fields = (
            'authors',
            'paperTitle',
            'name',
            'orgInstitute',
            'place',
            'duration',
        )


class WorkshopAttendedForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place'}))
    orgInstitute = forms.CharField(label='Organising Institute', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Organising Institute'}))
    duration = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = WorkshopsAttended
        fields = (
            'name',
            'orgInstitute',
            'place',
            'duration',
        )


class TPAttendedForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place'}))
    orgInstitute = forms.CharField(label='Organising Institute', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Organising Institute'}))
    duration = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = TrainingProgAttended
        fields = (
            'name',
            'orgInstitute',
            'place',
            'duration',
        )


class OrgForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    orgInstitute = forms.CharField(label='Organising Institute', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Organising Institute'}))
    fundingAgency = forms.CharField(label='Funding Agency',
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Funding Agency'}))
    duration = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}))


class ConfOrgForm(OrgForm):
    class Meta:
        model = ConferencesOrg
        fields = (
            'name',
            'orgInstitute',
            'role',
            'fundingAgency',
            'duration',
        )


class WorkOrgForm(OrgForm):
    class Meta:
        model = WorkshopsOrg
        fields = (
            'name',
            'orgInstitute',
            'role',
            'fundingAgency',
            'duration',
        )


class SemOrgForm(OrgForm):
    class Meta:
        model = SeminarsOrg
        fields = (
            'name',
            'orgInstitute',
            'role',
            'fundingAgency',
            'duration',
        )


class JournalsFilterForm(forms.Form):
    OPTIONS = (
        (0, 'SCI Journals'),
        (1, 'Unpaid Scopus'),
        (2, 'Paid Scopus'),
        (3, 'Other Journals'),

    )
    selections = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                           choices=OPTIONS)


class SeminarsFilterForm(forms.Form):
    OPTIONS = (
        (4, 'Conferences Attended'),
        (5, 'Seminars Attended'),
        (6, 'Workshops Attended'),
        (7, 'Training Programs Attended'),
        (8, 'Conferences Organised'),
        (9, 'Workshops Organised'),
        (10, 'Seminars Organised'),

    )
    selections = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                           choices=OPTIONS)


class PapersFilterForm(forms.Form):
    authors = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by space'}))
    corresAuthors = forms.CharField(required=False, label='Corresponding Authors', widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by space'}))
    paperTitle = forms.CharField(required=False, label='Paper Title',
                                 widget=forms.Textarea(
                                     attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Paper Title'}))
    name = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    year1 = forms.CharField(label='Years', required=False,
                            widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control',
                                                         'placeholder': "Use ',' for discrete years or '-' for range ex- 1999-2005 or 2017,1990 or 2016"}))


class SemFilterForm(forms.Form):
    name = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    place = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place'}))
    orgInstitute = forms.CharField(required=False, label='Organising Institute', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Organising Institute'}))
