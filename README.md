🖥️ TCP Image Transfer over Sockets

A lightweight TCP Client-Server application for transferring image files over a TCP connection.
It includes file transfer with progress bar, image preview after transfer, and simple text chat.

📜 Project Description
This project implements a Python-based TCP socket application that:

Connects a client to a server

Sends an image file (e.g., JPG, PNG)

Displays a real-time progress bar while transferring

Auto-previews the received image on the server

Enables basic text chat after the file transfer

🛠️ Tools & Libraries Used

Tool / Library	Purpose
Python 3.8+	Programming Language
socket	TCP connection
struct	Data packing (filename, filesize)
tqdm	Progress bar during file transfer
Pillow (PIL)	Image previewing after receiving
📂 Project Structure
kotlin
Copy
Edit
TCP-Image-Transfer/
├── README.md
├── requirements.txt
├── server.py       # Start this first
├── client.py       # Start this second
├── images/
│   ├── 2.jpg
│   └── 3.jpg
🚀 How to Run
Setup
Install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
1️⃣ Start the Server
bash
Copy
Edit
python server.py
The server will wait for a client connection and preview received images automatically.

2️⃣ Start the Client
bash
Copy
Edit
python client.py
The client will:

Send an image file

Show a progress bar

Enable text chat after the transfer

🖼 Screenshots

Client Progress	Server Preview
🐞 Known Bugs / Limitations
Only one client can connect at a time

No file type validation

No resume if transfer is interrupted

Limited error handling during chat

🎯 Possible Enhancements
Support for multiple simultaneous clients (threading or asyncio)

File type verification before accepting

Encrypt connection using SSL/TLS

Support for folders/multiple files

GUI Application (using Tkinter or PyQT)

📜 License
This project is open-source and distributed under the MIT License.

🌟 Star this project if you like it!
📋 requirements.txt file content (simple)
text
Copy
Edit
tqdm
pillow
✅ Recap

File	Purpose
server.py	Start first — receive image and preview
client.py	Start second — send image and chat
requirements.txt	Install needed Python libraries
images/	Folder for testing images
