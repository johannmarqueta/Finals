from django.contrib import admin
from .models import Project, About


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'bio', 'profile_image')}),
        ('Contact', {'fields': ('email',)}),
        ('Social Links', {'fields': ('github_url', 'linkedin_url', 'twitter_url')}),
    )
