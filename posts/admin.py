from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User_people)


class BoxingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Boxing, BoxingAdmin)

class WrestlingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Wrestling, WrestlingAdmin)

class AthleticsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Athletics, AthleticsAdmin)

class WeightliftingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Weightlifting, WeightliftingAdmin)

class CyclingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Cycling, CyclingAdmin)

class Team_sportsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Team_sports, Team_sportsAdmin)
