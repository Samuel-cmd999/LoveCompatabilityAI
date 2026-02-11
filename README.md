💘 Love Compatibility AI (Tkinter Edition)
A romantic desktop application built with Python & Tkinter that calculates love compatibility between two people based on their names and birthdays — complete with floating heart animations, background music, and screenshot saving functionality.
Made with ❤️ for fun, love, and creativity.

✨ Features
💌 Love compatibility percentage calculation
📅 Birthday-based scoring logic
💬 Dynamic romantic result messages
❤️ Floating heart animation
🎵 Background music support (optional)
📸 Save result as PNG screenshot
🌸 Smooth fade-in start screen
🎨 Cute pink romantic UI theme

How It Works
The compatibility score is calculated using:
Unicode value sum of both names
Birthday difference factor
A randomized “magic” compatibility factor
The final score is averaged and displayed as a percentage with a matching love message.
⚠️ Note: This app is for fun and entertainment purposes only.

🛠️ Built With
Python 3.x
Tkinter (GUI)
Pillow (ImageGrab for screenshots)
Pygame (background music)
Threading
Datetime

git clone https://github.com/yourusername/love-compatibility-ai.git
cd love-compatibility-ai
pip install pillow pygame

Make sure you have:
Python 3 installed
(Optional) A file named love_song.mp3 in the project folder for background music

🎵 Adding Music
Place a file named:
love_song.mp3
In the same directory as the script.
If no file is found, the app will still run without music.

🎨 Customization Ideas
Add zodiac compatibility logic
Improve heart animations using after() instead of threads
Convert to a web app (Flask / Django)
Package as a Windows .exe using PyInstaller
Add database saving for past results
Add dark mode

Build as Executable (.exe)
Install PyInstaller:
pip install pyinstaller

Then run:
pyinstaller --onefile --windowed main.py
Your executable will be inside the /dist folder.

Future Improvements
Thread-safe animation handling
More advanced AI compatibility logic
Mobile-friendly version
Online shareable version

👨‍💻 Author
Created with ❤️ by Motsamai Mashaba

📜 License
This project is licensed under the MIT License.

You are free to:
Use
Modify
Distribute
Sublicense
Sell
As long as you include the original copyright and license notice.
