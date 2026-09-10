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
    title_fa='طراح و توسعه‌دهنده وب',
    bio='Computer Science student with a passion for web design and development. Experienced with modern frontend and backend technologies, always eager to learn new topics. I have worked on various projects from desktop applications to interactive web apps.',
    bio_fa='دانشجوی علوم کامپیوتر با علاقه‌مندی به طراحی و توسعه وب. با تکنولوژی‌های مدرن فرانت‌اند و بک‌اند آشنا هستم و همیشه مشتاق یادگیری موضوعات جدیدم. روی پروژه‌های مختلفی از اپلیکیشن‌های دسکتاپ تا وب‌اپ‌های تعاملی کار کرده‌ام.',
    age=21,
    location='Iran, Tehran',
    email='parsatf98@gmail.com',
    phone='09192136163',
    linkedin='https://www.linkedin.com/in/amir-parsa-fatholahi/',
    github='https://github.com/ParsaPRF',
    instagram='https://www.instagram.com/parsa_fatholahi',
)

# Skill Categories
cat_frontend = SkillCategory.objects.create(name='Front-end', name_fa='فرانت‌اند')
cat_backend = SkillCategory.objects.create(name='Back-end', name_fa='بک‌اند')
cat_tools = SkillCategory.objects.create(name='Tools', name_fa='ابزارها')
cat_database = SkillCategory.objects.create(name='Database', name_fa='پایگاه داده')
cat_design = SkillCategory.objects.create(name='Design', name_fa='طراحی')
cat_other = SkillCategory.objects.create(name='Other Skills', name_fa='مهارت‌های دیگر')

# Skills
Skill.objects.create(category=cat_frontend, name='Front-end', name_fa='فرانت‌اند', description='HTML5, CSS3, JavaScript, Bootstrap, Responsive Design, SASS', description_fa='HTML5, CSS3, JavaScript, Bootstrap, طراحی ریسپانسیو, SASS')
Skill.objects.create(category=cat_backend, name='Back-end', name_fa='بک‌اند', description='Python, Django, Django REST Framework, API Development, Authentication Systems', description_fa='Python, Django, فریم‌ورک Django REST, توسعه API, سیستم‌های احراز هویت')
Skill.objects.create(category=cat_tools, name='Tools', name_fa='ابزارها', description='Git, GitHub, VS Code, PyCharm, Figma, Linux', description_fa='Git, GitHub, VS Code, PyCharm, Figma, Linux')
Skill.objects.create(category=cat_database, name='Database', name_fa='پایگاه داده', description='PostgreSQL, MySQL, SQLite, MongoDB (Basic)', description_fa='PostgreSQL, MySQL, SQLite, MongoDB (مقدماتی)')
Skill.objects.create(category=cat_design, name='Design', name_fa='طراحی', description='Figma, Photoshop, After Effects, Premiere Pro', description_fa='Figma, Photoshop, After Effects, Premiere Pro')
Skill.objects.create(category=cat_other, name='Other Skills', name_fa='مهارت‌های دیگر', description='REST API, JSON, AJAX, Command Line, Video Editing', description_fa='REST API, JSON, AJAX, خط فرمان, ویرایش ویدیو')

# Education
Education.objects.create(
    title='BSc in Computer Science',
    title_fa='کارشناسی علوم کامپیوتر',
    institution='Faculty of Engineering - Islamic Azad University, Tehran West',
    institution_fa='دانشکده مهندسی - دانشگاه آزاد اسلامی واحد تهران غرب',
    period='2021 - Present',
    description='Currently pursuing with over 3 years of studies in Computer Science. Completed courses in Algorithms, Data Structures, Programming, Databases, and Software Engineering.',
    description_fa='در حال حاضر بیش از ۳ سال تحصیل در رشته علوم کامپیوتر. دروس الگوریتم‌ها، ساختمان داده، برنامه‌نویسی، پایگاه داده و مهندسی نرم‌افزار را گذرانده‌ام.',
    order=1
)

# Experience
Experience.objects.create(
    title='Web Developer - Freelance',
    title_fa='توسعه‌دهنده وب - فریلنسر',
    period='2023 - Present',
    description='Designed and developed various web applications with Django, built REST APIs and implemented authentication systems.',
    description_fa='طراحی و توسعه وب‌اپلیکیشن‌های مختلف با Django، ساخت REST API و پیاده‌سازی سیستم‌های احراز هویت.',
    order=1
)
Experience.objects.create(
    title='Video Editor',
    title_fa='ویرایشگر ویدیو',
    period='2022 - Present',
    description='Editing, color grading, and producing video content using After Effects and Premiere Pro.',
    description_fa='ویرایش، تصحیح رنگ و تولید محتوای ویدیویی با استفاده از After Effects و Premiere Pro.',
    order=2
)

# Project Categories
cat_web = ProjectCategory.objects.create(name='web', name_fa='وب')
cat_python = ProjectCategory.objects.create(name='python', name_fa='پایتون')
cat_other_proj = ProjectCategory.objects.create(name='other', name_fa='سایر')

# Projects
Project.objects.create(
    title='Weather Application',
    title_fa='اپلیکیشن آب و هوا',
    category=cat_python,
    technologies='Python, Tkinter, API',
    description='A complete realworld Python application that fetches and displays graphical weather information for cities worldwide.',
    description_fa='یک اپلیکیشن کامل پایتون که اطلاعات آب و هوا را برای شهرهای سراسر جهان دریافت و نمایش می‌دهد.',
    github_url='https://github.com/ParsaPRF/Python-GUI-Weather-Application',
    order=1
)
Project.objects.create(
    title='Python Calculator',
    title_fa='ماشین حساب پایتون',
    category=cat_python,
    technologies='Python, Expression Parsing',
    description='A calculator built in Python without using the eval function, implementing expression parsing from scratch.',
    description_fa='ماشین حسابی ساخته شده در پایتون بدون استفاده از تابع eval، با پیاده‌سازی تحلیل عبارات از صفر.',
    github_url='https://github.com/ParsaPRF/This-is-a-calculator-built-in-Python-without-using-the-eval-function',
    order=2
)
Project.objects.create(
    title='Profile Website',
    title_fa='وب‌سایت پروفایل',
    category=cat_web,
    technologies='GitHub, Markdown',
    description='GitHub profile README with personal information and project showcases.',
    description_fa='README پروفایل گیت‌هاب با اطلاعات شخصی و نمایش پروژه‌ها.',
    github_url='https://github.com/ParsaPRF/ParsaPRF',
    order=3
)
Project.objects.create(
    title='CV Website',
    title_fa='وب‌سایت رزومه',
    category=cat_web,
    technologies='Django, Bootstrap, HTML/CSS',
    description='Professional resume website built with Django framework.',
    description_fa='وب‌سایت رزومه حرفه‌ای ساخته شده با فریم‌ورک Django.',
    order=4
)
Project.objects.create(
    title='OpenFrontIO',
    title_fa='OpenFrontIO',
    category=cat_other_proj,
    technologies='TypeScript, Browser Game',
    description='Online browser-based RTS game forked from openfrontio.',
    description_fa='بازی استراتژیک آنلاین مرورگری فورک شده از openfrontio.',
    github_url='https://github.com/ParsaPRF/OpenFrontIO',
    order=5
)
Project.objects.create(
    title='Travelo',
    title_fa='Travelo',
    category=cat_web,
    technologies='Django, SQLite, HTML/CSS',
    description='Travel blog website built with Django - Based on Colorlib Travelo template with authentication, blog posts, and comments.',
    description_fa='وبلاگ سفر ساخته شده با Django - بر اساس قالب Colorlib Travelo با احراز هویت، پست‌های وبلاگ و نظرات.',
    github_url='https://github.com/ParsaPRF/travelo',
    order=6
)
Project.objects.create(
    title='E-commerce Backend',
    title_fa='بک‌اند فروشگاه آنلاین',
    category=cat_web,
    technologies='Django REST, PostgreSQL, JWT',
    description='Full-featured e-commerce backend with REST API, authentication, and product management.',
    description_fa='بک‌اند کامل فروشگاه آنلاین با REST API، احراز هویت و مدیریت محصولات.',
    order=7
)

# Programming Languages
ProgrammingLanguage.objects.create(name='Python', name_fa='پایتون', technologies='Django, Django REST, Tkinter, Pandas', technologies_fa='Django, Django REST, Tkinter, Pandas', percentage=90, order=1)
ProgrammingLanguage.objects.create(name='JavaScript', name_fa='جاوااسکریپت', technologies='ES6+, DOM, AJAX, JSON', technologies_fa='ES6+, DOM, AJAX, JSON', percentage=75, order=2)
ProgrammingLanguage.objects.create(name='HTML / CSS', name_fa='HTML / CSS', technologies='Bootstrap, SASS, Responsive Design', technologies_fa='Bootstrap, SASS, طراحی ریسپانسیو', percentage=85, order=3)
ProgrammingLanguage.objects.create(name='SQL', name_fa='SQL', technologies='PostgreSQL, MySQL, SQLite', technologies_fa='PostgreSQL, MySQL, SQLite', percentage=70, order=4)
ProgrammingLanguage.objects.create(name='Bash', name_fa='Bash', technologies='Shell Scripting, Linux Commands', technologies_fa='اسکریپت‌نویسی Shell, دستورات Linux', percentage=65, order=5)
ProgrammingLanguage.objects.create(name='Git', name_fa='Git', technologies='Version Control, GitHub, GitLab', technologies_fa='کنترل نسخه, GitHub, GitLab', percentage=80, order=6)

# Language Certificates
LanguageCertificate.objects.create(
    title='C1 English Certificate',
    title_fa='گواهینامه زبان انگلیسی C1',
    institution='Kanoon Zaban Language Institute',
    institution_fa='آموزشگاه زبان کانون',
    level='C1 (Upper-Intermediate)',
    level_fa='C1 (فوق پیشرفته)'
)

print("Database populated successfully!")
