# IT Support Toolkit

A Python-based command-line toolkit designed to assist with common IT support, troubleshooting, and system diagnostics tasks.

## Features

### System Information
Displays:
- Operating system
- OS version
- Machine architecture
- Processor information

### Network Diagnostics
Checks:
- Computer hostname
- Local IP address
- Internet connectivity
- DNS resolution

### Storage Information
Displays:
- Total storage
- Used storage
- Free storage
- Storage usage percentage

### Memory Information
Displays:
- Total memory
- Used memory
- Available memory
- Memory usage percentage

### Diagnostic Report Generator
Generates a complete diagnostic report and saves it as:

```text
diagnostic_report.txt
The report includes:

System information
Network status
Storage usage
Memory usage
How to Run

Make sure Python 3 is installed.

Clone the repository:

git clone https://github.com/WEZx7/it-support-toolkit.git

Navigate to the project directory:

cd it-support-toolkit

Run the toolkit:

python main.py
Example Menu
================================
       IT SUPPORT TOOLKIT
================================
1. System Information
2. Network Diagnostics
3. Storage Information
4. Memory Information
5. Generate Diagnostic Report
6. Exit
Example Diagnostic Output
--- Network Diagnostics ---
Computer Name: example-device
Local IP Address: 10.0.0.5

Testing internet connection...
Internet Connection: Connected
DNS Resolution: Working
Technologies Used
Python 3
platform
socket
shutil
datetime
Project Purpose

This project was created to practice Python development while building practical tools commonly used in IT support and technical troubleshooting environments.

It demonstrates:

System diagnostics
Network troubleshooting
File generation
Command-line application development
Basic error handling
Future Improvements

Planned features include:

CPU usage monitoring
Windows support improvements
Additional troubleshooting checks
Exporting reports in different formats
Improved cross-platform compatibility

Author

Feras M. Jubran
