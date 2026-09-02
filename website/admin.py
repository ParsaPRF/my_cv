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
    summernote_fields = ('bio',)
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'bio', 'age', 'location', 'photo')
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
    list_display = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


@admin.register(Education)
class EducationAdmin(SummernoteModelAdmin):
    list_display = ('title', 'institution', 'period', 'order')
    ordering = ('order',)
    summernote_fields = ('description',)


@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'period', 'order')
    ordering = ('order',)
    summernote_fields = ('description',)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'image', 'order')
    list_filter = ('category',)
    ordering = ('order',)
    summernote_fields = ('description',)
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'category', 'technologies', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('github_url', 'demo_url')
        }),
        ('Ordering', {
            'fields': ('order',)
        }),
    )


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'order')
    ordering = ('order',)


@admin.register(LanguageCertificate)
class LanguageCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'level')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
