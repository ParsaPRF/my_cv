# Amir Parsa Fatholahi - CV Website

A professional resume/CV website built with Django 5.2, featuring a modern design with dark mode support.

## Features

- **Database-Driven Content**: All content managed through Django admin panel
- **Dark Mode**: Toggle between light and dark themes with persistent preference
- **PDF Download**: Export resume as PDF document
- **Responsive Design**: Optimized for mobile, tablet, and desktop
- **SEO Optimized**: Meta tags, Open Graph, and Twitter Card support
- **Google Analytics**: Track visitor statistics
- **Smooth Scroll**: Enhanced navigation experience
- **Summernote Editor**: Rich text editing in admin panel

## Tech Stack

- **Backend**: Python, Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: SQLite
- **Libraries**: Summernote, ReportLab, Pillow

## Installation

```bash
# Clone the repository
git clone https://github.com/ParsaPRF/my_cv.git
cd my_cv

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Populate database with sample data
python populate_db.py

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Admin Panel

Access the admin panel at `/admin` to manage:
- Profile information
- Skills and categories
- Education history
- Work experience
- Projects with images
- Programming languages
- Language certificates
- Contact messages

## Project Structure

```
my_cv/
├── my_cv/              # Project settings
├── website/            # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── admin.py        # Admin configuration
│   └── urls.py         # URL routing
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # Uploaded files
└── manage.py           # Django management
```

## Author

**Amir Parsa Fatholahi**
- GitHub: [ParsaPRF](https://github.com/ParsaPRF)
- LinkedIn: [amir-parsa-fatholahi](https://www.linkedin.com/in/amir-parsa-fatholahi/)
- Email: parsatf98@gmail.com

## License

This project is open source and available under the MIT License.
