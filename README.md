Install Python 3.9.13:

Download and install Python 3.9.13 from 
https://www.python.org/downloads/release/python-3913/  (windows 64 bit installer)

Install Chrome Driver that matches the version of Chrome you are using (tested on 122.0.6261.69)
https://googlechromelabs.github.io/chrome-for-testing/
For Windows use ChromeDriver Win64 version (example download link: https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/win64/chromedriver-win64.zip)

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

      python -m venv venv

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

To Execute script

Open command line prompt or Bash on Linux by typing Command Prompt or CMD in start menu
Browse to the script location using `cd C:\locationofdirectory` command

1. 
For automatically calling and speaking to the staff yourself (during in office hours)

Execute Python script:

      python auto_call.py
      
Note: This will leave 35 seconds for you to speak and leave your message after it automatically hangs up and calls next number: to change this edit the code:

      time.sleep(35) #Change This Value as needed for your speaking message length

2. 
For leaving a voicemail (during out of office hours)
      Create a voice_message.mp3 of your recorded voice file and place it in the same directory as the script
Execute Python script:

      python leave_voicemail.py
   
Note: This will leave 25 seconds as measured for the typical voice answering machine to finish,  to change this edit the code:

      time.sleep(25) #Change This Value to greater than average length of answering machine messages


Now you have a virtual environment using Python 3.9.13, the project requirements are installed, and you've run the code using the dial_script.py file.
