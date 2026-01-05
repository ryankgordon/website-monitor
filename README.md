Created by Ryan Gordon
📘 What This Application Does
This application is a website monitoring tool built with Python and FastAPI.

✅ What it does:
  ● Monitors one or more websites (like Google, GitHub, or AWS status pages)
  ● Checks each site every 60 seconds
  ● Detects whether a site is UP or DOWN
  ● Logs results to files for later review
  ● Sends a Discord alert when a website’s status changes (optional)
  
This is useful for:
  ● Learning backend APIs
  ● Monitoring important services
  ● Practicing real-world Python projects
  ● Understanding uptime monitoring systems
  
🛠 Requirements
Before starting, make sure you have:
  ● Python 3 installed
  ● A terminal (Mac/Linux/WSL recommended)
  ● Internet connection
✅ STEP 1: Check Python Installation

Run:
python3 --version
You should see something like:
Python 3.x.x

📁 STEP 2: Create the Project Folder
Run:
mkdir website-monitor
cd website-monitor
This creates and enters the project directory.

🧪 STEP 3: Create a Virtual Environment (Recommended)
Run:
python3 -m venv venv
source venv/bin/activate

✅ If successful, your terminal will show:
(venv)

📦 STEP 4: Install Required Python Packages

Run exactly this command:
pip install fastapi uvicorn httpx python-dotenv
These packages handle:
  ● API creation
  ● Web server
  ● Website requests
  ● Environment variables
  
🧠STEP 5: Create the Application File
Create and open the file:
nano app.py
➡ Paste the Python code
In the code file on GitHub
➡ Save: CTRL + O, then press Enter
➡ Exit: CTRL + X

📂 STEP 6: Create a Logs Folder
Run:
mkdir logs
This folder stores monitoring history for each website.

🔔 STEP 7 (Optional): Create a .env File for Discord Alerts
Only needed if you want Discord notifications.

Run:
nano .env
Paste:
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK
Save and exit:
● CTRL + O → Enter
● CTRL + X

🚀STEP 8: Run the Website Monitor
Start the FastAPI server:
uvicorn app:app --reload
If successful, you’ll see:
Uvicorn running on http://127.0.0.1:8000/
✅ Leave this terminal running.

🌍 STEP 9: Open the API in Your Browser
Go to:
http://127.0.0.1:8000/docs on your browser
This opens the interactive FastAPI dashboard.

➕ STEP 10: Add a Website to Monitor
1. Find POST /monitor
2. Click Try it out
3. Paste:
{
"url": "https://status.aws.amazon.com/"
}
4. Click Execute
You can replace the URL with:
  ● https://google.com
  ● https://github.com
  ● https://discord.com How to Know It’s Working

Terminal shows UP/DOWN messages
✅ Log files appear inside the logs/ folder
✅ Discord alerts trigger when a site changes status
🎉 Done!
