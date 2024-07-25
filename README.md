# Expense Tracker

## Overview

Expense Tracker is a Django-based web application designed to help users manage and track their expenses. It features user authentication with signup, login, and logout functionalities. The project uses SQLite as its default database and Pillow for image handling.

## Features

- **User Authentication**: Allows users to sign up, log in, and log out.
- **Expense Tracking**: Users can manage and track their expenses.

## Setup Instructions
### 1. Clone the Repository:
Open your terminal and run:
```bash
git clone https://github.com/rvindr/expense_tracker_django.git
```

### 2. Create and Activate Virtual Environment
#### On Windows
1.Create the Virtual Environment (if not already created):
```bash
python -m venv env
```
2.Activate the Virtual Environment:
```bash
.\env\Scripts\activate
```
#### On macOS
1.Create the Virtual Environment (if not already created):
```bash
python3 -m venv env
```
2.Activate the Virtual Environment:
```bash
source env/bin/activate
```

### 3. Install Dependencies
Install the required packages:
```bash
pip install django
pip install pillow
```
### 4. Apply Migrations
Navigate to the project directory and apply migrations:
```bash
cd expense
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Application
Start the development server:
```bash
python manage.py runserver
```
Access the admin panel at http://127.0.0.1:8000/admin/

### Screenshots
Here are some screenshots of the application:
<img width="1440" alt="Screenshot 2024-07-25 at 5 53 32 PM" src="https://github.com/user-attachments/assets/233a0104-d4a2-428e-87b9-35e85dbd2caf">
<img width="1440" alt="Screenshot 2024-07-25 at 5 54 03 PM" src="https://github.com/user-attachments/assets/96e10897-59da-4d34-b574-06d7b42e1659">
<img width="1440" alt="Screenshot 2024-07-25 at 5 54 51 PM" src="https://github.com/user-attachments/assets/72103f99-8a90-4e06-8fbe-92a43a94244b">



### Contributing
Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on GitHub.




