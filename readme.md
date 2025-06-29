# 🧾 Client Retainer Tracker

A complete client retainer tracking system built using **Python**, **Pandas**, **Streamlit**, and **Excel automation**. Designed to help freelancers, agencies, and service providers monitor client payments, identify overdue accounts, and generate actionable alerts with real-time dashboards.

---

## 🚀 Features

- 📁 **Mock Dataset Generator**
  - Creates 250+ realistic client records using `Faker`
  - Includes names, emails, contract dates, retainer amounts, payment history

- 🧹 **Data Cleaning Pipeline**
  - Removes duplicates, fixes date formats, handles missing values
  - Stores cleaned data for downstream processes

- 🔔 **Automated Alerts**
  - Flags overdue or partial payments
  - Simulates email reminders for unpaid clients
  - Saves alert summaries for reference

- 🔄 **Status Updater**
  - Auto-updates `Payment Status` & `Contract Status` based on due dates and amounts

- 📊 **Interactive Dashboard**
  - Streamlit-powered visual dashboard
  - KPIs, Pie & Bar Charts, and full client table
  - Easy to deploy and use as a client or agency reporting tool

- 💻 **Command Line Interface (CLI)**
  - Easily trigger any part of the pipeline:
    ```bash
    python cli.py clean
    python cli.py reminder
    python cli.py update
    ```

---

## 🧱 Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| Python          | Core logic and automation        |
| Pandas          | Data processing and manipulation |
| Faker           | Generating realistic sample data |
| Streamlit       | Interactive dashboard            |
| Matplotlib      | Visual charts (Pie, Bar)         |
| argparse + os   | CLI commands                     |
| Excel & CSV     | Data storage and reporting       |

---
🌍 Future Improvements
Real email & Twilio SMS alert integration

Add filters (month/year/client)

Upload actual Excel files (not just mock)

Multi-user authentication in dashboard

PDF export for monthly summaries

📌 Author
Aman Ali
Freelancer in Automation • Python Developer
💼 Portfolio: Doc-27 Portfolio Site
📧 Contact: amanalimar1993@gmail.com



