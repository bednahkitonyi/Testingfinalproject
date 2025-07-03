## ✅ Revised and Testable Functional Requirements

This document provides rewritten versions of previously unclear or ambiguous functional requirements from the **CleanCity Functional Requirements Specification (FRS)**. A

---

### 📌 FR-031 – Blog System
- **The system shall provide a blog feature accessible to both users and admins.**
- **The system shall allow admins to create, edit, and delete blog posts.**
- **The system shall allow users to read and comment on blog posts.**
- **The blog feature shall support images and tags for categorization.**

---

### 📌 FR-014 – Time Slot Selection
- **The system shall generate available pickup time slots dynamically based on user location and current schedule availability.**
- **The system shall present pickup slots in hourly intervals between 8:00 AM and 5:00 PM.**
- **The system shall prevent users from selecting a fully booked time slot.**

---

### 📌 FR-020 – Real-Time Status Updates
- **The system shall update pickup request statuses every 30 seconds using polling or WebSocket technology.**
- **The system shall reflect changes made by admins to pickup requests in the user interface within 30 seconds.**

---

### 📌 FR-021 – Status Change Notifications
- **The system shall notify users of status changes via in-app notification and optional email alerts.**
- **The system shall allow users to configure their notification preferences.**
- **The system shall send notifications within 1 minute of a status update.**

---

### 📌 FR-028 – Data Export Functionality
- **The system shall allow users to export their pickup history, feedback, and environmental statistics in CSV format.**
- **The export feature shall be available from the user dashboard.**
- **The system shall allow users to filter data by date range prior to export.**

---

### 📌 FR-036 – Rotating Eco Tips
- **The system shall display eco tips on the homepage, rotating every 5 seconds in a carousel component.**
- **The system shall allow users to pause or manually scroll through tips.**
- **Eco tips shall be displayed in a random order on each page load.**

---

### 📌 FR-030 – Gamification Points and Levels
- **The system shall assign points for each completed activity (e.g., scheduling a pickup, completing a quiz, posting to the community feed).**
- **The system shall level up users based on cumulative points using a tiered formula (e.g., Level = Points / 100).**
- **The system shall display the user’s current points and level on their profile page.**

---

### 📌 FR-046 – User Activity History
- **The system shall record the following user activities: pickups scheduled, quizzes completed, posts shared, and badges earned.**
- **The system shall store activity history for a minimum of 12 months.**
- **The user activity history shall be accessible from the user profile page.**

---

### 📌 FR-065 – Notification Bell
- **The system shall display a notification bell on the header of all authenticated user pages.**
- **The bell shall show a badge with the count of unread notifications, updated in real-time.**
- **Clicking the bell shall display a dropdown list of the latest 20 notifications.**

---

### 📌 FR-078 – Local Storage and Persistence
- **The system shall use browser localStorage only for session tokens and user preferences.**
- **The system shall store all persistent user data (e.g., pickups, posts, profiles) in a secure backend database.**
- **The system shall synchronize local data with the server on login and logout.**

---
.

