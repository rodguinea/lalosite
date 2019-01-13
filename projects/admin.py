from django.contrib import admin

# Register your models here.
from projects.models import Project, Category, Bio
from projects.forms import ProjectsInlineForm


class ProjectsInline(admin.TabularInline):
    model = Project
    form = ProjectsInlineForm

    class Media:
        # js = ('js/admin/my_own_admin.js',)
        css = {
            'all': ('css/admin.css',)
        }


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [ProjectsInline]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'image', 'video', 'description', 'is_principal', 'order', 'is_shown')
    list_filter = ('language',)


class BioAdmin(admin.ModelAdmin):
    model = Bio


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Bio, BioAdmin)
