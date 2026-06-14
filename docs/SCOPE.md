# Shared Expenses App - Scope & Anomaly Log

## Project Goal

Build a shared expense management application that helps a group of flatmates manage expenses, settlements, balances, and membership changes over time.

The application must import a messy CSV dataset, identify anomalies, allow users to review them, and generate accurate balances.

---

# Problem Statement

The provided spreadsheet contains several data quality issues:

- Duplicate entries
- Inconsistent participant names
- Multiple currencies
- Membership changes over time
- Settlements recorded as expenses
- Invalid or ambiguous data formats

The goal is not just to import the data but to handle these issues transparently and explain every action taken.

---

# Functional Requirements

## Authentication

- User Registration
- Login
- JWT Authentication

---

## Group Management

- Create Groups
- Update Groups
- Delete Groups
- View Group Details

---

## Membership Management

Support historical membership tracking.

A member can:

- Join a group
- Leave a group

Expenses should only affect members who belonged to the group when the expense occurred.

Example:

- Meera leaves at end of March
- Sam joins mid-April

April expenses should not affect Meera.

---

## Expense Management

Users can:

- Add Expense
- Edit Expense
- Delete Expense
- View Expense History

Supported split types:

- Equal Split
- Exact Amount Split
- Percentage Split
- Share / Weight Based Split

---

## Settlement Management

Users can:

- Record payments
- Settle balances
- View settlement history

Settlements must not be treated as expenses.

---

## Balance Calculation

### Group Summary

Show:

- Total owed
- Total receivable

### Individual Summary

Show:

- Amount owed
- Amount receivable

### Simplified Settlement View

Generate minimum transactions required to settle balances.

Example:

Rohan → Aisha ₹1200

---

## CSV Import

Users can upload the provided CSV file.

The importer must:

1. Parse data
2. Detect anomalies
3. Present anomalies
4. Suggest actions
5. Allow review
6. Import approved data

---

# Anomaly Log

## A01 - Exact Duplicate Expense

Description:
Two rows contain the same expense.

Detection:
Same payer, amount, date, and participants.

Action:
Flag for review.

---

## A02 - Possible Duplicate Expense

Description:
Similar expense descriptions with slightly different amounts.

Action:
Flag for review.

---

## A03 - Inconsistent Person Names

Examples:

- Priya
- priya
- Priya S

Action:
Suggest merge.

Requires approval.

---

## A04 - Multiple Date Formats

Examples:

- YYYY-MM-DD
- DD/MM/YYYY
- Month Name Formats

Action:
Normalize when unambiguous.

Otherwise request review.

---

## A05 - Missing Payer

Description:
Expense has no payer.

Action:
Flag as needs review.

---

## A06 - Settlement Recorded As Expense

Description:
Transaction appears to be debt repayment.

Action:
Convert to settlement after review.

---

## A07 - Invalid Percentage Split

Description:
Percentages do not total 100%.

Action:
Reject automatic import.

---

## A08 - Missing Currency

Description:
Currency field missing.

Action:
Suggest default currency.

Requires approval.

---

## A09 - Currency Conversion Required

Description:
USD expenses exist in dataset.

Action:
Convert using chosen exchange rate policy.

---

## A10 - Negative Amount

Description:
Negative expense detected.

Action:
Treat as refund.

---

## A11 - Zero Amount Expense

Description:
Expense amount equals zero.

Action:
Flag for review.

---

## A12 - Former Member Included

Description:
Expense includes member who already left.

Action:
Flag for review.

---

## A13 - New Member Charged Before Joining

Description:
Expense includes member before join date.

Action:
Flag for review.

---

## A14 - Split Type Mismatch

Description:
Declared split type differs from participant data.

Action:
Flag for review.

---

## A15 - Unknown Participant

Description:
Participant not found in group.

Action:
Create temporary participant or request review.

---

# Database Schema Overview

Tables:

- Users
- Groups
- Memberships
- Expenses
- ExpenseParticipants
- Settlements
- ImportJobs
- Anomalies

Detailed schema documented in DECISIONS.md.

---
