# Internship Management System

## Overview
This project is an **Internship Management System** designed to streamline the internship process for universities. The system addresses challenges such as complex tracking, communication gaps, administrative burdens, and compliance record-keeping. It features four dashboards tailored for different user roles: **Student (Intern)**, **Admin**, **Mentor**, and **Instructor**. The system incorporates **Streamlit** for the UI, **Airtable API** for database management, and integrates **Discord API** for notifications and **Mapbox API** for real-time location tracking of interns. Additionally, **Ollama LLaMA3.2** powers AI-based assistance.

---

## Features
### Student Dashboard
- Submit internship details:
  - Start Date
  - Company Name, Address, and Registration Number
  - External Mentor Name, Contact Details, and Email Address
  - City, Stipend Amount, and Offer Letter Upload
- Submit reports:
  - Fortnightly Reports (Every 15 days)
  - Mentor Assignments (Every 30 days)
  - Industry Mentor Evaluation Report (Final Submission)
- View internship progress and updates.

### Admin Dashboard
- Assign internal mentors to students.
- Track progress and generate comprehensive reports.
- Verify internship company details with the **Ministry of Corporate Affairs**.
- Manage compliance and record-keeping.

### Mentor Dashboard
- Assign tasks to students.
- Evaluate and submit marks for submitted reports.
- Review fortnightly progress.

### Instructor Dashboard
- Oversee and verify the progress of all assigned interns.
- Manage CRUD operations related to intern details.

### Mobile App
- Track current locations of interns in real-time using **Mapbox API**.
- Notifications for pending tasks and updates via **Discord API**.

---

## Functional Requirements
1. **Real-Time Tracking**: Use Mapbox for location tracking of interns.
2. **Centralized Communication**: Integrate Discord for real-time notifications.
3. **Airtable Integration**: Manage internship data (CRUD operations) using Airtable API.
4. **AI Assistance**: Utilize Ollama LLaMA3.2 for intelligent task recommendations.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: Airtable API
- **APIs**:
  - **Mapbox API**: Location tracking
  - **Discord API**: Notifications
- **AI Integration**: Ollama LLaMA3.2

---

## Screenshots
### Airtable API Integration Example
Below is a sample snippet showcasing how data was managed using the Airtable API:

```python
import requests

# Airtable API Configuration
API_URL = "https://api.airtable.com/v0/appXXXXXXXX/internship_records"
HEADERS = {
    "Authorization": "Bearer YOUR_AIRTABLE_API_KEY",
    "Content-Type": "application/json"
}

# Fetch Internship Records
def fetch_internship_records():
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Example Usage
data = fetch_internship_records()
print(data)
```

![Airtable API Screenshot](https://via.placeholder.com/800x400?text=Airtable+API+Integration+Example)

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/internship-management-system.git
   cd internship-management-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys in the `.env` file:
   ```plaintext
   AIRTABLE_API_KEY=your_api_key
   DISCORD_API_KEY=your_api_key
   MAPBOX_API_KEY=your_api_key
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
