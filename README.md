# Shared Expenses App

## Overview

Shared Expenses App is a full-stack expense management system designed to help groups track shared expenses, settlements, balances, and changing memberships over time.

The application was built as part of the Spreetail Software Engineering Internship assignment. The primary objective is not only expense tracking but also importing and cleaning a messy real-world expense dataset while maintaining transparency and auditability.

The system supports:

- User authentication
- Group management
- Historical membership tracking
- Expense management
- Settlement recording
- CSV import workflow
- Anomaly detection and review
- Balance calculation

---

# Problem Statement

A group of flatmates (Aisha, Rohan, Priya, Meera, Dev, and Sam) maintained shared expenses in a spreadsheet that contains:

- Duplicate entries
- Inconsistent participant names
- Multiple currencies
- Membership changes over time
- Settlement entries mixed with expenses
- Missing and ambiguous values

The goal is to import the CSV without manual editing, identify anomalies, allow review, and generate reliable balances.

---

# Tech Stack

## Backend

- Python 3.11
- Django 5
- Django REST Framework
- JWT Authentication
- PostgreSQL

## Database

- PostgreSQL 18

## API Authentication

- Simple JWT

## Development Tools

- Git
- GitHub
- pgAdmin 4

---

# Project Structure

```text
shared-expense-app/

├── backend/
│   ├── accounts/
│   ├── groups/
│   ├── expenses/
│   ├── settlements/
│   ├── imports/
│   ├── config/
│   └── manage.py
│
├── README.md
├── SCOPE.md
├── DECISIONS.md
├── AI_USAGE.md
└── IMPORT_REPORT.md
```

---

# Database Design

Core entities:

- User
- Group
- Membership
- Expense
- ExpenseParticipant
- Settlement
- ImportJob
- Anomaly

Membership history is tracked using:

```text
joined_at
left_at
```

This allows balances to respect membership changes over time.

---

# Features Implemented

## Authentication

- User registration
- JWT login
- JWT token refresh

## Group Management

- Groups
- Membership tracking

## Expense Domain

- Expense model
- Expense participant model

## Settlements

- Settlement tracking

## CSV Import

Current workflow:

```text
Upload CSV
↓
Parse CSV
↓
Create Import Job
↓
Store import metadata
```

---

# API Endpoints

## Authentication

```http
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
```

## Imports

```http
POST /api/imports/upload/
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Sakshi-Sood/shared-expenses-app.git
cd shared-expenses-app
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Create database:

```sql
CREATE DATABASE shared_expenses_db;
```

Create `.env`:

```env
SECRET_KEY=your_secret_key

DB_NAME=shared_expenses_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Server

```bash
python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# Import Workflow

The import subsystem processes CSV files without manual modification.

Workflow:

```text
CSV Upload
↓
Validation
↓
Parsing
↓
Import Job Creation
↓
Anomaly Detection
↓
Review
↓
Import
```

Current implementation supports:

- CSV upload
- CSV parsing
- Import job creation

Anomaly detection framework has been designed and is ready for extension.

---

# Documentation

Additional project documentation:

- SCOPE.md – anomaly catalog and database scope
- DECISIONS.md – engineering decision log
- AI_USAGE.md – AI collaboration report
- IMPORT_REPORT.md – import analysis report

---

# AI Usage

AI was used as a development collaborator for:

- Architecture planning
- Database design
- Django implementation guidance
- API design
- Import workflow design

All generated code and recommendations were reviewed, tested, and modified before inclusion.

---

# Repository

GitHub Repository:

https://github.com/Sakshi-Sood/shared-expenses-app
