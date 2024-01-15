Install Python 3.9.13:

Download and install Python 3.9.13 from 
https://www.python.org/downloads/release/python-3913/  (windows 64 bit installer)

Install Chrome Driver that matches the version of Chrome you are using (tested on 120.0.6099.109)
https://googlechromelabs.github.io/chrome-for-testing/

Check crhome version by goign to this address  
      chrome://settings/help

copy chromedriver.exe into the same directory as the script 
      dial_script.py, numbers.txt, and requirements.txt

Open a Terminal/Command Prompt:
On Windows: Press Win + R, type cmd, and press Enter.
On macOS/Linux: Press Ctrl + Alt + T or use your preferred terminal.

Navigate to Your Project Directory:

      cd path/to/your/project
Create a Virtual Environment:

      python3.9 -m venv venv

On Windows:

      venv\Scripts\activate
On macOS/Linux:

      source venv/bin/activate
Install Requirements:

      pip install -r requirements.txt
Verify Installation:

      pip list


Make changes to the script as needed
Change the default user directory (username Admin to whatever is your windows profile and chrome profile name on the line below)
      C:\Users\Admin\AppData\Local\Google\Chrome\User Data

Change voice_message.mp3 to your recorded voice file and place it in the same directory as the script

Execute your Python script, assuming it's named dial_script.py:

      python dial_script.py

Now you have a virtual environment using Python 3.9.13, the project requirements are installed, and you've run the code using the dial_script.py file.
