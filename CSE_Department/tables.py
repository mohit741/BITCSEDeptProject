import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_tables2 import A
from .models import SeminarsOrg, SCIJournals, SeminarsAttended, UnpaidScopus, OtherJournals, ConferencesOrg, PaidScopus
from .models import WorkshopsAttended, TrainingProgAttended, WorkshopsOrg, ConferencesAttended, Profile


class UserTable(tables.Table):
    viewProfile = tables.LinkColumn('show_other_profile', text='View', args=[A('user')],
                                    orderable=False, empty_values=(), verbose_name='')

    def render_viewProfile(self, record):
        return mark_safe(
            '<a href=' + reverse("show_other_profile", args=[record.user]) + ' class="btn btn-sm btn-warning">View</a>')

    class Meta:
        model = Profile
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'user',
            'name',
            'dept',
            'desgn',
            'phone',
        )


class SCITable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        paper_type = 'SCI'
        return mark_safe(
            '<a href=' + reverse("edit_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        paper_type = 'SCI'
        return mark_safe(
            '<a href=' + reverse("delete_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = SCIJournals
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'corresAuthors',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class UnpaidScopusTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        paper_type = 'unpaid_scopus'
        return mark_safe(
            '<a href=' + reverse("edit_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        paper_type = 'unpaid_scopus'
        return mark_safe(
            '<a href=' + reverse("delete_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = UnpaidScopus
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'corresAuthors',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class PaidScopusTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        paper_type = 'paid_scopus'
        return mark_safe(
            '<a href=' + reverse("edit_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        paper_type = 'paid_scopus'
        return mark_safe(
            '<a href=' + reverse("delete_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = PaidScopus
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'corresAuthors',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class OtherJournalTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        paper_type = 'other_journals'
        return mark_safe(
            '<a href=' + reverse("edit_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        paper_type = 'other_journals'
        return mark_safe(
            '<a href=' + reverse("delete_papers",
                                 args=[paper_type, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = OtherJournals
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'corresAuthors',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class ConferencesAttendedTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        sem_type = 'Conferences_Attended'
        code = 0
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        sem_type = 'Conferences_Attended'
        code = 0
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = ConferencesAttended
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'place',
            'orgInstitute',
            'duration',
        )


class SeminarsAttendedTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 1
        sem_type = 'Seminars_Attended'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 1
        sem_type = 'Seminars_Attended'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = SeminarsAttended
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'paperTitle',
            'authors',
            'place',
            'orgInstitute',
            'duration',
        )


class WorkshopsAttendedTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 2
        sem_type = 'Workshops_Attended'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 2
        sem_type = 'Workshops_Attended'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = WorkshopsAttended
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'place',
            'orgInstitute',
            'duration',
        )


class TrainingProgAttendedTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 3
        sem_type = 'Training_Programs_Attended'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 3
        sem_type = 'Train_Programs_Attended'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = TrainingProgAttended
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'place',
            'orgInstitute',
            'duration',
        )


class ConferencesOrgTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 4
        sem_type = 'Conferences_Organised'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 4
        sem_type = 'Conferences_Organised'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = ConferencesOrg
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'role',
            'fundingAgency',
            'orgInstitute',
            'duration',
        )


class WorkshopsOrgTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 5
        sem_type = 'Workshops_Organised'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 5
        sem_type = 'Workshops_Organised'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = WorkshopsOrg
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'role',
            'fundingAgency',
            'orgInstitute',
            'duration',
        )


class SeminarsOrgTable(tables.Table):
    edit = tables.LinkColumn('edit', text='Edit', args=[A('pk')],
                             orderable=False, empty_values=(), verbose_name='')
    delete = tables.LinkColumn('delete', text='Delete', args=[A('pk')],
                               orderable=False, empty_values=(), verbose_name='')

    def render_edit(self, record):
        code = 6
        sem_type = 'Seminars_Organised'
        return mark_safe(
            '<a href=' + reverse("edit_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-warning">Edit</a>')

    def render_delete(self, record):
        code = 6
        sem_type = 'Seminars_Organised'
        return mark_safe(
            '<a href=' + reverse("delete_seminars",
                                 args=[sem_type, code, record.pk]) + ' class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = SeminarsOrg
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = (
            'name',
            'role',
            'fundingAgency',
            'orgInstitute',
            'duration',
        )
