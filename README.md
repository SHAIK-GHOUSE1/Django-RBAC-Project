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
