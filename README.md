### Student Management System
Project Description
The Student Management System (SMS) is a RESTful API built with FastAPI that provides a robust backend for managing student, course, and enrollment data. The system includes features for user authentication and authorization, allowing for different levels of access (admin vs. regular user) to protect sensitive data. The project uses SQLAlchemy with a SQLite database to handle data persistence, and Pydantic for data validation.

Features
User Management:

User registration and authentication with JWT (JSON Web Tokens).

Role-based access control (Admin and regular users).

Hashed passwords for security.

Student Management:

CRUD (Create, Read, Update, Delete) operations for students.

Search for students by ID or email.

View a list of all courses a student is enrolled in.

Course Management:

CRUD operations for courses.

Search for courses by ID or course code.

View a list of all students enrolled in a specific course.

Enrollment Management:

Create and delete student enrollments in courses.

Prevents duplicate enrollments.

View a list of all enrollments.

Technologies Used
Backend Framework: FastAPI

Database: SQLite

ORM (Object-Relational Mapping): SQLAlchemy

Data Validation: Pydantic

Authentication: python-jose for JWT

Password Hashing: passlib (bcrypt)

Deployment: The project is structured to be easily deployed.

Installation
Clone the repository:

git clone https://github.com/alphaaa-m/Student_Management_System
cd Student_Management_System

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies:
(You will need to create a requirements.txt file first)

pip install -r requirements.txt

Run the application:

uvicorn app.main:app --reload

The API will be available at http://127.0.0.1:8000. You can access the interactive documentation at http://127.0.0.1:8000/docs.

API Endpoints
The following are the main endpoints available in the API. For a complete list and detailed schema, please refer to the OpenAPI documentation available at /docs.

Users
POST /users/register: Register a new user (admin-only).

POST /users/token: Get an access token.

GET /users/me: Get the current authenticated user's information.

GET /users/: Get a list of all users (admin-only).

Students
POST /students/: Create a new student (admin-only).

GET /students/: Get a list of all students.

GET /students/{student_id}: Get a student by their ID.

PUT /students/{student_id}: Update student information (admin-only).

DELETE /students/{student_id}: Delete a student (admin-only).

GET /students/{student_id}/courses: Get a list of courses for a student.

Courses
POST /courses/: Create a new course (admin-only).

GET /courses/: Get a list of all courses.

GET /courses/{course_id}: Get a course by its ID.

PUT /courses/{course_id}: Update course information (admin-only).

DELETE /courses/{course_id}: Delete a course (admin-only).

GET /courses/{course_id}/students: Get a list of students for a course.

Enrollments
POST /enrollments/: Create a new enrollment (admin-only).

GET /enrollments/: Get a list of all enrollments.

GET /enrollments/{enrollment_id}: Get an enrollment by its ID.

DELETE /enrollments/{enrollment_id}: Delete an enrollment (admin-only).

Contributing
Please feel free to fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
