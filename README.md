# KPA Backend Assignment

This repository contains the implementation of Wheel Specification and Bogie Checksheet APIs as per the requirements.

## Project Setup

1. Clone the repository:

   git clone : https://github.com/leelamayashatapathy/kpa.git

2. Create virtual environment:

   python -m venv env

3. Activate the virtual environment:

   For Windows:

   env\Scripts\activate

   For Linux/Mac:

   source env/bin/activate

4. Install dependencies:

   pip install -r requirements.txt

5. Configure PostgreSQL database:

   - Create a PostgreSQL database 
   - Create a database user and grant privileges

6. Create .env file in project root:

   SECRET_KEY=your_django_secret_key
   DEBUG=True

   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=

7. Run migrations:

   python manage.py makemigrations
   python manage.py migrate

8. Start the development server:

   python manage.py runserver

APIs will be available at:

- http://127.0.0.1:8000/api/forms/wheel-specifications/
- http://127.0.0.1:8000/api/forms/wheel-specifications?formNumber=&submittedBy=&submittedDate=
- http://127.0.0.1:8000/api/forms/bogie-checksheet/

## Tech Stack Used

- Backend Framework: Django Rest Framework (DRF)
- Programming Language: Python
- Database: PostgreSQL
- Tools: Postman for testing, pgAdmin4 for database management

## Key Features Implemented

- Wheel Specification API
  - POST: Save wheel specification data with multiple nested fields
  - GET: Fetch filtered wheel specification data with query parameters

- Bogie Checksheet API
  - POST: Save bogie checksheet data with nested structure

## Limitations and Assumptions

- Authentication and user management are not implemented
