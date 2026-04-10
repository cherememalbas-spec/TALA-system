# 🟦 TALABILL – Billing and Invoicing System

**TALABILL** is a professional, web-based billing and invoicing solution designed to streamline customer management and financial tracking. Built with the **Flask** framework, it offers a clean interface for managing transactions, processing payments, and monitoring the financial health of a business.

---

## 👥 Developers
* **Malbas, Chereme**
* **Aron, Christa Loraine**
* **Patayan, Mafe**
* **Baluca, Rea Mae**

---

## 🚀 Project Description
The system provides an end-to-end solution for:
* **Customer Management:** Efficiently track and manage client profiles.
* **Invoicing & Billing:** Create professional invoices and apply rates.
* **Payment Processing:** Support for standard and advance payments.
* **Financial Reporting:** Daily and monthly health reports for better decision-making.

---

## 🛠️ Prerequisites
Before running the project, ensure you have the following installed:
* **Python 3.8+** (`python --version`)
* **Pip** (Python package manager)
* **Code Editor** (VS Code recommended)
* **Modern Web Browser** (Chrome, Edge, or Firefox)

---

## ⚙️ Installation & Setup

1. **Clone or Create the Project Folder**
   Place the `billing_system` folder in your desired directory.

2. **Install Flask**
   Open your terminal and run:
   ```bash
   pip install flask
3. **Save the code:**
    Save the Python code as app.py in your folder.
4. **Run the Application:**
    *python app.py*
    The system will be live at http://127.0.0.1:5000/.

---

## 🕹️ Usage Guide

### 🏠 Home / Index Page
* The system landing page provides an overview of **TALABILL**.
* Users can view descriptions and choose to "Sign In" to access the system.

### 🔐 Authentication
Use the following credentials to access the available user roles of the system:

* **Admin Access:**
    * **Username:** `admin`
    * **Password:** `admin123`
* **Staff/User Access:**
    * **Username:** `user`
    * **Password:** `user123`

### 📊 Dashboard & Navigation
* **Main Interface:** After a successful login, users are redirected to the Dashboard which displays the customer records table.
* **Navigation Bar:** * **Toggle Feature:** Use the sidebar menu to navigate between different system modules.

### 👥 Customer Management (CRUD)
* **Add:** Click the "Add Customer" button to open the input form. Fill in the details to save a new record.
* **Edit:** Update existing customer information by clicking the edit icon.
* **Delete:** Remove outdated or incorrect records from the database.
* **View:** All data is dynamically pulled and displayed in a clean, professional table format.

### 🚪 Secure Exit
* **Log Out:** Click the **Log Out** button (found in the top-right profile menu or the bottom of the sidebar) to end your session securely. 
* This redirects you back to the Home page and prevents unauthorized access to the dashboard.
---

## Module Description


**Completed Module:**
### Module 1:Customer Management Module

It allows users to:

* **Add new customers** using input forms
* **Store customer data** using Python lists and dictionaries 
* **Display customer records** dynamically on the dashboard
* **Automatically generate unique customer IDs**
* **Edit** existing customer information
* **Delete** customer records when necessary
