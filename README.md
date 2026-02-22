🎓 Student Management System (File-Based)

A complete File-Based Student Management System built using Python (OOP) with secure password hashing and JSON-based marks storage.

This project simulates a real academic management environment with Admin, Teacher, and Student roles.

🚀 Features
👨‍💼 Admin Panel

Add / View / Delete Teachers

Add / View / Delete Students

Assign Students to Teachers

Change Admin Password

File persistence support

👨‍🏫 Teacher Panel

Secure Login (Hashed PIN)

View Assigned Students

Assign:

Quiz Marks

Assignment Marks

Mid Marks

Final Marks

Update Existing Marks

View Student Marks

Change Password

👨‍🎓 Student Panel

Secure Login (Hashed PIN)

View Subject Marks

View Detailed Result

Automatic:

Total Calculation

Percentage Calculation

Grade Calculation

Change Password

🔐 Security Features

Passwords stored using SHA-256 hashing

Role-based access control

File-based data persistence

JSON-based marks storage

🧠 OOP Concepts Used

Classes & Objects

Encapsulation

Class Relationships

Data Abstraction

Modular Functions

Classes:

Student

Teacher

SubjectRecord

💾 Data Storage Structure
Data Type	Storage Method
Students	Text File
Teachers	Text File
Student-Teacher Assignment	Text File
Marks	JSON File
Admin PIN	Text File
📊 Result Calculation Logic

Quiz Total = Number of quizzes × 10

Assignment Total = Number of assignments × 10

Mid = 25 Marks

Final = 50 Marks

Percentage auto calculated

Grade auto generated (A+ to F)

🛠 Technologies Used

Python

OOP

File Handling

JSON

Hashlib (SHA-256)

Basic System Design

▶️ How to Run

Make sure Python is installed.

Download or clone this repository.

Run:

python filename.py
📌 Project Purpose

This project was built to:

Strengthen OOP concepts

Practice file-based data persistence

Simulate real-world system architecture

Prepare for database conversion

🔜 Future Improvements

Convert to Database Version (MySQL)

Build Web Version (Flask / FastAPI)

Add GUI Interface

Improve error handling

Add logging system

👨‍💻 Author

Saad Khan
Software Engineering Student
Passionate about AI-Powered Systems & Backend Development

⭐ If you like this project, consider giving it a star!
