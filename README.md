# 👥 Employee Management System (EMS) v2.0

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A robust, dark-themed desktop application built to streamline workplace administration. This system provides a centralized dashboard for managing employee records with local database persistence.

---

## 🌟 Key Features

- **🔐 Secure Access**: Integrated login system to prevent unauthorized data entry.
- **⚡ CRUD Operations**: Full capability to **Add, View, Update, and Delete** employee data.
- **🔍 Smart Search**: Real-time filtering system to locate staff by name or department instantly.
- **📊 Relational Storage**: Powered by **SQLite** for reliable and serverless data management.
- **🖥️ Responsive UI**: Clean, professional interface built with Python's **Tkinter** and `ttk` library.

---

## 📂 Project Architecture

The project is structured into modular components for easier maintenance:

| File | Responsibility |
| :--- | :--- |
| **`main.py`** | The application launcher and initial entry point. |
| **`login.py`** | Handles user authentication and session startup. |
| **`employee.py`** | The core dashboard UI and management logic. |
| **`emp.py`** | Database abstraction layer (SQL queries). |
| **`employee.db`** | Local SQLite database file. |

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python 3.x installed. No external pip installations are required as it uses standard libraries.

### 2. Run the App
Clone this repository and run the main script:
```bash
python main.py
