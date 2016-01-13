from django.contrib import admin
from problems.models import Detail,Problem,Submission

class ProblemAdmin(admin.ModelAdmin):
    pass

class DetailAdmin(admin.ModelAdmin):
    pass

class SubmissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Detail,DetailAdmin)
admin.site.register(Submission,SubmissionAdmin)

# Register your models here.
