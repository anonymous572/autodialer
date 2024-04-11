import os
import time
import subprocess
import re
import undetected_chromedriver as webdriver
import random
import re
import pygame

    
def open_chrome():
    global driver
    #try:
    #    subprocess.run("taskkill /f /im chrome.exe", check=True, stdin=subprocess.DEVNULL)
    #except:
    #    print('no chrome processes open')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.use_chromium = True  
    #chrome_options.add_argument('--disable-popup-blocking')  

    chrome_options.add_argument(r'--user-data-dir=' + os.getenv('LOCALAPPDATA') + r'\Google\Chrome\User Data')
    chrome_options.add_argument(r'--profile-directory=Default')
    
    driver = webdriver.Chrome(driver_executable_path="chromedriver.exe", use_subprocess=True, options=chrome_options)

def play_audio(filename):
    pygame.init()
    pygame.mixer.init()
    #pygame.mixer.init(90000, size=-16, channels=2)    
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def google_voice_call(number):
    driver.get("https://voice.google.com")

    #This first section of the script clsoes the popup
    try:
        stop_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/section/div/div/div/gv-call-response/div/button'
        stop_element = driver.find_element("xpath", stop_xpath)
        driver.execute_script("arguments[0].click();", stop_element)
        time.sleep(5)
    except:
        print('call not stopped')

    #this stops the call
    try:
        stop_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/section/div/div/div/gv-call-response/div/button'
        stop_element = driver.find_element("xpath", stop_xpath)
        driver.execute_script("arguments[0].click();", stop_element)
        time.sleep(5)
    except:
        print('call not stopped')

    #makes the call
    try:
        element_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/gv-make-call-panel/div/gv-call-as-banner/div/div/gv-call-as-select/div/div[1]/div/div[2]/span[2]'
        mynumber_element = driver.find_element("xpath", element_xpath)

        # Perform actions on the element (e.g., get text)
        element_text = mynumber_element.text
        input_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/gv-make-call-panel/div/div[1]/div/input'

        mynumber_element = driver.find_element("xpath", input_xpath)
        time.sleep(2)
        mynumber_element.send_keys(number)

        time.sleep(2)
        call_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/gv-make-call-panel/div/div[1]/button'
        callbtn_element = driver.find_element("xpath", call_xpath)
        driver.execute_script("arguments[0].click();", callbtn_element)
    except:
        print('could not make call')
            
    time.sleep(2)

def random_call():
    open_chrome()

    matches = []

    # Open the text file for reading
    with open("numbers-zip.txt", 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Find all matches of the number pattern in the line
            match = re.sub(r'\D', '', line)
            print(f"Number: {match}")
            if match: 
                match = match[:10] + " " + match[10:]
                match = ''.join(match)
                if len(match) > 9:
                    matches.append(match)

    # Randomize the order of matches
    random.shuffle(matches)

    # Loop through the randomized matches
    for match in matches:
        print(f"Number found: {match}")
        try:
            if match is not None:
                # Play the audio
                google_voice_call(match[:10])
                time.sleep(30)  # Change This Value as needed for your speaking message length
        except Exception as e:
            print(f"Failed with error: {e}")

def main():
    random_call()

if __name__ == "__main__":
    main()