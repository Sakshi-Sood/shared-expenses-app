# Engineering Decision Log

## Decision 1 - Use Django REST Framework

### Options Considered

1. Flask
2. FastAPI
3. Django REST Framework

### Chosen

Django REST Framework

### Reason

- Rapid development
- Built-in authentication
- ORM support
- Admin panel
- Well suited for relational data

---

## Decision 2 - Use React Frontend

### Options Considered

1. HTML Templates
2. Vue
3. React

### Chosen

React

### Reason

- Mentioned in job description
- Industry standard
- Better frontend/backend separation

---

## Decision 3 - Use PostgreSQL

### Options Considered

1. SQLite
2. MySQL
3. PostgreSQL

### Chosen

PostgreSQL

### Reason

- Strong relational support
- Better production readiness
- Suitable for deployment

---

## Decision 4 - Track Membership History

### Problem

Group members change over time.

### Chosen Solution

Membership table with:

- joined_at
- left_at

### Reason

Balances must respect historical membership.

Without this approach:

- Meera could be charged after leaving
- Sam could be charged before joining

---

## Decision 5 - Store Settlements Separately

### Problem

Repayments are different from expenses.

### Chosen Solution

Create Settlement table.

### Reason

Avoid mixing money movement with spending.

---

## Decision 6 - Preserve Original Imported Data

### Chosen Solution

Store import logs and anomalies.

### Reason

Users should be able to trace decisions.

Supports auditability.

---

## Decision 7 - Do Not Auto Delete Duplicates

### Problem

Duplicate detection is probabilistic.

### Chosen Solution

Require user approval.

### Reason

Meera explicitly requested review before deletion.

---

## Decision 8 - Currency Handling

### Problem

Dataset contains USD expenses.

### Chosen Solution

Store:

- Original amount
- Original currency
- Converted INR amount

### Reason

Maintains transparency.

Supports audit trail.

---

## Decision 9 - Introduce Anomaly Table

### Chosen Solution

Dedicated anomaly tracking table.

### Reason

Every issue becomes traceable.

Supports import reports.

---

## Decision 10 - Import Wizard Instead Of Direct Import

### Chosen Solution

Upload
→ Analyze
→ Review
→ Import

### Reason

Prevents silent corrections.

Improves transparency.

---

## Decision 11 - Explainable Balances

### Problem

Users want balance transparency.

### Chosen Solution

Store expense contribution records.

### Reason

Users can trace every balance calculation.

Supports Rohan's requirement.

---

## Decision 12 - Balance Simplification

### Chosen Solution

Use debt simplification algorithm.

### Reason

Matches Aisha's requirement:

"Who pays whom and how much."

---
