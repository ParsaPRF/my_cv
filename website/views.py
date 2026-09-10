import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import (
    Profile, SkillCategory, Skill, Education, Experience,
    ProjectCategory, Project, ProgrammingLanguage,
    LanguageCertificate, Contact, Newsletter
)
from .forms import ContactForm, NewsletterForm
from .translations import TRANSLATIONS
from .utils import (
    localize_profile, localize_categories, localize_education,
    localize_experience, localize_project_categories,
    localize_projects, localize_programming_languages,
    localize_certificates
)

FONT_DIR = 'static/fonts'
pdfmetrics.registerFont(TTFont('Vazir', f'{FONT_DIR}/Vazir-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Vazir-Bold', f'{FONT_DIR}/Vazir-Bold.ttf'))

COLOR_PRIMARY = HexColor('#6c5ce7')
COLOR_ACCENT = HexColor('#00cec9')
COLOR_DARK = HexColor('#1a1a2e')
COLOR_TEXT = HexColor('#2d3436')
COLOR_LIGHT_TEXT = HexColor('#636e72')
COLOR_BG_LIGHT = HexColor('#f8f9fa')
COLOR_LINE = HexColor('#dfe6e9')


def fa(text):
    if not text:
        return ''
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def set_language(request, lang):
    if lang in ['en', 'fa']:
        response = redirect('website:index')
        response.set_cookie('lang', lang, max_age=365*24*60*60)
        return response
    return redirect('website:index')


def index_view(request):
    lang = request.COOKIES.get('lang', 'en')
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])

    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.all()
    education_items = Education.objects.all()
    experience_items = Experience.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    programming_languages = ProgrammingLanguage.objects.all()
    language_certificates = LanguageCertificate.objects.all()

    context = {
        't': t,
        'lang': lang,
        'profile': localize_profile(profile, lang),
        'skill_categories': localize_categories(skill_categories, lang),
        'education_items': localize_education(education_items, lang),
        'experience_items': localize_experience(experience_items, lang),
        'project_categories': localize_project_categories(project_categories, lang),
        'projects': localize_projects(projects, lang),
        'programming_languages': localize_programming_languages(programming_languages, lang),
        'language_certificates': localize_certificates(language_certificates, lang),
        'stat_projects': projects.count(),
        'stat_skills': Skill.objects.count(),
        'stat_langs': programming_languages.count(),
        'stat_experience': 3,
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
    lang = request.COOKIES.get('lang', 'en')
    is_fa = lang == 'fa'

    profile = Profile.objects.first()
    if not profile:
        messages.error(request, 'Profile not found.')
        return redirect('website:index')

    filename = f"{profile.name}_CV{'_FA' if is_fa else '_EN'}.pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    doc = SimpleDocTemplate(
        response, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm
    )

    font_normal = 'Vazir' if is_fa else 'Helvetica'
    font_bold = 'Vazir-Bold' if is_fa else 'Helvetica-Bold'
    align = TA_RIGHT if is_fa else TA_LEFT

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'NameStyle', fontName=font_bold, fontSize=22,
        textColor=COLOR_PRIMARY, spaceAfter=2*mm, alignment=align, leading=28
    )
    title_style = ParagraphStyle(
        'TitleStyle', fontName=font_normal, fontSize=12,
        textColor=COLOR_ACCENT, spaceAfter=4*mm, alignment=align, leading=16
    )
    section_style = ParagraphStyle(
        'SectionStyle', fontName=font_bold, fontSize=14,
        textColor=COLOR_PRIMARY, spaceBefore=6*mm, spaceAfter=3*mm,
        alignment=align, leading=18
    )
    body_style = ParagraphStyle(
        'BodyStyle', fontName=font_normal, fontSize=10,
        textColor=COLOR_TEXT, spaceAfter=2*mm, alignment=align, leading=15
    )
    small_style = ParagraphStyle(
        'SmallStyle', fontName=font_normal, fontSize=9,
        textColor=COLOR_LIGHT_TEXT, spaceAfter=1*mm, alignment=align, leading=13
    )
    contact_style = ParagraphStyle(
        'ContactStyle', fontName=font_normal, fontSize=9,
        textColor=COLOR_TEXT, alignment=align, leading=13
    )
    skill_name_style = ParagraphStyle(
        'SkillName', fontName=font_bold, fontSize=10,
        textColor=COLOR_TEXT, alignment=align, leading=14
    )
    skill_desc_style = ParagraphStyle(
        'SkillDesc', fontName=font_normal, fontSize=9,
        textColor=COLOR_LIGHT_TEXT, alignment=align, leading=13
    )

    elements = []

    if is_fa:
        name_display = fa(profile.name)
        title_display = fa(profile.title_fa or profile.title)
        bio_display = fa(profile.bio_fa or profile.bio)
    else:
        name_display = profile.name
        title_display = profile.title
        bio_display = profile.bio

    elements.append(Paragraph(name_display, name_style))
    elements.append(Paragraph(title_display, title_style))

    contact_items = []
    if is_fa:
        contact_items.append(fa(f"ایمیل: {profile.email}"))
        contact_items.append(fa(f"تلفن: {profile.phone}"))
        contact_items.append(fa(f"محل سکونت: {profile.location}"))
    else:
        contact_items.append(f"Email: {profile.email}")
        contact_items.append(f"Phone: {profile.phone}")
        contact_items.append(f"Location: {profile.location}")

    for item in contact_items:
        elements.append(Paragraph(item, contact_style))

    elements.append(Spacer(1, 2*mm))
    elements.append(HRFlowable(width="100%", thickness=1, color=COLOR_LINE, spaceAfter=4*mm))

    if is_fa:
        elements.append(Paragraph(fa('درباره من'), section_style))
    else:
        elements.append(Paragraph('About Me', section_style))
    elements.append(Paragraph(bio_display, body_style))

    educations = Education.objects.all()
    if educations.exists():
        if is_fa:
            elements.append(Paragraph(fa('تحصیلات'), section_style))
        else:
            elements.append(Paragraph('Education', section_style))
        for edu in educations:
            if is_fa:
                edu_title = fa(edu.title_fa or edu.title)
                edu_inst = fa(edu.institution_fa or edu.institution)
                edu_desc = fa(edu.description_fa or edu.description)
            else:
                edu_title = edu.title
                edu_inst = edu.institution
                edu_desc = edu.description
            elements.append(Paragraph(f"<b>{edu_title}</b>", body_style))
            elements.append(Paragraph(f"{edu_inst} | {edu.period}", small_style))
            elements.append(Paragraph(edu_desc, small_style))
            elements.append(Spacer(1, 2*mm))

    experiences = Experience.objects.all()
    if experiences.exists():
        if is_fa:
            elements.append(Paragraph(fa('تجربه کاری'), section_style))
        else:
            elements.append(Paragraph('Experience', section_style))
        for exp in experiences:
            if is_fa:
                exp_title = fa(exp.title_fa or exp.title)
                exp_desc = fa(exp.description_fa or exp.description)
            else:
                exp_title = exp.title
                exp_desc = exp.description
            elements.append(Paragraph(f"<b>{exp_title}</b>", body_style))
            elements.append(Paragraph(exp.period, small_style))
            elements.append(Paragraph(exp_desc, small_style))
            elements.append(Spacer(1, 2*mm))

    skill_cats = SkillCategory.objects.all()
    if skill_cats.exists():
        if is_fa:
            elements.append(Paragraph(fa('مهارت‌ها'), section_style))
        else:
            elements.append(Paragraph('Skills', section_style))
        for cat in skill_cats:
            if is_fa:
                cat_name = fa(cat.name_fa or cat.name)
            else:
                cat_name = cat.name
            elements.append(Paragraph(f"<b>{cat_name}</b>", skill_name_style))
            for skill in cat.skills.all():
                if is_fa:
                    s_name = fa(skill.name_fa or skill.name)
                    s_desc = fa(skill.description_fa or skill.description)
                else:
                    s_name = skill.name
                    s_desc = skill.description
                bullet = "• " if not is_fa else "• "
                elements.append(Paragraph(f"{bullet}{s_name}: {s_desc}", skill_desc_style))
            elements.append(Spacer(1, 1*mm))

    prog_langs = ProgrammingLanguage.objects.all()
    if prog_langs.exists():
        if is_fa:
            elements.append(Paragraph(fa('زبان‌های برنامه‌نویسی'), section_style))
        else:
            elements.append(Paragraph('Programming Languages', section_style))
        for lang_item in prog_langs:
            if is_fa:
                l_name = fa(lang_item.name_fa or lang_item.name)
                l_tech = fa(lang_item.technologies_fa or lang_item.technologies)
            else:
                l_name = lang_item.name
                l_tech = lang_item.technologies
            elements.append(Paragraph(f"<b>{l_name}</b> ({lang_item.percentage}%) - {l_tech}", body_style))

    certs = LanguageCertificate.objects.all()
    if certs.exists():
        if is_fa:
            elements.append(Paragraph(fa('گواهینامه‌های زبان'), section_style))
        else:
            elements.append(Paragraph('Language Certificates', section_style))
        for cert in certs:
            if is_fa:
                c_title = fa(cert.title_fa or cert.title)
                c_inst = fa(cert.institution_fa or cert.institution)
                c_level = fa(cert.level_fa or cert.level)
            else:
                c_title = cert.title
                c_inst = cert.institution
                c_level = cert.level
            elements.append(Paragraph(f"<b>{c_title}</b> - {c_level}", body_style))
            elements.append(Paragraph(c_inst, small_style))

    doc.build(elements)
    return response
