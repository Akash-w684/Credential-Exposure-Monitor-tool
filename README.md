
# Credential Exposure Monitor Tool

Overview

Credential Exposure Monitor Tool is a cybersecurity project designed to detect and monitor exposed credentials from leaked datasets. The system helps users identify whether an email or credential has appeared in known breach records.

Features
- Search for exposed credentials
- Breach history tracking
- Simple web interface using Flask
- Stores breach records in SQLite database
- Displays breach results dynamically
- History page for previous searches

Technologies Used
- Python
- Flask
- SQLite
- HTML/CSS
- CSV Data Handling

Project Structure
Credential_Exposure_Monitor_tool/

├── app.py

├── breaches.csv

├── database.db

├── templates/

│   ├── index.html

│   ├── result.html

│   └── history.html

└── README.md

Installation & Setup
1. Clone Repository
git clone https://github.com/Akash-w684/Credential_Exposure_Monitor_tool.git

2. Navigate to Project Folder
cd Credential_Exposure_Monitor_tool

3. Install Dependencies
pip install flask pandas

4. Run the Application
python app.py

Usage
1. Start the Flask server
2. Open browser: http://127.0.0.1:5001
3. Enter an email or credential
4. View breach exposure results
Security Note
This project is developed for educational and cybersecurity awareness purposes only. No real credentials should be exposed or misused.

Future Improvements
- Real-time breach API integration
- Dark web monitoring support
- Email alert notifications
- Improved dashboard visualization
- Authentication system

Author

Akash Wavhal

