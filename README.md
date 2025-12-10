# Django Portfolio

A simple and clean Django-based portfolio website to showcase your projects and skills.

## Features

- **Project Showcase**: Display your projects with descriptions, technologies, and links
- **Portfolio Page**: Grid view of all projects with filtering capabilities
- **Project Details**: Individual project pages with full descriptions
- **About Section**: Personal bio and social media links
- **Responsive Design**: Mobile-friendly layout
- **Admin Dashboard**: Easy content management through Django admin

## Project Structure

```
myproject/
├── myapp/
│   ├── models.py          # Project and About models
│   ├── views.py           # View logic
│   ├── urls.py            # App URLs
│   ├── admin.py           # Django admin configuration
│   └── migrations/        # Database migrations
├── myproject/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Project URLs
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
│   ├── base.html
│   └── myapp/
│       ├── home.html
│       ├── portfolio.html
│       ├── project_detail.html
│       └── about.html
├── static/                # Static files
│   ├── css/style.css
│   └── js/script.js
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database

```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd myproject
```

2. **Create a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install django pillow
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create a superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

The portfolio will be available at `http://127.0.0.1:8000/`

## Usage

### Admin Dashboard

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Add your information in the "About" section
4. Create projects in the "Projects" section
5. Mark projects as "featured" to display them on the home page

### Adding Content

**To add a project:**
1. Go to Admin Dashboard
2. Click "Add Project"
3. Fill in the project details:
   - Title
   - Description
   - Image (optional)
   - Technologies used
   - Live project link (optional)
   - GitHub link (optional)
   - Mark as featured (optional)

**To add your about information:**
1. Go to Admin Dashboard
2. Click "Add About"
3. Fill in your bio and social media links

## Models

### Project Model
- `title`: Project name
- `description`: Project description
- `image`: Project screenshot/thumbnail
- `link`: Live project URL
- `github_link`: GitHub repository URL
- `technologies`: Technologies used (text field)
- `created_at`: Automatic timestamp
- `featured`: Boolean to feature on home page

### About Model
- `title`: Your name/title
- `bio`: Your biography
- `profile_image`: Profile picture
- `email`: Contact email
- `github_url`: GitHub profile URL
- `linkedin_url`: LinkedIn profile URL
- `twitter_url`: Twitter profile URL

## Customization

### Styling
Edit `static/css/style.css` to customize colors, fonts, and layout.

### Templates
Modify HTML templates in `templates/myapp/` to change the layout and design.

### Colors (CSS Variables)
```css
--primary-color: #2c3e50
--secondary-color: #3498db
--accent-color: #e74c3c
```

## Deployment

For production deployment:

1. **Update settings.py:**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = 'your-secret-key-here'
   ```

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Deploy to hosting platform** (Heroku, PythonAnywhere, etc.)

## Technologies Used

- **Backend**: Django 5.2+
- **Database**: SQLite (development), PostgreSQL (recommended for production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Handling**: Pillow

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

---

Happy showcasing! 🚀
