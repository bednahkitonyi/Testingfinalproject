# 🌐 CleanCity Web App – Test Environment Specification

## 📌 Purpose
This document defines the configuration and components of the test environments required for validating the CleanCity Waste Pickup Scheduler Web Application by the QA Team.

---

## 🧪 Environment Types

| Environment | Purpose                          | URL                             |
|-------------|----------------------------------|----------------------------------|
| Staging     | QA & UAT testing (pre-production)| `http://localhost:3000`  |
| Production  | Live user deployment             | `http://localhost:3000`  |

---

## 🖥️ Hardware and Devices

### Desktop
- **Windows 10/11**: Chrome, Firefox, Edge
- **macOS Monterey/Ventura**: Safari, Chrome

### Mobile
- **Android 11/12/13**: Chrome (Pixel, Samsung Galaxy)
- **iOS 15/16**: Safari and Chrome (iPhone SE, XR, 13)

### Tablet (Optional)
- **iPad (iOS 15+)**: Safari
- **Android Tablets**: Chrome

---

## 🌍 Browsers and Versions

| Browser  | Minimum Version |
|----------|------------------|
| Chrome   | 114+             |
| Firefox  | 115+             |
| Safari   | 15+              |
| Edge     | 113+             |

> 💡 All tests will be validated on latest stable releases unless otherwise stated.

---

## ⚙️ Software Stack & Dependencies

| Layer        | Technology                         |
|--------------|-------------------------------------|
| Frontend     | HTML, CSS, JavaScript               |
| Framework    | Vanilla JS + DOM manipulation       |
| Backend API  | (Assumed integrated via REST calls) |
| Data Storage | JSON (client-side simulation)       |
| Test Tools   | Chrome DevTools, Postman, JIRA      |
| Automation   | (Optional) Cypress / Playwright     |

---

## 🔐 Test Data

### User Accounts
- **Regular User:**  
  - Email: `user@cleancity.com`  
  - Password: `password123`

- **Admin User:**  
  - Email: `admin@cleancity.com`  
  - Password: `admin123`

### Sample Pickup Requests
- Request IDs: `REQ001` to `REQ005` (used in dashboard and feedback tests)

---

## 🔧 Configuration

- **Screen Resolution:**  
  - Minimum: 360px width (mobile)  
  - Maximum: 1920x1080 (desktop)

- **Timezone:**  
  - GMT+3 (East Africa Time – default for Nairobi)

- **Network Simulation:**  
  - 4G, offline, and slow 3G tested via Chrome DevTools

- **Browser Storage:**  
  - LocalStorage or SessionStorage used for session simulation

---

## 🧹 Environment Management

| Task                      | Owner            | Notes                                 |
|---------------------------|------------------|----------------------------------------|
| Environment Setup         | QA Team          | Ensure staging mirrors production      |
| Credential Management     | QA Team         | Stored in secure vault/shared doc      |
| Data Refresh/Cleanup      | QA Team      | Before each test cycle                 |
| Test Logging & Reporting  | QA Team       | Via Notion, JIRA, or Excel reports     |

---

## 📋 Validation Checklist

- [x] Navigation works across all devices
- [x] API endpoints reachable in staging
- [x] Test data reset before major regression
- [x] Cross-browser rendering confirmed
- [x] Admin panel access restricted by role

---

**Document Version:** 1.0  
**Prepared By:** QA Team, CleanCity  
**Last Updated:** 2025-07-05  
**Status:** ✅ Approved for testing
