from django.contrib import admin
from .models import Profile
from .models import SCIJournals, UnpaidScopus, PaidScopus, OtherJournals, SeminarsOrg, SeminarsAttended, \
    ConferencesAttended, ConferencesOrg, WorkshopsAttended, WorkshopsOrg, TrainingProgAttended

admin.site.register(Profile)
admin.site.register(SCIJournals)
admin.site.register(UnpaidScopus)
admin.site.register(PaidScopus)
admin.site.register(OtherJournals)
admin.site.register(SeminarsOrg)
admin.site.register(SeminarsAttended)
admin.site.register(ConferencesAttended)
admin.site.register(ConferencesOrg)
admin.site.register(WorkshopsAttended)
admin.site.register(WorkshopsOrg)
admin.site.register(TrainingProgAttended)
