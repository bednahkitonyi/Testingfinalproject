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

### 📝 Pickup Request Form (User)

**TC-WM-01** – Submit form with valid inputs  
**Preconditions:** User is logged in  
**Steps:**  
1. Open form  
2. Fill in name, location, waste type, preferred date  
3. Submit  
**Test Data:** Name: John Doe, Location: Nairobi, Type: Plastic, Date: Tomorrow  
**Expected Result:** Confirmation message: "Request submitted successfully"

**TC-WM-02** – Submit without selecting location  
**Preconditions:** User is logged in  
**Steps:** Fill in name and waste type, leave location blank, then submit  
**Test Data:** Name: Jane Doe, Waste Type: Organic  
**Expected Result:** Error: "Location is required"

**TC-WM-03** – Submit without selecting waste type  
**Preconditions:** User is logged in  
**Steps:** Fill in name and location, leave waste type blank, then submit  
**Test Data:** Name: Jane Doe, Location: Kisumu  
**Expected Result:** Error: "Waste Type is required"

**TC-WM-04** – Submit without full name  
**Preconditions:** User is logged in  
**Steps:** Fill in location and waste type, leave name blank, then submit  
**Test Data:** Location: Kisumu, Waste Type: Plastic  
**Expected Result:** Error: "Full Name is required"

**TC-WM-05** – Submit all fields blank  
**Preconditions:** User is logged in  
**Steps:** Open form and click submit with all fields empty  
**Expected Result:** Multiple error messages for each required field

**TC-WM-06** – Select a past pickup date  
**Preconditions:** User is logged in  
**Steps:** Fill in all fields and select a date in the past, then submit  
**Test Data:** Date: Yesterday  
**Expected Result:** Error: "Date must be in the future" or auto-adjust

**TC-WM-07** – Use special characters in name  
**Preconditions:** User is logged in  
**Steps:** Fill in form with name containing special characters and submit  
**Test Data:** Name: @John*#  
**Expected Result:** Submission successful, characters stored correctly

**TC-WM-08** – Submit duplicate request  
**Preconditions:** User is logged in  
**Steps:** Submit the same name and date twice  
**Test Data:** John Doe, 2025-07-04  
**Expected Result:** System prevents or handles duplicate gracefully

**TC-WM-09** – Submit while logged out  
**Preconditions:** User is logged out  
**Steps:** Open form and try to submit  
**Expected Result:** Redirect to login or error: "You must be logged in"

**TC-WM-10** – Submit via mobile browser  
**Preconditions:** Use mobile browser or emulator  
**Steps:** Fill out and submit form  
**Test Data:** Valid form inputs  
**Expected Result:** Form is responsive and functional

---

### 📊 Dashboard View (User)

**TC-WM-11** – View dashboard  
**Preconditions:** User logged in  
**Steps:** Navigate to dashboard  
**Expected Result:** List of all user’s requests shown

**TC-WM-12** – Filter by status "Pending"  
**Preconditions:** Mixed-status requests exist  
**Steps:** Select filter: Pending  
**Expected Result:** Only pending requests shown

**TC-WM-13** – Filter by location "Kisumu"  
**Preconditions:** Kisumu and other requests exist  
**Steps:** Select filter: Location = Kisumu  
**Expected Result:** Only Kisumu records displayed

**TC-WM-14** – Combine location & status filters  
**Preconditions:** Completed Nairobi requests exist  
**Steps:** Set filters: Location = Nairobi, Status = Completed  
**Expected Result:** Matching records shown

**TC-WM-15** – Reset filters  
**Preconditions:** Filters are applied  
**Steps:** Click reset  
**Expected Result:** All requests shown again

**TC-WM-16** – No results for filters  
**Preconditions:** Filter will return no results  
**Steps:** Select unmatched filter e.g., Location = Mars  
**Expected Result:** Message: "No matching records found"

**TC-WM-17** – View dashboard logged out  
**Preconditions:** User is logged out  
**Steps:** Go to dashboard URL  
**Expected Result:** Redirect to login page

**TC-WM-18** – Handle many entries  
**Preconditions:** Many records exist  
**Steps:** Open dashboard  
**Expected Result:** UI supports pagination or scroll properly

---

### ⚙️ Admin Panel – Request Management

**TC-WM-19** – View admin request table  
**Preconditions:** Admin is logged in  
**Steps:** Navigate to admin panel  
**Expected Result:** All user requests shown

**TC-WM-20** – Update status to "Scheduled"  
**Preconditions:** Request exists  
**Steps:** Select a request, change status to Scheduled, click Save  
**Expected Result:** Status updated, confirmation shown

**TC-WM-21** – Update without selecting request  
**Steps:** Click update without selecting any request  
**Expected Result:** Error or disabled update button

**TC-WM-22** – Update without selecting new status  
**Preconditions:** A request is selected  
**Steps:** Click update without choosing new status  
**Expected Result:** Error: "Please select status"

**TC-WM-23** – Multiple updates on same request  
**Preconditions:** Request exists  
**Steps:** Change status multiple times  
**Expected Result:** All changes saved correctly

**TC-WM-24** – Status reflects on user dashboard  
**Preconditions:** Admin updates request  
**Steps:** User views dashboard  
**Expected Result:** Updated status visible to user

**TC-WM-25** – Admin on mobile view  
**Steps:** Open admin panel on mobile  
**Expected Result:** Layout is responsive and usable

**TC-WM-26** – View system stats  
**Preconditions:** System has data  
**Steps:** View stats panel  
**Expected Result:** Stats match backend data

---

### 🛠️ Error Handling & UX

**TC-WM-27** – Submit with poor network  
**Preconditions:** Simulate slow network  
**Steps:** Submit the form  
**Expected Result:** Error or retry option shown

**TC-WM-28** – Admin updates while filtering  
**Preconditions:** Data table is filtered  
**Steps:** Update a request status  
**Expected Result:** Update still processed correctly

**TC-WM-29** – Dashboard loads slowly  
**Preconditions:** Many entries  
**Steps:** Open dashboard  
**Expected Result:** Loading indicator shown

**TC-WM-30** – Messages disappear after action  
**Preconditions:** Error or success triggered  
**Steps:** Fix form or wait  
**Expected Result:** Messages fade or clear smoothly



**Prepared By:** QA Team, CleanCity  
**Date:** 2025-06-28  
**Status:** Complete

