# 🔐 Educational Keylogger with C2


## ⚠️ Educational Purpose Only
This project is developed for educational and cybersecurity research purposes only.

✅ Security research and education
✅ Authorized penetration testing on own systems
✅ Learning cybersecurity concepts
❌ Unauthorized access or malicious activities

### 📋 Description
An educational keylogger implementation with encrypted Command & Control (C2) communication for cybersecurity learning purposes. This project demonstrates various security concepts including data exfiltration, persistence mechanisms, and client-server communication in a controlled educational environment.
🎯 Features

🎹 Educational Keylogger - Captures keyboard inputs for learning purposes
🌐 Encrypted C2 Communication - Secure client-server architecture
🔒 Data Encryption - Encrypted data transmission for security research
💾 Persistence Mechanism - Windows registry-based persistence (educational)
🔄 Auto-start Functionality - Session-based startup via registry modification
📁 APPDATA Integration - File management in user directory
💽 USB Autorun - Portable execution capabilities

### 🛠️ Installation
Prerequisites

Python 3.8
Windows OS


## Setup

Clone the repository:
```powershell
git clone https://github.com/NoxCaellum/encrypted_keylogger
cd educational_keylogger
```

Install dependencies:
```powershell
pip install -r requirements.txt
````

### 🚀 Usage
Basic Usage
Step 1: Start the C2 Server
```powershell
python c2_server.py
```

Step 2: Generate Executable
```powershell
python usbautorun.py
```
This generates the executable and the Autorun.inf files from educational_keylogger.py

Step 3: Run the Educational Client
```powershell
educational_keylogger.exe
```

### 📸 Screenshots
<img width="770" height="453" alt="keylogger" src="https://github.com/user-attachments/assets/3cc75928-296a-4844-9229-d67bdd4b1321" />

<img width="774" height="83" alt="register" src="https://github.com/user-attachments/assets/7ab8a48c-181d-4872-9836-72a4b3d91066" />




## 📁 Project Structure
educational_keylogger/

├── c2_client.py   
├── c2_server.py        
├── educational_keylogger.py 
├── persistence.py      
├── usbautorun.py        
├── key.ico             
├── requirements.txt    
├── LICENSE            
└── README.md          


### 🧪 Educational Testing
Important: Only test on systems you own or have explicit permission to test


### 📜 Legal Notice & Disclaimer
This tool is intended for educational and authorized security research only
Users are solely responsible for compliance with applicable laws and regulations
Unauthorized use on systems without explicit permission is strictly prohibited
The author assumes no liability for any misuse or damage caused by this software
This software is provided "as is" without any warranty
Violation of local, state, or federal laws through misuse is the user's responsibility

### 📚 Learning Objectives
This project helps understand:

Client-server communication patterns
Data encryption in network communication
Windows persistence mechanisms
Registry modification techniques
Security tool development concepts
Ethical considerations in cybersecurity

###📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

⚖️ Educational Disclaimer: This software is strictly for educational and authorized research purposes. Any misuse for malicious activities is strictly prohibited and may violate applicable laws.
