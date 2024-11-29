**Django Role Base Access Control Project**
**Introduction**
This project implements an Authentication, Authorization, and Role-Based Access Control (RBAC) system using Django.
It is designed to meet the requirements outlined in the VRV Security Backend Developer Intern Assignment.
The application demonstrates secure user management with role-specific access to various resources,
ensuring that users can perform actions based on their assigned roles.
**Features**

1. **Authentication**
Users can register, log in, and log out securely.
Passwords are hashed using Django’s built-in secure password hashing.

3. **Role-Based Access Control (RBAC)**
Three roles are defined:
**Admin**: Has full access to manage users and modify content.
**Moderator**: Can view and manage specific content.
**User**: Has restricted access to view only user-specific content.
Access to views and resources is dynamically controlled based on the user’s role.
4. **Authorization**
Only authorized roles can access specific pages or perform specific actions.
Unauthorized attempts to access restricted pages return a 403 Forbidden error.

**Technical Stack**
**Backend Framework:** Django
**Database:** SQLite (default for development purposes)
**Authentication:** Session-based authentication (with secure password storage)
**HTML Templates:** Django’s templating engine

<h3>Setup and Installation</h3>
Follow the steps below to set up and run the project locally:

1. Clone the Repository

git clone https://github.com/SHAIK-GHOUSE1/Django-RBAC-Project.git


cd Django-RBAC-Project


2. **Create a Virtual Environment :**
      python -m venv rbac

source rbac/bin/activate   # For Linux/Mac

rbac\Scripts\activate      # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations

python manage.py migrate

5. Create a Superuser

python manage.py createsuperuser

6. Run the Server

python manage.py runserver

7. Access the Application

Open your browser and navigate to http://127.0.0.1:8000/.

Use the superuser credentials to log in to the Django Admin interface at /admin/.

Usage
Roles and Access
**Admin:**

Can log in to the admin dashboard.
Can manage all users, roles, and permissions.
**Moderator:**

Can access the moderator dashboard.
Has access to specific resources for content management.
**User:**

Can log in to the user dashboard.
Has restricted access to only user-related content.
Testing RBAC
Log in with different roles to test access controls.
Attempt accessing restricted pages (e.g., /admin-dashboard/ as a regular user) to see the 403 Forbidden error.
Project Structure
Django-RBAC-Project/<br>
├── Back_End/                   # Main Django project directory<br>
│   ├── settings.py             # Project settings<br>
│   ├── urls.py                 # URL configurations<br>
│   ├── wsgi.py                 # WSGI application<br>
├── accounts/                   # Accounts app for authentication and RBAC<br>
│   ├── models.py               # User and role models<br>
│   ├── views.py                # Views for login, registration, and dashboards<br>
│   ├── urls.py                 # App-specific URL patterns<br>
│   ├── templates/              # HTML templates<br>
│       ├── home.html           # Home page<br>
│       ├── login.html          # Login page<br>
│       ├── register.html       # Registration page<br>
│       ├── admin_dashboard.html  # Admin-specific dashboard<br>
│       ├── moderator_dashboard.html  # Moderator-specific dashboard<br>
│       ├── user_dashboard.html      # User-specific dashboard<br>
├── db.sqlite3                  # SQLite database<br>
├── manage.py                   # Django management script<br>
├── requirements.txt            # Dependencies<br>
└── README.md                   # Project description<br>


Security Best Practices Implemented<br>
Secure Password Hashing: User passwords are stored securely using Django's built-in hashing mechanisms.<br>
Role-Based Permissions: Views are protected based on user roles, ensuring secure access.<br>
Session Management: Users are authenticated and managed securely.<br>

**Future Enhancements**
Implement JWT-based authentication for API support.<br>
Add support for more granular permissions for roles.<br>
Integrate email verification for secure registration.<br>
