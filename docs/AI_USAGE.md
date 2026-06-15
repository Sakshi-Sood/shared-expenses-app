# AI_USAGE.md

# AI Usage Report

## AI Tools Used

### Primary AI Tool

- ChatGPT (GPT-5.5)

### Purpose

AI was used as a development copilot throughout the project lifecycle for:

- Requirement analysis
- Product planning
- Database schema design
- Django project setup
- Django REST Framework development
- PostgreSQL configuration
- JWT authentication implementation
- CSV import workflow design
- Documentation generation
- Debugging assistance
- Architecture reviews

All outputs were reviewed and tested before incorporation into the project.

---

# Key Prompts Used

## Requirement Analysis

"Analyze the assignment and identify the underlying product and engineering problems rather than treating it as a CRUD application."

---

## Database Design

"Design a relational database schema for a shared expense application where users can join and leave groups over time."

---

## Authentication

"Implement JWT authentication using Django REST Framework and SimpleJWT."

---

## Import Architecture

"Design a CSV import pipeline that can detect anomalies, allow user review, and maintain auditability."

---

## Anomaly Detection

"Identify possible data anomalies in a shared expense dataset and propose handling strategies."

---

## Debugging

"Explain the root cause of this Django error and suggest a fix."

---

# Cases Where AI Was Wrong

The following examples demonstrate situations where AI-generated output required verification and correction.

---

## Case 1: Missing JWT Imports

### AI Output

AI generated URL configuration using:

```python
TokenObtainPairView.as_view()
TokenRefreshView.as_view()
```

but omitted the required import statement.

### How It Was Detected

Running:

```bash
python manage.py runserver
```

produced:

```text
NameError: TokenObtainPairView is not defined
```

### Correction

Added:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
```

### Lesson Learned

Generated code should always be verified for missing imports and dependencies before execution.

---

## Case 2: Incorrect Development Priority

### AI Output

AI suggested implementing anomaly detection logic before validating the CSV upload pipeline.

### How It Was Detected

During implementation it became clear that anomaly detection could not be tested until file upload, parsing, and import job creation were functioning correctly.

### Correction

The development order was changed to:

1. Database Models
2. Authentication
3. CSV Upload
4. Import Jobs
5. Anomaly Detection
6. Balance Calculation

### Lesson Learned

Foundational functionality should be completed before building higher-level features.

---

## Case 3: Overcomplicated Initial Architecture

### AI Output

AI initially proposed implementing a larger set of APIs, services, and business logic before confirming that the database schema was stable.

### How It Was Detected

This approach increased complexity and slowed progress during the early stages of development.

### Correction

The project was simplified into incremental milestones:

- Core models
- Database migrations
- Admin verification
- Authentication
- Import infrastructure
- Business logic

### Lesson Learned

Iterative development is more effective than implementing all features simultaneously.

---

## Case 4: CSV Upload Testing Strategy

### AI Output

AI initially focused on testing file uploads primarily through the Django REST Framework browser interface.

### How It Was Detected

Browser-based testing did not consistently provide the clearest feedback for multipart file uploads.

### Correction

API-first testing was adopted, focusing on endpoint validation and import job creation.

### Lesson Learned

The most convenient testing interface is not always the most reliable one.

---

# Validation Process

For every AI-generated suggestion:

- Requirements were reviewed manually.
- Code was inspected before integration.
- Database changes were tested locally.
- API endpoints were verified through execution.
- Documentation was updated to reflect implementation changes.

No AI-generated code was accepted without review.

---

# Conclusion

AI significantly accelerated development by acting as a technical copilot. However, all architectural decisions, debugging, validation, and final implementation choices remained the responsibility of the developer. The project was built through an iterative process of AI-assisted generation, human review, testing, and refinement.
