TALABILL – Billing and Invoicing System
Developed by: Malbas, Aron, Sedimo, Baluca

Project Description
    The Billing and Invoicing System-TALABILL is a simple web-based billing and invoicing system built using Flask. It allows users to manage customers, create invoices, process payments, applies rate, and track billing records. The system also supports advance payments and provides comprehensive reporting for daily and monthly financial health.

Prerequisites:

-Python 3.8+
    Verify installation by running: python --version
-Flask: The core web framework.
-Pip: Python package manager.
    pip install flask
-Web Browser: To access the local dashboard (Chrome, Firefox, Edge).
-Code editor (VS Code recommended)

Instalation:
Clone or create the project folder:
    Place the billing_system folder in your desired directory (e.g., billing_system).
Install Flask:
    pip install flask
Save the code:
    Save the Python code as app.py in your folder.
Run the Application:
    python app.py
    The system will be live at http://127.0.0.1:5000/.

Usage:
-Home / Index Page
The system starts at the Home Page
Shows available user roles
-Login
Admin:
Username: admin
Password: admin123
User:
Username: user
Password: user123
-Dashboard
Main interface after logging in
Displays list of customers records
Features available:
-Add
Users can add new customer data
Input details through a form
Data is stored and displayed 
-Edit
Existing customer information can be updated
Users can modify names or other details
-Delete
Users can remove customer records
Deleted data will no longer appear in the list

Module Description

Completed Module: 
Module 1:Customer Management Module
It allows users to:

-Add new customers using input forms
-Store customer data using Python lists and dictionaries 
-Display customer records dynamically on the dashboard
-Automatically generate unique customer IDs
-Edit existing customer information
-Delete customer records when necessary
