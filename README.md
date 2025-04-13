# ♻️ ZeroWaste – Geo-Intelligent Food Donation & Rescue System

## 📌 Selected Domain:
**Social Good / Waste Management / Food Distribution**

---

## ❗ Problem Statement

Every day, millions of tons of edible food are wasted, while millions of people remain hungry. A major barrier to effective food rescue is the lack of a simple, accessible, real-time system for connecting food donors (like individuals, restaurants, and stores) with receivers (such as shelters, NGOs, and individuals in need).

---

## 📝 Problem Description

The current food donation processes are often manual, disorganized, or restricted to large institutions. There's a need for a **lightweight, location-based web platform** where:

- Donors can quickly post food availability.
- Receivers can request food without long procedures.
- Both parties can coordinate pickups based on **geolocation**.
- The process should be **mobile-friendly**, require **minimal setup**, and show **submission success instantly**.

---

## 💡 Project Objective

The **ZeroWaste** project aims to build a clean, fast, and geolocation-powered platform that:

- Encourages **easy food donation** from individuals or organizations.
- Helps **receivers locate nearby donations** in real time.
- Enables location tracking using **HTML + JavaScript Geolocation API**.
- Displays **success feedback** after every form submission for clarity.
- Provides a structured foundation for future enhancements like admin panels and food distribution maps.

---

## 🛠️ Tech Stack Used

### 🧩 Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)
- Geolocation API
- Google Fonts (Roboto, Poppins)

### ⚙️ Backend
- Python 3.x
- Flask (Micro web framework)
- Flask-CORS (to enable frontend-backend communication)

---

## 💻 Project Explanation

This project includes the following:

### ➤ `index.html`
- A landing page with navigation to all other panels.

### ➤ `donor.html`
- A form for donors to enter:
  - Food details (type, quantity, deadline)
  - Perishability status
  - Upload food image
  - Auto-detect current location
- On submission, it redirects to `success.html`.

### ➤ `receiver.html`
- A form for receivers to enter:
  - Name, email, food preference, quantity
  - Auto-detect or manually enter location
  - Optional document upload
- On submission, it redirects to `success.html`.

### ➤ `success.html`
- Displays a clean success message: “Your request was submitted successfully!”

### ➤ `donor_api.py`
- Python Flask API to handle:
  - Donor form (`/submit-donor`)
  - Receiver form (`/submit-receiver`)
  - Success response

---

