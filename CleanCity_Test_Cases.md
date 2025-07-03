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

# 🧪 Test Cases for Waste Management System

## 4.1 Pickup Scheduling

### ✅ TC-001: Schedule a Pickup with Valid Inputs
1. Navigate to scheduling page  
2. Enter future date  
3. Select waste type (e.g., Recyclable)  
4. Choose quantity (e.g., Medium)  
5. Enter special instructions (optional)  
6. Verify address is auto-filled  
7. Submit request  
**Expected Result:** Pickup is scheduled successfully

### ❌ TC-002: Attempt to Schedule Pickup with Past Date
1. Enter a past date  
2. Fill all other valid details  
3. Submit request  
**Expected Result:** Error message displayed – date must be in the future

### ❌ TC-003: Schedule Pickup Without Selecting Waste Type
1. Leave waste type empty  
2. Fill all other fields  
3. Submit request  
**Expected Result:** Error message – waste type is required

### ❌ TC-004: Schedule Pickup Without Quantity
1. Leave quantity empty  
2. Fill other fields  
3. Submit request  
**Expected Result:** Error message – quantity is required

### ❌ TC-005: Schedule Pickup With Too Long Special Instructions
1. Enter 201+ characters in special instructions  
2. Fill other fields  
3. Submit request  
**Expected Result:** Error message – max 200 characters allowed

### ❌ TC-006: Pickup Date Less Than 24 Hours Away
1. Select a date less than 24 hours in future  
2. Fill all required fields  
3. Submit request  
**Expected Result:** Validation error – must be at least 24 hours in advance

### ✅ TC-007: View Available Time Slots
1. Go to scheduling page  
2. Choose valid pickup date  
**Expected Result:** Available time slots are displayed

### ❌ TC-008: Schedule Multiple Pickups on Same Date
1. Schedule a pickup for a given date  
2. Attempt to schedule another pickup for same date  
**Expected Result:** Error – only one pickup per date allowed

---

## 4.2 Request Management

### ✅ TC-009: View Pickup Request History
1. Log in  
2. Go to request history  
**Expected Result:** List of all past pickup requests displayed

### ✅ TC-010: Cancel Pending Pickup Request
1. Select a pending request  
2. Click cancel  
**Expected Result:** Status changes to Cancelled

### ✅ TC-011: Modify Request More Than 24 Hours in Advance
1. Select request with pickup time more than 24 hours away  
2. Update details (e.g., quantity)  
**Expected Result:** Details updated successfully

### ❌ TC-012: Modify Request Less Than 24 Hours in Advance
1. Select request with pickup time less than 24 hours away  
2. Attempt to modify details  
**Expected Result:** Error – modification not allowed

### ✅ TC-013: Check Status Display for Request
1. View request list  
**Expected Result:** Each request shows status (Pending, Confirmed, Completed, Cancelled)

---

## 4.3 Request Tracking

### ✅ TC-014: Real-time Status Update
1. Submit pickup request  
2. Trigger status change in system (e.g., Confirmed)  
**Expected Result:** Status updates reflect immediately in UI

### ✅ TC-015: Notification on Status Change
1. Submit request  
2. System updates status  
**Expected Result:** Notification received (email, push, etc.)

### ✅ TC-016: Add Feedback After Completion
1. Wait for pickup completion  
2. Navigate to feedback section  
3. Submit feedback  
**Expected Result:** Feedback is recorded successfully


**Prepared By:** QA Team, CleanCity  
**Date:** 2025-06-28  
**Status:** Complete

