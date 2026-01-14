# bloodpoint
An application that helps streamline the process of blood donation while also encouraging people to donate blood through a reward system. It works on python-sql connectivity. 
<br>
Author - Aprajit Sinha
<br>
•	Objective:
<br>
The program's primary goal is to bridge the gap between blood donors and those in need by enabling efficient communication and coordination. It is designed to streamline the process of finding suitable donors based on blood type, location, and availability, ensuring that blood reaches recipients in a timely manner.
<br>
•	Features:
<br>
	Donor Registration: Allows individuals to sign up as donors, providing essential details such as blood type, contact information, and availability.
<br>
	Recipient Requests: Enables recipients or hospitals to create urgent blood requests specifying their requirements.
<br>
	Real-Time Matching: Uses an intelligent matching system to connect donors with recipients based on compatibility and proximity.
<br>

	Encouraging involvement: Encourages users to donate blood frequently by rewarding them for each donation they make in form of titles and credit points.

The repository includes the MySQL database schema (`bloodpoint_schema.sql`).
Only table structures and default award data are provided.
No real user data or credentials are included.

## 🗄️ Database Setup & Local Execution Guide

This project uses a MySQL relational database named **`bloodpoint`** to store donor details, blood requests, and award information.

For security reasons, only the **database schema and default award data** are included in this repository.  
No real user data or database credentials are uploaded.

---

### 📁 Files Included
- `bloodpoint_schema.sql` (or `database.sql`)
  - Creates the database and required tables
  - Inserts default award titles and prize values

---

## ✅ Prerequisites

Ensure the following are installed on your system:

- Python 3.x  
- MySQL Server  
- MySQL Connector for Python  

Install MySQL connector (if not already installed):
```bash
pip install mysql-connector-python

Step 1: Open MySQL
Open terminal or MySQL Workbench and log in:

mysql -u root -p

Step 2: Execute the SQL Schema File
Navigate to the folder containing the SQL file and run:

SOURCE path/to/bloodpoint_schema.sql;

Step 3: Verify Database Setup (Optional):

USE bloodpoint;
SHOW TABLES;
SELECT * FROM Award;

Step 4: Update Database Credentials in Python
Locate the MySQL connection block in the misc.py file (near the top):

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="bloodpoint"
)
