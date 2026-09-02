import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_cv.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from website.models import (
    Profile, SkillCategory, Skill, Education, Experience,
    ProjectCategory, Project, ProgrammingLanguage, LanguageCertificate
)

# Clear existing data
Profile.objects.all().delete()
SkillCategory.objects.all().delete()
Skill.objects.all().delete()
Education.objects.all().delete()
Experience.objects.all().delete()
ProjectCategory.objects.all().delete()
Project.objects.all().delete()
ProgrammingLanguage.objects.all().delete()
LanguageCertificate.objects.all().delete()

# Profile
profile = Profile.objects.create(
    name='Amir Parsa Fatholahi',
    title='Web Designer & Developer',
    bio='Computer Science student with a passion for web design and development. Experienced with modern frontend and backend technologies, always eager to learn new topics. I have worked on various projects from desktop applications to interactive web apps.',
    age=21,
    location='Iran, Tehran',
    email='parsatf98@gmail.com',
    phone='09192136163',
    linkedin='https://www.linkedin.com/in/amir-parsa-fatholahi/',
    github='https://github.com/ParsaPRF',
    instagram='https://www.instagram.com/parsa_fatholahi',
)

# Skill Categories
cat_frontend = SkillCategory.objects.create(name='Front-end')
cat_backend = SkillCategory.objects.create(name='Back-end')
cat_tools = SkillCategory.objects.create(name='Tools')
cat_database = SkillCategory.objects.create(name='Database')
cat_design = SkillCategory.objects.create(name='Design')
cat_other = SkillCategory.objects.create(name='Other Skills')

# Skills
Skill.objects.create(category=cat_frontend, name='Front-end', description='HTML5, CSS3, JavaScript, Bootstrap, Responsive Design, SASS')
Skill.objects.create(category=cat_backend, name='Back-end', description='Python, Django, Django REST Framework, API Development, Authentication Systems')
Skill.objects.create(category=cat_tools, name='Tools', description='Git, GitHub, VS Code, PyCharm, Figma, Linux')
Skill.objects.create(category=cat_database, name='Database', description='PostgreSQL, MySQL, SQLite, MongoDB (Basic)')
Skill.objects.create(category=cat_design, name='Design', description='Figma, Photoshop, After Effects, Premiere Pro')
Skill.objects.create(category=cat_other, name='Other Skills', description='REST API, JSON, AJAX, Command Line, Video Editing')

# Education
Education.objects.create(
    title='BSc in Computer Science',
    institution='Faculty of Engineering - Islamic Azad University, Tehran West',
    period='2021 - Present',
    description='Currently pursuing with over 3 years of studies in Computer Science. Completed courses in Algorithms, Data Structures, Programming, Databases, and Software Engineering.',
    order=1
)

# Experience
Experience.objects.create(
    title='Web Developer - Freelance',
    period='2023 - Present',
    description='Designed and developed various web applications with Django, built REST APIs and implemented authentication systems.',
    order=1
)
Experience.objects.create(
    title='Video Editor',
    period='2022 - Present',
    description='Editing, color grading, and producing video content using After Effects and Premiere Pro.',
    order=2
)

# Project Categories
cat_web = ProjectCategory.objects.create(name='web')
cat_python = ProjectCategory.objects.create(name='python')
cat_other_proj = ProjectCategory.objects.create(name='other')

# Projects
Project.objects.create(
    title='Weather Application',
    category=cat_python,
    technologies='Python, Tkinter, API',
    description='A complete realworld Python application that fetches and displays graphical weather information for cities worldwide.',
    github_url='https://github.com/ParsaPRF/Python-GUI-Weather-Application',
    order=1
)
Project.objects.create(
    title='Python Calculator',
    category=cat_python,
    technologies='Python, Expression Parsing',
    description='A calculator built in Python without using the eval function, implementing expression parsing from scratch.',
    github_url='https://github.com/ParsaPRF/This-is-a-calculator-built-in-Python-without-using-the-eval-function',
    order=2
)
Project.objects.create(
    title='Profile Website',
    category=cat_web,
    technologies='GitHub, Markdown',
    description='GitHub profile README with personal information and project showcases.',
    github_url='https://github.com/ParsaPRF/ParsaPRF',
    order=3
)
Project.objects.create(
    title='CV Website',
    category=cat_web,
    technologies='Django, Bootstrap, HTML/CSS',
    description='Professional resume website built with Django framework.',
    order=4
)
Project.objects.create(
    title='OpenFrontIO',
    category=cat_other_proj,
    technologies='TypeScript, Browser Game',
    description='Online browser-based RTS game forked from openfrontio.',
    github_url='https://github.com/ParsaPRF/OpenFrontIO',
    order=5
)
Project.objects.create(
    title='E-commerce Backend',
    category=cat_web,
    technologies='Django REST, PostgreSQL, JWT',
    description='Full-featured e-commerce backend with REST API, authentication, and product management.',
    order=6
)

# Programming Languages
ProgrammingLanguage.objects.create(name='Python', technologies='Django, Django REST, Tkinter, Pandas', percentage=90, order=1)
ProgrammingLanguage.objects.create(name='JavaScript', technologies='ES6+, DOM, AJAX, JSON', percentage=75, order=2)
ProgrammingLanguage.objects.create(name='HTML / CSS', technologies='Bootstrap, SASS, Responsive Design', percentage=85, order=3)
ProgrammingLanguage.objects.create(name='SQL', technologies='PostgreSQL, MySQL, SQLite', percentage=70, order=4)
ProgrammingLanguage.objects.create(name='Bash', technologies='Shell Scripting, Linux Commands', percentage=65, order=5)
ProgrammingLanguage.objects.create(name='Git', technologies='Version Control, GitHub, GitLab', percentage=80, order=6)

# Language Certificates
LanguageCertificate.objects.create(
    title='C2 English Certificate',
    institution='Kanoon Zaban Language Institute',
    level='C2 (Advanced)'
)

print("Database populated successfully!")
