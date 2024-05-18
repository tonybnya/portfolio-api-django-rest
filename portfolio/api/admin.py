from django.contrib import admin

from .models import Project, ProjectImage, Tag


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


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
