## 🔐 Test Scenarios for Authentication System – CleanCity Web App

### 📌 Objective
To ensure the CleanCity authentication system (Login, Registration, and Logout) is secure, reliable, and user-friendly. These scenarios cover positive and negative paths, validations, role-based access, and UI behavior.

---

### 🔑 Registration Scenarios

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| R-01   | Register with valid name, email, password, and confirm password   | Account is created successfully; redirected to login      |
| R-02   | Submit registration form with missing name                        | Error message shown: "Full Name is required"             |
| R-03   | Register with existing email address                              | Error: "Email already exists"                            |
| R-04   | Password and confirm password do not match                        | Error: "Passwords do not match"                          |
| R-05   | Password length < 3 characters                                    | Error: "Password must be at least 3 characters"          |
| R-06   | Register with invalid email format                                | Error: "Invalid email address"                           |
| R-07   | Submit with all fields blank                                      | All required field errors displayed                       |
| R-08   | Register with leading/trailing spaces in input                    | Input is trimmed and account created                      |

---

### 🔐 Login Scenarios

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| L-01   | Login with valid credentials (user account)                       | Redirect to Dashboard with user links                     |
| L-02   | Login with valid admin credentials                                | Redirect to Dashboard with admin links shown              |
| L-03   | Login with incorrect password                                     | Error: "Invalid email or password"                        |
| L-04   | Login with non-existent email                                     | Error: "Invalid email or password"                        |
| L-05   | Submit login form with empty email                                | Error: "Email is required"                               |
| L-06   | Submit login form with empty password                             | Error: "Password is required"                            |
| L-07   | Attempt login with SQL injection (`' OR 1=1 --`)                  | Input blocked or error shown                              |
| L-08   | Input long strings in email/password fields (>100 chars)          | Proper error handling or trimming                         |

---

### 🚪 Logout Scenarios

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| LO-01  | Click logout as logged-in user                                    | Session cleared; redirected to login                      |
| LO-02  | Logout button hidden for unauthenticated users                    | Logout button not displayed                               |
| LO-03  | Access logout URL directly without being logged in               | Redirect to login or homepage                             |

---

### 👮‍♂️ Access Control & Role-Based UI

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| A-01   | Admin logs in and sees admin panel link                           | Admin link visible                                        |
| A-02   | Regular user logs in; admin link should be hidden                 | Admin link hidden                                         |
| A-03   | Unauthenticated user visits Dashboard URL                         | Redirected to login                                       |
| A-04   | Admin-only page accessed by regular user                          | Access blocked or redirected                              |
| A-05   | Authenticated user sees correct navbar links                      | Login/Register hidden; Dashboard/Logout shown             |
| A-06   | Unauthenticated user sees Login/Register only                     | Dashboard/Admin/Logout hidden                             |

---

### 🛠️ UI & Field Behavior

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| UI-01  | Input fields display placeholders                                 | Placeholders correctly displayed                          |
| UI-02  | Required fields show visual indicator (e.g., *)                   | Asterisk or visual cue shown                             |
| UI-03  | Error messages disappear after successful correction              | Errors hidden upon valid input                            |
| UI-04  | Tab order allows keyboard navigation between fields               | Tabbing order is correct                                  |
| UI-05  | Password fields are masked (dots instead of plain text)           | Passwords not visible                                     |
| UI-06  | Responsive form layout on mobile devices                          | Form fields adapt to screen size                          |

---

### 🧪 Other Security and Usability Checks

| ID     | Scenario Description                                              | Expected Result                                          |
|--------|--------------------------------------------------------------------|-----------------------------------------------------------|
| S-01   | Session timeout after inactivity                                  | User is logged out automatically                         |
| S-02   | CSRF protection on forms                                          | Tokens validated (if implemented)                        |
| S-03   | Multiple failed login attempts                                    | Optional lockout or throttling shown                     |
| S-04   | Browser back button after logout                                  | Session invalidated; redirected to login                 |
| S-05   | Autofill functionality allowed for email but not password         | Security best practices maintained                       |

---
## ♻️ Test Scenarios for Waste Management Module

### 📌 Objective
To validate all aspects of the Waste Pickup Request functionality, from form submission to dashboard tracking and admin status updates.

---

### 📝 Pickup Request Form (User)

| ID     | Scenario Description                                                  | Expected Result                                              |
|--------|------------------------------------------------------------------------|---------------------------------------------------------------|
| WM-01  | Submit pickup form with valid name, location, and waste type         | Request is created successfully; confirmation message shown   |
| WM-02  | Submit form without selecting location                               | Error: "Location is required"                                |
| WM-03  | Submit form without selecting waste type                             | Error: "Waste Type is required"                              |
| WM-04  | Submit form without full name                                        | Error: "Full Name is required"                               |
| WM-05  | Submit form with all fields blank                                    | All required field errors displayed                          |
| WM-06  | Select preferred pickup date in the past                             | Error or date auto-adjusted                                  |
| WM-07  | Enter name with special characters                                   | Input accepted and stored correctly                          |
| WM-08  | Try submitting duplicate request (same name + date)                  | System should handle gracefully (optional prevention)         |
| WM-09  | Attempt form submission while logged out                             | Redirect to login or error message                           |
| WM-10  | Submit form on mobile browser                                        | Mobile layout remains functional                             |

---

### 📊 Dashboard View (User)

| ID     | Scenario Description                                                  | Expected Result                                              |
|--------|------------------------------------------------------------------------|---------------------------------------------------------------|
| WM-11  | Login as user and view dashboard                                      | All user-submitted requests are displayed                     |
| WM-12  | Filter requests by status = "Pending"                                | Only pending requests shown                                   |
| WM-13  | Filter by location = "Kisumu"                                        | Only Kisumu requests displayed                                |
| WM-14  | Combine filters: Location = Nairobi, Status = Completed              | Matching subset returned                                      |
| WM-15  | Reset filters                                                         | All requests are displayed again                              |
| WM-16  | No results found for filters                                          | Message: "No matching records found"                         |
| WM-17  | Try to view dashboard when logged out                                | Redirect to login                                            |
| WM-18  | UI handles long request lists (scrollable, paginated, or fluid)      | Table maintains structure                                    |

---

### ⚙️ Admin Panel – Request Management

| ID     | Scenario Description                                                  | Expected Result                                              |
|--------|------------------------------------------------------------------------|---------------------------------------------------------------|
| WM-19  | Login as admin and view request table                                | All user requests shown                                       |
| WM-20  | Select request and update status to "Scheduled"                     | Status updated; confirmation shown                            |
| WM-21  | Try updating status without selecting request                        | Button disabled or error shown                                |
| WM-22  | Admin tries to update status without selecting new status            | Button disabled or error shown                                |
| WM-23  | Admin updates same request multiple times                            | All changes persist and show correct latest status            |
| WM-24  | Check if status changes reflect on user dashboard                    | User dashboard shows updated status                          |
| WM-25  | Admin attempts form actions on mobile                                | Panel layout adapts correctly                                 |
| WM-26  | View system stats (total/pending/scheduled/completed)               | Counts match backend data                                     |

---

### 🛠️ Error Handling & UX

| ID     | Scenario Description                                                  | Expected Result                                              |
|--------|------------------------------------------------------------------------|---------------------------------------------------------------|
| WM-27  | Form submitted with slow or failing network                          | Error shown, form retryable                                   |
| WM-28  | Admin updates status while data table is being filtered              | Update still processed correctly                              |
| WM-29  | User dashboard table loads slowly with many entries                  | Loading indicator shown                                      |
| WM-30  | All error/success messages disappear on correction/submit            | Clean UX transition                                           |

---




**Prepared By:** QA Team, CleanCity  
**Date:** 2025-06-28  
**Status:** Complete

