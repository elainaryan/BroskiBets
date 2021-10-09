from django.contrib import admin
from .models import DailyPicks, ScottPick, KanePick

class ScottPickInline(admin.StackedInline):
    model = ScottPick
    min_num = 0
    extra = 0

class KanePickInline(admin.StackedInline):
    model = KanePick
    min_num = 0
    extra = 0

class DailyPicksAdmin(admin.ModelAdmin):
    inlines = [ScottPickInline, KanePickInline]

admin.site.register(DailyPicks, DailyPicksAdmin)