from django.contrib import admin
from .models import Course, Step


class StepInline(admin.StackedInline):
    model = Step

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline]


admin.site.register(Step)