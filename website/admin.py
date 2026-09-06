from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Profile, SkillCategory, Skill, Education, Experience,
    ProjectCategory, Project, ProgrammingLanguage,
    LanguageCertificate, Contact, Newsletter
)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'phone', 'photo')
    summernote_fields = ('bio', 'bio_fa')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'title_fa', 'bio', 'bio_fa', 'age', 'location', 'photo')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'github', 'instagram')
        }),
        ('Files', {
            'fields': ('cv_file',)
        }),
    )


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa', 'category')
    list_filter = ('category',)


@admin.register(Education)
class EducationAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_fa', 'institution', 'period', 'order')
    ordering = ('order',)
    summernote_fields = ('description', 'description_fa')


@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_fa', 'period', 'order')
    ordering = ('order',)
    summernote_fields = ('description', 'description_fa')


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa')


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_fa', 'category', 'image', 'order')
    list_filter = ('category',)
    ordering = ('order',)
    summernote_fields = ('description', 'description_fa')
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'title_fa', 'category', 'technologies', 'description', 'description_fa')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('github_url', 'demo_url', 'live_url')
        }),
        ('Ordering', {
            'fields': ('order',)
        }),
    )


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fa', 'percentage', 'order')
    ordering = ('order',)


@admin.register(LanguageCertificate)
class LanguageCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_fa', 'institution', 'level')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
