from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Customizable Variables
MoreInfo = False # Displays more information about every bus at your stop. This is only in console for debugging purposes.
BUS = ""  # Specify the bus number you want to search for (e.g., "305")
STOP = ""  # Specify the stop number you want to search for (e.g., "1278")
NICK = ""  # Specify the stop name you want to search for (e.g., "ЛЪВОВ")
TIME = ""  # This will hold the time extracted for the bus !!! It is not requerd for you to type anything

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,2000") 

# Path to the Chromium WebDriver
service = Service("/usr/bin/chromedriver")      # !!!Please Change this unless you are in linux
driver = webdriver.Chrome(service=service, options=chrome_options)

def extract_bus_times(section_text, bus_number):
    """
    Function to search for the bus number and return the time details.
    Assumes section_text is a long string containing all bus data in 4-line blocks.
    """
    # Split the section text into lines
    lines = section_text.splitlines()

    # Loop through every 4 lines (bus data block)
    for i in range(0, len(lines), 4):
        bus_line = lines[i].strip()  # Bus number line
        if bus_number in bus_line:
            # If we find the bus number, grab the minutes (4th line)
            minutes_line = lines[i+3].strip()  # The 4th line contains the minutes
            return minutes_line
    
    # If bus is not found in the section
    return f"Bus {bus_number} is not online."

try:
    # Open the website
    print("Loading website...")
    driver.get("https://www.sofiatraffic.bg/bg/public-transport")
    print("Website loaded.")
    time.sleep(10)  # Wait for the page to load

    # Step 1: Locate the search bar directly by its XPath
    try:
        print(f"Searching your Stop:'{STOP}'...")
        search_bar = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/main/div[1]/section/div/div[1]/div/div/div/div[3]/div/div[2]/label/input"))
        )
        search_bar.click()
        time.sleep(1)
        search_bar.clear()
        search_bar.send_keys(STOP)  # Use the customizable STOP variable
        time.sleep(3)

    except Exception:
        print("Error: Search bar not found or not interactable.")
        driver.quit()
        exit()

    # Step 2: Search for "NICK" and click the first tag
    try:
        print(f"Searching for '{NICK}'...")
        nick_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{NICK}')]"))
        )
        print(f"'{NICK}' found. Clicking it...")
        driver.execute_script("arguments[0].scrollIntoView(true);", nick_element)
        time.sleep(1)
        nick_element.click()
        time.sleep(3)
    except Exception:
        print(f"Error: '{NICK}' not found.")
        driver.quit()
        exit()

    # Step 3: Search for the bus section
    try:
        print("Searching for bus times section...")
        section_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/section/div/div[1]/div/div/div[2]")

        # Extract the text from the section
        section_text = section_element.text
        if MoreInfo == True:
            print(f"Section text: {section_text}")
        else:
            print("Section text: Not displayed due to 'MoreInfo' variable set to False.")

        # Extract time for the specified bus (BUS variable)
        bus_time = extract_bus_times(section_text, BUS)
        TIME = bus_time  # Assign the result to the TIME variable
        if "is not online" not in bus_time:
            print(f"Bus {BUS} status: {TIME}")
        else:
            print(TIME)

    except Exception as e:
        print(f"Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")

