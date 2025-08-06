# Build a complete Student Management System using FastAPI with authentication.

## The system should include the following features:

### Core Functionalities:
- CRUD operations for:
  - Students  
  - Courses  
  - Enrollments

### Database:
- Use SQLite with SQLAlchemy ORM  
- Set up proper relationships (many-to-many for students and courses via enrollments)

### API Endpoints:
- Register and manage students  
- Create, update, delete, and list courses  
- Enroll students into courses

### List:
- All students in a course  
- All courses a student is enrolled in

### Authentication:
- Implement JWT-based user authentication  
- Endpoints to:  
  - Register a user (admin or staff)  
  - Login and get a JWT token  
  - Protect all student/course/enrollment routes (only authenticated users can access)

- Optional:  
  - Include a role-based flag (e.g. is_admin) to distinguish user permissions

---

## Additional Requirements:
- Modular project structure:  
  `models`, `schemas`, `crud`, `auth`, `routes`, `database`

- Use Pydantic for validation  
- Dependency injection for DB sessions  
- Include Swagger UI (`/docs`)  
- Clean code with basic validations and error handling