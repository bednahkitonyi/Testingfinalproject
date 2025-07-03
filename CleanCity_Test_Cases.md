## 🧪 Test Cases for Authentication System – CleanCity Web App

### 📌 Objective
Translate authentication test scenarios into detailed, step-by-step test cases for manual execution.

---

### 🔐 Registration Test Cases

#### ✅ TC-R-01: Register with Valid Inputs
- **Preconditions:** User is on the Register page
- **Test Steps:**
  1. Enter full name: "Jane Doe"
  2. Enter email: "jane@example.com"
  3. Enter password: "password123"
  4. Confirm password: "password123"
  5. Click "Create Account"
- **Expected Result:** Account is successfully created; user redirected to login with a success message

#### ❌ TC-R-02: Missing Name Field
- **Test Steps:**
  1. Leave the name field blank
  2. Fill other fields correctly
  3. Click "Create Account"
- **Expected Result:** Error displayed: "Full Name is required"

#### ❌ TC-R-03: Email Already Exists
- **Test Steps:**
  1. Use an existing email: "user@cleancity.com"
  2. Fill other fields
  3. Submit form
- **Expected Result:** Error displayed: "Email already exists"

#### ❌ TC-R-04: Password Mismatch
- **Test Steps:**
  1. Enter password: "abc123"
  2. Confirm password: "123abc"
  3. Submit form
- **Expected Result:** Error displayed: "Passwords do not match"

#### ❌ TC-R-05: Password Too Short
- **Test Steps:**
  1. Enter password: "ab"
  2. Submit form
- **Expected Result:** Error: "Password must be at least 3 characters"

#### ❌ TC-R-06: Invalid Email Format
- **Test Steps:**
  1. Enter email: "jane@com"
  2. Submit form
- **Expected Result:** Error: "Invalid email address"

---

### 🔐 Login Test Cases

#### ✅ TC-L-01: Valid User Login
- **Test Steps:**
  1. Go to login page
  2. Enter: Email: "user@cleancity.com" | Password: "password123"
  3. Click "Sign In"
- **Expected Result:** Redirect to Dashboard; user-specific links shown

#### ✅ TC-L-02: Valid Admin Login
- **Test Steps:**
  1. Enter: Email: "admin@cleancity.com" | Password: "admin123"
  2. Click "Sign In"
- **Expected Result:** Redirect to Dashboard; admin panel link is visible

#### ❌ TC-L-03: Wrong Password
- **Test Steps:**
  1. Enter valid email
  2. Enter incorrect password
  3. Submit
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-04: Non-Existent Email
- **Test Steps:**
  1. Enter unused email
  2. Submit with any password
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-05: Empty Email
- **Test Steps:**
  1. Leave email blank
  2. Enter valid password
  3. Submit
- **Expected Result:** Error: "Email is required"

#### ❌ TC-L-06: Empty Password
- **Test Steps:**
  1. Enter valid email
  2. Leave password blank
  3. Submit
- **Expected Result:** Error: "Password is required"

#### ❌ TC-L-07: SQL Injection Attempt
- **Test Steps:**
  1. Enter `admin@cleancity.com` and password `' OR 1=1 --`
  2. Submit
- **Expected Result:** Login blocked; generic error shown

---

### 🚪 Logout Test Cases

#### ✅ TC-LO-01: Logout from Logged-In State
- **Precondition:** User is logged in
- **Test Steps:**
  1. Click on Logout
- **Expected Result:** Session ends; redirected to login page

#### ✅ TC-LO-02: Hide Logout for Guest
- **Test Steps:**
  1. Access app without logging in
- **Expected Result:** Logout button is not visible

#### ✅ TC-LO-03: Logout via URL as Guest
- **Test Steps:**
  1. Access logout endpoint manually in browser
- **Expected Result:** Redirected to login/homepage; no error

---

### 👮‍♂️ Access Control Test Cases

#### ✅ TC-A-01: Admin Sees Admin Panel
- **Test Steps:**
  1. Login as admin
  2. Check navigation bar
- **Expected Result:** "Admin" link is visible

#### ✅ TC-A-02: Regular User Cannot See Admin Panel
- **Test Steps:**
  1. Login as regular user
  2. Check nav links
- **Expected Result:** Admin link is hidden

#### ❌ TC-A-03: Direct Dashboard Access by Guest
- **Test Steps:**
  1. Visit `/dashboard` without logging in
- **Expected Result:** Redirect to login

#### ❌ TC-A-04: Regular User Accessing Admin Panel URL
- **Test Steps:**
  1. Copy admin URL and visit as regular user
- **Expected Result:** Access denied or redirected

---

### 🧪 UI & Usability Test Cases

#### ✅ TC-UI-01: Placeholder Texts Exist
- **Test Steps:**
  1. Check email and password fields
- **Expected Result:** Placeholder like "Enter your email" visible

#### ✅ TC-UI-02: Required Fields Indicator
- **Test Steps:**
  1. Check label next to required fields
- **Expected Result:** Asterisk (*) shown

#### ✅ TC-UI-03: Field Tab Navigation
- **Test Steps:**
  1. Use Tab key to move between fields
- **Expected Result:** Order flows logically

#### ✅ TC-UI-04: Password Masking
- **Test Steps:**
  1. Type password
- **Expected Result:** Dots shown instead of visible text

#### ✅ TC-UI-05: Responsive Layout
- **Test Steps:**
  1. Load form on mobile browser
- **Expected Result:** All inputs and buttons are usable

---

## ✅ Test Cases for Waste Management Module – CleanCity Web App


---

## 📝 Section 1: Pickup Request Form (User)

| **Test Case ID** | **Scenario**                               | **Preconditions**       | **Steps**                                                                 | **Test Data**                                      | **Expected Result**                                      |
|------------------|--------------------------------------------|--------------------------|---------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------|
| TC-WM-01         | Submit form with valid inputs              | User is logged in        | 1. Open form<br>2. Fill in name, location, type, date<br>3. Submit       | Name: John Doe<br>Location: Nairobi<br>Type: Plastic<br>Date: Tomorrow | Confirmation: "Request submitted successfully"           |
| TC-WM-02         | Submit without selecting location          | User is logged in        | Fill in name and waste type, leave location blank, then submit          | Name: Jane Doe<br>Waste Type: Organic              | Error: "Location is required"                            |
| TC-WM-03         | Submit without selecting waste type        | User is logged in        | Fill in name and location, leave waste type blank, then submit          | Name: Jane Doe<br>Location: Kisumu                 | Error: "Waste Type is required"                          |
| TC-WM-04         | Submit without full name                   | User is logged in        | Fill in location and waste type, leave name blank, then submit          | Location: Kisumu<br>Waste Type: Plastic            | Error: "Full Name is required"                           |
| TC-WM-05         | Submit all fields blank                    | User is logged in        | Open form and click submit with all fields empty                        | –                                                  | Multiple error messages shown                            |
| TC-WM-06         | Select a past pickup date                  | User is logged in        | Fill in all fields, select a past date, then submit                     | Date: Yesterday                                    | Error or auto-adjust to future date                     |
| TC-WM-07         | Use special characters in name             | User is logged in        | Fill in name with special characters, then submit                       | Name: @John*#                                      | Submission successful, characters stored correctly       |
| TC-WM-08         | Submit duplicate request                   | User is logged in        | Submit same name and date twice                                         | Name: John Doe<br>Date: 2025-07-04                 | System handles duplicates gracefully                     |
| TC-WM-09         | Submit while logged out                    | User is logged out       | Open form and attempt to submit                                         | –                                                  | Redirect to login or error: "You must be logged in"      |
| TC-WM-10         | Submit via mobile browser                  | Mobile browser used      | Fill and submit form                                                    | Valid form inputs                                  | Form is responsive and works properly                    |

---

## 📊 Section 2: Dashboard View (User)

| **Test Case ID** | **Scenario**                               | **Preconditions**       | **Steps**                                            | **Expected Result**                                 |
|------------------|--------------------------------------------|--------------------------|------------------------------------------------------|-----------------------------------------------------|
| TC-WM-11         | View dashboard                             | User is logged in        | Navigate to dashboard                                | List of user's requests shown                       |
| TC-WM-12         | Filter by status "Pending"                 | Mixed-status requests     | Apply filter: Status = Pending                       | Only pending requests displayed                     |
| TC-WM-13         | Filter by location "Kisumu"                | Kisumu + other records    | Filter: Location = Kisumu                            | Only Kisumu records displayed                       |
| TC-WM-14         | Combine location & status filters          | Completed Nairobi records | Filter: Nairobi + Completed                          | Matching requests displayed                         |
| TC-WM-15         | Reset filters                              | Filters are applied       | Click reset                                          | All requests re-displayed                           |
| TC-WM-16         | No results for filters                     | No matching entries       | Apply unmatched filter (e.g., Location = Mars)       | Message: "No matching records found"                |
| TC-WM-17         | View dashboard while logged out            | User is logged out        | Access dashboard URL                                 | Redirect to login page                              |
| TC-WM-18         | Handle many entries                        | Many records exist        | Open dashboard                                       | Pagination or scrollable UI displayed               |

---

## ⚙️ Section 3: Admin Panel – Request Management

| **Test Case ID** | **Scenario**                               | **Preconditions**       | **Steps**                                                        | **Expected Result**                                   |
|------------------|--------------------------------------------|--------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| TC-WM-19         | View admin request table                   | Admin is logged in       | Navigate to admin panel                                          | All user requests listed                             |
| TC-WM-20         | Update status to "Scheduled"               | Request exists            | Select request, change status, click Save                        | Status updated with confirmation                     |
| TC-WM-21         | Update without selecting a request         | –                        | Click update with no request selected                            | Error or disabled update button                      |
| TC-WM-22         | Update without selecting new status        | A request is selected     | Try updating without selecting new status                        | Error: "Please select status"                        |
| TC-WM-23         | Multiple updates on same request           | Request exists            | Change status multiple times                                     | All changes saved correctly                          |
| TC-WM-24         | Status reflects on user dashboard          | Admin updates request     | User checks dashboard                                            | Updated status is visible                            |
| TC-WM-25         | Admin view on mobile                       | –                        | Open admin panel on mobile device                                | Layout remains responsive                            |
| TC-WM-26         | View system statistics                     | System contains data      | Navigate to stats section                                        | Stats match backend values                           |

---

## 🛠️ Section 4: Error Handling & UX

| **Test Case ID** | **Scenario**                               | **Preconditions**       | **Steps**                                    | **Expected Result**                              |
|------------------|--------------------------------------------|--------------------------|----------------------------------------------|--------------------------------------------------|
| TC-WM-27         | Submit with poor network                   | Simulate slow connection | Submit form                                   | Error or retry option shown                      |
| TC-WM-28         | Admin updates while filtering              | Data table is filtered    | Update status of a request                    | Update still processed correctly                 |
| TC-WM-29         | Dashboard loads slowly                     | Many records exist        | Open dashboard                                | Loading indicator shown                          |
| TC-WM-30         | Messages disappear after action            | Error or success occurs   | Wait or fix issue                             | Messages fade/clear automatically                |


**Prepared By:** QA Team, CleanCity  
**Date:** 2025-06-28  
**Status:** Complete

