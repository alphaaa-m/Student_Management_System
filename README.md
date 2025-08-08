# Student Management System

## Project Poster

![Student Management System Poster](https://github.com/alphaaa-m/Student_Management_System/blob/main/SMS_POSTER.png)

---

## Project Description

The **Student Management System (SMS)** is a RESTful API built with **FastAPI** that provides a robust backend for managing student, course, and enrollment data. The system includes features for **user authentication and authorization**, allowing for different levels of access (admin vs. regular user) to protect sensitive data. The project uses **SQLAlchemy** with a **SQLite** database to handle data persistence, and **Pydantic** for data validation.

---

## Features

### 🔐 User Management
- User registration and authentication with **JWT** (JSON Web Tokens)
- **Role-based access control** (Admin and regular users)
- **Hashed passwords** for security

### 👤 Student Management
- **CRUD** (Create, Read, Update, Delete) operations for students
- Search for students by ID or email
- View a list of all courses a student is enrolled in

### 📘 Course Management
- CRUD operations for courses
- Search for courses by ID or course code
- View a list of all students enrolled in a specific course

### 📝 Enrollment Management
- Create and delete student enrollments in courses
- Prevents duplicate enrollments
- View a list of all enrollments

---

## Technologies Used

- **Backend Framework**: FastAPI  
- **Database**: SQLite  
- **ORM**: SQLAlchemy  
- **Data Validation**: Pydantic  
- **Authentication**: `python-jose` for JWT  
- **Password Hashing**: `passlib` (bcrypt)  
- **Deployment**: The project is structured to be easily deployed

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/alphaaa-m/Student_Management_System
cd Student_Management_System
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
```bash
uvicorn app.main:app --reload
```
