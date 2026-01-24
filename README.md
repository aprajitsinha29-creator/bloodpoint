# 🩸 BloodPoint

A Python and SQL-based application that streamlines the blood donation process while encouraging people to donate blood through an innovative reward system.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Database Configuration](#database-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)

---

## 🎯 Overview

BloodPoint bridges the gap between blood donors and those in need by enabling efficient communication and coordination. The system streamlines the process of finding suitable donors based on blood type, location, and availability, ensuring that blood reaches recipients in a timely manner.

### Objective

The program's primary goal is to facilitate seamless blood donation by:
- Connecting donors with recipients efficiently
- Providing real-time matching based on compatibility
- Encouraging regular donations through gamification
- Maintaining a reliable database of available donors

---

## ✨ Features

### 🩸 For Donors
- **Easy Registration**: Sign up as a donor with essential details (blood type, contact info, availability)
- **Reward System**: Earn credit points and titles for each donation made
- **Profile Management**: Update availability and contact information

### 🏥 For Recipients/Hospitals
- **Urgent Requests**: Create blood requests specifying requirements
- **Real-Time Matching**: Intelligent system connects requests with compatible donors
- **Location-Based Search**: Find nearby donors for faster response

### 🎮 Gamification
- **Title Awards**: Earn prestigious titles based on donation frequency
- **Credit Points**: Accumulate points for each successful donation
- **Leaderboard**: Track your contribution impact

---

## 📁 Project Structure

```
bloodpoint/
│
├── main.py                 # Main application entry point
├── donor.py                # Donor management module
├── request.py              # Blood request handling module
├── misc.py                 # Utility functions and database connection
├── database_schema.sql     # MySQL database schema and default data
└── README.md               # Project documentation
```

### File Descriptions

- **main.py**: Contains the primary application logic and user interface
- **donor.py**: Handles donor registration, updates, and profile management
- **request.py**: Manages blood request creation and donor-recipient matching
- **misc.py**: Utility functions, database connection setup, and helper methods
- **database_schema.sql**: Complete database structure with tables for donors, requests, and awards

---

## 🔧 Prerequisites

Before setting up BloodPoint, ensure you have the following installed:

- **Python 3.x** ([Download](https://www.python.org/downloads/))
- **MySQL Server 8.0+** ([Download](https://dev.mysql.com/downloads/mysql/))
- **MySQL Connector for Python**

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/aprajitsinha29-creator/bloodpoint.git
cd bloodpoint
```

### Step 2: Install Python Dependencies

```bash
pip install mysql-connector-python
```

### Step 3: Set Up MySQL Database

#### Option A: Using MySQL Command Line

1. Open MySQL command line client:
```bash
mysql -u root -p
```

2. Execute the schema file:
```sql
SOURCE /path/to/bloodpoint/database_schema.sql;
```

3. Verify the setup:
```sql
USE bloodpoint;
SHOW TABLES;
SELECT * FROM Award;
```

#### Option B: Using MySQL Workbench

1. Open MySQL Workbench and connect to your server
2. Go to **File → Open SQL Script**
3. Select `database_schema.sql` from the project folder
4. Click **Execute** (lightning bolt icon)
5. Verify tables were created in the left sidebar

### Step 4: Configure Database Credentials

Open `misc.py` and update the database connection details:

```python
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",              # Your MySQL username
    password="YOUR_PASSWORD",  # Your MySQL password
    database="bloodpoint"
)
```

**⚠️ Important**: Never commit your actual password to version control. Consider using environment variables for sensitive data.

---

## 🗄️ Database Configuration

### Database Structure

The BloodPoint database includes the following main tables:

- **Donor**: Stores donor information (name, blood type, contact details, donation count)
- **Request**: Manages blood requests from recipients/hospitals
- **Award**: Contains title awards and prize values for donors

### Default Data

The schema file includes default award tiers to encourage donations. No real user data or credentials are included in the repository for security reasons.

---

## 💻 Usage

### Running the Application

```bash
python main.py
```

### Main Menu Options

1. **Register as Donor**: Create a new donor profile
2. **View Donors**: Browse all registered donors
3. **Create Blood Request**: Submit an urgent blood requirement
4. **Match Request with Donor**: Find compatible donors for requests
5. **View Awards/Leaderboard**: Check donation statistics and rankings
6. **Update Donor Information**: Modify donor details
7. **Exit**: Close the application

### Example Workflow

1. Register as a donor with your blood type and contact information
2. Recipients/hospitals create blood requests specifying needs
3. System matches requests with compatible donors automatically
4. Donors receive notifications and confirm availability
5. Upon successful donation, donors earn points and titles

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Improvement

- Add email/SMS notification system
- Implement web-based interface
- Add donor appointment scheduling
- Create mobile app version
- Enhance security with password encryption
- Add data analytics and reporting

---

## 👨‍💻 Author

**Aprajit Sinha**

- GitHub: [@aprajitsinha29-creator](https://github.com/aprajitsinha29-creator)

---

## 🙏 Acknowledgments

- Thanks to all blood donors who save lives daily
- Inspired by the need for efficient blood donation systems
- Built to make a positive impact on healthcare accessibility

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/aprajitsinha29-creator/bloodpoint/issues) page
2. Create a new issue with detailed description
3. Contact the author through GitHub

---

## 🔮 Future Enhancements

- [ ] Web-based dashboard
- [ ] Mobile application
- [ ] SMS/Email notifications
- [ ] Integration with hospital systems
- [ ] Blood bank inventory management
- [ ] Donation history tracking
- [ ] Emergency alert system
- [ ] Multi-language support

---

**⭐ If you find this project useful, please consider giving it a star!**

*Together, we can save lives through efficient blood donation management.*

