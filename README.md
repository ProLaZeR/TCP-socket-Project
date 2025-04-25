# TCP-socket-Project
04/10/25 my first Networking Project

 TCP Socket Project — Image File Transfer
A simple TCP client-server project built with Python, allowing the transfer of image files (JPEG, PNG) over a TCP connection with a progress bar and automatic preview after receiving.



Server listens for client connections

Client connects and sends:

Filename

File size

File data

Server:

Receives and saves the file

Previews the image

Then continues simple text chat if needed

✨ Features
📡 TCP communication between client and server

🖼️ Send any image file (JPG, PNG, etc.)

📈 Real-time progress bar using tqdm

📂 Save received files automatically

🖥️ Auto-preview the received image using Pillow

💬 Optional text messaging after file transfer

🔒 Single connection handling both file and messages


/TCP-socket-Project
    ├── server.py
    ├── client.py
    └── images/
         └── your_image.jpg

         
