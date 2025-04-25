# TCP-socket-Project
04/10/25 my first Networking Project

🖥️ TCP Image Transfer over Sockets





A lightweight TCP Client/Server application for transferring image files over a secure socket connection with:

Progress tracking 📈

Auto-preview after reception 🖼️

Optional text chatting 💬

✨ Features

📤 Send image files (JPEG, PNG, etc.)

📈 Real-time transfer progress via tqdm

🖼️ Auto-preview received images using Pillow

🔄 Simple two-way messaging after file transfer

🎯 Single socket connection — no need to reconnect

⚡ Fast, lightweight, and easy to extend

🛠️ Requirements

Python 3.8+

Install dependencies:

pip install tqdm pillow

(Optional) For AVIF format support:

pip install pillow-avif-plugin

🚀 Getting Started

1⃣ Run the Server

python server.py

The server waits for a client connection and auto-previews incoming images.

2⃣ Run the Client

python client.py

The client sends the selected image file to the server and enters text chat mode.

📂 Project Structure

TCP-socket-Project/
├── server.py     # Server script (receiver)
├── client.py     # Client script (sender)
└── images/       # Folder containing your images (client side)
    └── your_image.jpg

🔥 Preview

Client Uploading

Server Receiving





Real-time upload progress and image preview after transfer!

🎯 Usage Example

✅ Send images✅ Preview on server✅ Switch to chat mode easily

# client.py
filepath = r"C:\path\to\your\image.jpg"

📜 License

This project is licensed under the MIT License.

❤️ Acknowledgments

Python Socket Library

TQDM Progress Bar

Pillow Imaging Library

✨ Star this repo if you like it!

