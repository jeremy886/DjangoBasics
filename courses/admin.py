from django.contrib import admin
from . import models


class TextInline(admin.StackedInline):
    model = models.Text


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline]


admin.site.register(models.Text)
admin.site.register(models.Quiz)