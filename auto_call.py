
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
    subprocess.run("taskkill /f /im chrome.exe")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.use_chromium = True  
    #chrome_options.add_argument('--disable-popup-blocking')  

    chrome_options.add_argument(r'--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data')
    chrome_options.add_argument(r'--profile-directory=Default')
    
    driver = webdriver.Chrome(driver_executable_path="chromedriver.exe", use_subprocess=True, options=chrome_options)

def extract_number_from_filename(filename):
    # Extract numbers from the filename using regular expression
    numbers = re.findall(r'\d+', filename)
    if numbers:
        return int(numbers[0])
    else:
        return None

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
        #stop_element = driver.find_elements_by_css_selector("[aria-label=XXXX]")
        driver.execute_script("arguments[0].click();", stop_element)
        time.sleep(5)
    except:
        print('call not stopped')

    #this stops the call
    try:
        stop_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/section/div/div/div/gv-call-response/div/button'
        stop_element = driver.find_element("xpath", stop_xpath)
        #stop_element = driver.find_elements_by_css_selector("[aria-label=XXXX]")
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

        #print('Element Text:', element_text)

        time.sleep(2)
        call_xpath = '/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-call-sidebar/div/gv-in-call-ng2/gv-make-call-panel/div/div[1]/button'
        callbtn_element = driver.find_element("xpath", call_xpath)
        driver.execute_script("arguments[0].click();", callbtn_element)
    except:
        print('could not make call')
            
    time.sleep(2)

def loop_call():
    open_chrome()

    number_pattern = re.compile(r'\b\d+\s+\d+\b')

    # Open the text file for reading
    with open("numbers.txt", 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Find all matches of the number pattern in the line
            match = number_pattern.findall(line)[0]

            print(f"Number found: {match}")
            try:
                if match is not None:
                    print(f"Extracted number from filename: {match}")
                    # Play the audio
                    google_voice_call(match)
                    time.sleep(35) #Change This Value as needed for your speaking message length
            except:
                print("failed")

def random_call():
    open_chrome()

    number_pattern = re.compile(r'\b\d+\s+\d+\b')
    matches = []

    # Open the text file for reading
    with open("numbers.txt", 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Find all matches of the number pattern in the line
            match = number_pattern.findall(line)
            if match:
                matches.append(match[0])

    # Randomize the order of matches
    random.shuffle(matches)

    # Loop through the randomized matches
    for match in matches:
        print(f"Number found: {match}")
        try:
            if match is not None:
                # Play the audio
                google_voice_call(match)
                time.sleep(30)  # Change This Value as needed for your speaking message length
        except Exception as e:
            print(f"Failed with error: {e}")

def main():
    random_call()

if __name__ == "__main__":
    main()