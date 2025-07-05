## 🧪 Test Cases for Authentication System – CleanCity Web App

# 📄 Introduction

This document outlines the comprehensive set of test cases designed to validate the functionality, performance, and reliability of the application under test. Each test case has been developed based on the system’s requirements and user expectations to ensure that all features behave as intended across various scenarios. 

The test cases cover both **functional** and **non-functional** aspects of the system, enabling consistent quality assurance and traceability throughout the testing lifecycle.

---

### 🔐 Registration Test Cases

#### ✅ TC-R-01: Register with Valid Inputs
- **Preconditions:** User is on the Register page
- **Test Steps:**
  1. Enter full name: "Jane Doe"
  2. Enter email: "user1@test.com"
  3. Enter password: "TestPass123"
  4. Confirm password: "TestPass123"
  5. Click "Register" button
- **Expected Result:** Account is successfully created; user redirected to login with a success message

#### ❌ TC-R-02: Missing Name Field
- **Test Steps:**
  1. Leave the name field blank
  2. Enter email: "user1@test.com"
  3. Enter password: "TestPass123"
  4. Confirm password: "TestPass123"
  5. Click "Register" button
- **Expected Result:** Error displayed: "Full Name is required"

#### ❌ TC-R-03: Email Already Exists
- **Test Steps:**
  1.Enter full name: "Jane Doe"
  2. Use an existing email: "user1@cleancity.com"
  3.Enter password: "TestPass123".
  4.Confirm password: "TestPass123"
  4. Click "Register" button
  
- **Expected Result:** Error displayed: "Email already exists"

#### ❌ TC-R-04: Password Mismatch
- **Test Steps:**
  1. Enter full name: "Jane Doe"
  2. Enter email: "user1@test.com"
  3. Enter password: "TestPass123"
  4. Confirm password: "123abc"
  5. Click "Register" button
- **Expected Result:** Error displayed: "Passwords do not match"

#### ❌ TC-R-05: Password Too Short
- **Test Steps:**
  1. Enter full name: "Jane Doe"
  2. Enter email: "user1@test.com"
  3. Enter password: "TestPass"
  4. Confirm password: "TestPass"
  5. Click "Register" button
     
- **Expected Result:** Error: "Password must be at least 3 characters"

#### ❌ TC-R-06: Invalid Email Format
- **Test Steps:**
  1. Enter full name: "Jane Doe"
  2. Enter email: "user1@test"
  4. Enter password: "TestPass123"
  5. Confirm password: "TestPass123"
  6. Click "Register" button
     
- **Expected Result:** Error: "Invalid email address"

---

### 🔐 Login Test Cases

#### ✅ TC-L-01: Valid User Login
- **Test Steps:**
  1. Go to login page
  2. Enter: Email: "user@cleancity.com"
  3. Enter Password: "TestPass123"
  4. Click "Login" button
- **Expected Result:** Redirect to Dashboard; user-specific links shown

#### ✅ TC-L-02: Valid Admin Login
- **Test Steps:**
  1. Enter: Email: "admin@cleancity.com"
  2. Password: "admin123"
  3. Click "Login" button
- **Expected Result:** Redirect to Dashboard; admin panel link is visible

#### ❌ TC-L-03: Wrong Password
- **Test Steps:**
  1. Enter valid registered user email e.g user1@test.com
  2. Enter incorrect password e.g "Test"
  3. Click "Login" button
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-04: Non-Existent Email
- **Test Steps:**
  1. Enter unused email e.g "user@test"
  2. Enter any password
  3. Click "Login" button
     
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-05: Empty Email
- **Test Steps:**
  1. Leave email blank
  2. Enter valid password e.g "TestPass123"
  3. Click "Login" button
- **Expected Result:** Error: "Email is required"

#### ❌ TC-L-06: Empty Password
- **Test Steps:**
  1. Enter valid registered email e.g "user1@test.com"
  2. Leave password blank
  3. Click "Login" button
     
- **Expected Result:** Error: "Password is required"

#### ❌ TC-L-07: SQL Injection Attempt
- **Test Steps:**
  1. Enter `admin@cleancity.com`
  2. Password `' OR 1=1 --`
  3. Submit
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
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
7. Select waste type (e.g., Recyclable)
8. Choose future pick date  e.g "12/07/2025"
9. Enter any additional description  
10. Click "Submit request" button
      
**Expected Result:** Pickup is scheduled successfully

### ❌ TC-002: Attempt to Schedule Pickup with Past Date
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Enter a past date e.g "1/07/2025"
7. Enter any additional description  
8. Click "Submit request" button
**Expected Result:** Error message displayed – date must be in the future

### ❌ TC-003: Schedule Pickup Without Selecting Waste Type
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
5. leave the Select waste type empty
6. Enter a future date e.g "11/07/2025"
7. Enter any additional description  
8. Click "Submit request" button
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



# 🧪 Gamification Test Cases

---

## ✅ Positive Test Cases

---

#### 1. Award badge for first pickup scheduled

 **Precondition:** The user has no previous pickups.

 **Steps:**
  1. Login to the application using valid credentials.
  2. Navigate to the **Pickup** section.
  3. Schedule a new pickup with valid details.
  4. Submit the pickup request.
  5. Navigate to the **Badges** section.

 **Expected Result:**  A badge labeled **"First Pickup Scheduled"** is awarded and visible.

---

#### 2. Award badge after 10 pickups completed

 **Precondition:** The user has already completed 9 pickups.

 **Steps:**
  1. Login to the application.
  2. Schedule and complete one more pickup.
  3. Return to the dashboard or profile.
  4. Navigate to **Badges** section.

 **Expected Result:**  **"10 Pickups Completed"** badge appears in the user's badge list.

---

#### 3. Award badge for perfect recycling score

 **Precondition:** Recycling score logic is implemented.

 **Steps:**
  1. Login to the application.
  2. Schedule a pickup with correctly sorted recyclables.
  3. Submit the pickup.
  4. Check recycling score on the dashboard.
  5. Open **Badges** section.

 **Expected Result:**  Badge for **"Perfect Recycling Score"** is displayed.

---

#### 4. Award badge for community contributor

 **Precondition:** User participates in community activities (e.g., referrals).

 **Steps:**
  1. Login to the application.
  2. Refer a new user or join a community cleanup event.
  3. Complete the qualifying community action.
  4. Visit the **Badges** section.

 **Expected Result:**  **"Community Contributor"** badge is awarded.

---

#### 5. Award points for completed pickup

**Precondition:** Point awarding logic is enabled.

 **Steps:**
  1. Login to the application.
  2. Schedule and complete a pickup.
  3. Navigate to the user profile or dashboard.

 **Expected Result:** Points are added to the user's total.

---

#### 6. Level increases after reaching point threshold

 **Precondition:** User is close to leveling up (e.g., 95/100 points).

 **Steps:**
  1. Complete an activity that awards sufficient points.
  2. Refresh the dashboard or profile page.

 **Expected Result:**  User’s level increases and reflects the new level.

---

#### 7. View current level and points in profile

 **Precondition:** User has accumulated some points.

 **Steps:**
  1. Login to the application.
  2. Navigate to the user profile.
  3. Locate the points and level section.

**Expected Result:** Current point total and level are displayed.

---

## ❌ Negative Test Cases

---

#### 8. Badge is awarded multiple times for the same event

 **Precondition:** User has already earned the **"First Pickup Scheduled"** badge.

 **Steps:**
  1. Schedule another pickup.
  2. Refresh the badge section.

 **Expected Result:**  **"First Pickup Scheduled"** badge is not duplicated.

---

#### 9. User receives points without valid activity

 **Precondition:** API or frontend vulnerability.

 **Steps:**
  1. Attempt to manipulate point API via console or external tool.

 **Expected Result:** System rejects the manipulation; points remain unchanged.

---

#### 10. Level does not update correctly after rollback

**Precondition:** Points rollback due to admin correction.

 **Steps:**
  1. Admin reduces user points below threshold.
  2. User logs in and checks level.

 **Expected Result:** Level reflects reduced points accurately.

---

#### 11. Badge awarded without completing valid community action

 **Steps:**
  1. Attempt to claim community badge without doing referral.
  2. Reload badge list.

 **Expected Result:** Community badge is not awarded.

---

## 🎨 UI/UX Test Cases

---

#### 12. Badge icons are unique and well labeled

 **Steps:**
  1. Navigate to **Badges** section.

 **Expected Result:** Each badge has unique icons and labels.

---

#### 13. Points and levels use consistent styles and colors

 **Steps:**
  1. View dashboard and profile.

 **Expected Result:**  Progress bar and colors match level progression.

---

#### 14. Responsive badge and level display on mobile devices

 **Steps:**
  1. Open app on mobile or resize browser.
  2. View badges and level display.

**Expected Result:**  All elements adjust without overflow or distortion.


