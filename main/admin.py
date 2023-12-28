from django.contrib import admin
from .models import User, Anketa, JobSeeker, Employer, Oтclick

admin.site.register(User)
# admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(Oтclick)

@admin.register(Anketa)
class Anketaadmin(admin.ModelAdmin):
    list_display = ['name','age','city','gender','file_url','phone_number','job']
    search_fields = ['name__istartswith','job']
    list_editable = ['age','city','file_url','job']
    ordering = ['job']

@admin.register(JobSeeker)
class JobSeekeradmin(admin.ModelAdmin):
    list_display = ['user_id','category','skill','format','experience_j','salary']
    search_fields = ['salary','skill__istartswith','category__istartswith']
    list_editable = ['category','skill','format','experience_j','salary']
    ordering = ['salary']
    
