## 🕵️ Unclear or Ambiguous Functional Requirements

This document outlines the functional requirements from the **CleanCity Functional Requirements Specification (FRS)** that are unclear or ambiguous. These should be reviewed and refined to ensure clarity, completeness, and testability.

---

### 📌 Blog System (Section 6.1)
- **Issue:** Requirements not numbered (e.g., FR-031–FR-035 missing).
- **Ambiguity:** Uses "should" instead of "shall".
- **Missing:**
  - Permissions for post creation/editing.
  - Media support (images, video).
  - Types of interaction (likes, shares, comments).

---

### 📌 FR-014 – Pickup Time Slots
- **Issue:** Vague presentation of time slot behavior.
- **Ambiguity:**
  - Are time slots dynamic or static?
  - Are they based on user location or system availability?
  - What time formats are used (hourly, AM/PM)?

---

### 📌 FR-020 – Real-Time Status Updates
- **Issue:** "Real-time" not clearly defined.
- **Ambiguity:**
  - What technology is used (WebSockets, polling)?
  - How often are updates pushed?
  - Who triggers status updates?

---

### 📌 FR-021 – Status Change Notifications
- **Issue:** Notification channels not specified.
- **Ambiguity:**
  - Are notifications sent via email, SMS, in-app?
  - Can users configure their preferences?
  - Notification delays?

---

### 📌 FR-028 – Data Export
- **Issue:** Export scope unclear.
- **Ambiguity:**
  - Which data is included (e.g., pickups, stats)?
  - Who can export (users vs admins)?
  - Are filters/selective exports supported?

---

### 📌 FR-036 – Rotating Eco Tips
- **Issue:** Display context not defined.
- **Ambiguity:**
  - Where are tips shown (dashboard, homepage)?
  - Can rotation be paused?
  - How are tips selected (random, order)?

---

### 📌 FR-030 – Points and Levels
- **Issue:** Gamification logic missing.
- **Ambiguity:**
  - What actions earn points?
  - Formula for leveling up?
  - User visibility of point history?

---

### 📌 FR-046 – Activity History
- **Issue:** Scope of activity tracking not defined.
- **Ambiguity:**
  - Which activities are recorded (pickups, logins)?
  - How far back is data retained?

---

### 📌 FR-065 – Notification Bell
- **Issue:** Interface details unclear.
- **Ambiguity:**
  - Is the bell on all pages or only dashboard?
  - Are unread counts updated in real-time?

---

### 📌 FR-078 – Data in localStorage
- **Issue:** Unrealistic design implication.
- **Ambiguity:**
  - Does this imply no backend database?
  - How is data synchronized across users?
  - What about sensitive data or persistence limits?

---


