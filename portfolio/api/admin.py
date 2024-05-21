from django.contrib import admin

from .models import Project, ProjectImage, Tag, Timeline


# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    """Custom fields inside the Admin panel of Django."""

    list_display = ("title", "live_url", "source_url")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class TimelineAdmin(admin.ModelAdmin):
    list_display = ("year", "milestone", "duration")
    search_fields = ("milestone", "year")
    list_filter = ("year",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Timeline, TimelineAdmin)
