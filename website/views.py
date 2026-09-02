from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import (
    Profile, SkillCategory, Education, Experience,
    ProjectCategory, Project, ProgrammingLanguage,
    LanguageCertificate, Contact, Newsletter
)
from .forms import ContactForm, NewsletterForm


def index_view(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.all()
    education_items = Education.objects.all()
    experience_items = Experience.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    programming_languages = ProgrammingLanguage.objects.all()
    language_certificates = LanguageCertificate.objects.all()

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'education_items': education_items,
        'experience_items': experience_items,
        'project_categories': project_categories,
        'projects': projects,
        'programming_languages': programming_languages,
        'language_certificates': language_certificates,
    }
    return render(request, 'website/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('website:index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been subscribed successfully.')
    return redirect('website:index')


def download_cv(request):
    profile = Profile.objects.first()
    if not profile:
        messages.error(request, 'Profile not found.')
        return redirect('website:index')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_CV.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#4da6ff'),
        spaceAfter=20
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#333'),
        spaceBefore=20,
        spaceAfter=10
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#666'),
        spaceAfter=8
    )
    
    # Profile Info
    elements.append(Paragraph(profile.name, title_style))
    elements.append(Paragraph(profile.title, normal_style))
    elements.append(Paragraph(f"Email: {profile.email}", normal_style))
    elements.append(Paragraph(f"Phone: {profile.phone}", normal_style))
    elements.append(Paragraph(f"Location: {profile.location}", normal_style))
    elements.append(Spacer(1, 20))
    
    # Bio
    elements.append(Paragraph("About Me", heading_style))
    elements.append(Paragraph(profile.bio, normal_style))
    elements.append(Spacer(1, 20))
    
    # Education
    elements.append(Paragraph("Education", heading_style))
    for edu in Education.objects.all():
        elements.append(Paragraph(f"<b>{edu.title}</b>", normal_style))
        elements.append(Paragraph(f"{edu.institution} - {edu.period}", normal_style))
        elements.append(Paragraph(edu.description, normal_style))
    elements.append(Spacer(1, 20))
    
    # Experience
    elements.append(Paragraph("Experience", heading_style))
    for exp in Experience.objects.all():
        elements.append(Paragraph(f"<b>{exp.title}</b>", normal_style))
        elements.append(Paragraph(exp.period, normal_style))
        elements.append(Paragraph(exp.description, normal_style))
    elements.append(Spacer(1, 20))
    
    # Skills
    elements.append(Paragraph("Skills", heading_style))
    for cat in SkillCategory.objects.all():
        for skill in cat.skills.all():
            elements.append(Paragraph(f"• {skill.name}: {skill.description}", normal_style))
    elements.append(Spacer(1, 20))
    
    # Programming Languages
    elements.append(Paragraph("Programming Languages", heading_style))
    for lang in ProgrammingLanguage.objects.all():
        elements.append(Paragraph(f"• {lang.name}: {lang.technologies} ({lang.percentage}%)", normal_style))
    
    doc.build(elements)
    return response
