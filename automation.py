from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options-  to prevent the browser from closing after the script finishes.
options = Options()
options.add_experimental_option("detach", True)

# Set up the Chrome service
service = Service(executable_path='./chromedriver.exe')

# Initialize the Chrome WebDriver with the options
chrome_browser = webdriver.Chrome(service=service, options=options)

# To maximize the window
chrome_browser.maximize_window()
# Open the URL
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


# assert 'Selenium Easy Demo' in chrome_browser.title   # True
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

# grabbing the input field using page source- 'id="user-message"
user_message = chrome_browser.find_element(By.ID, 'user-message')

# to clear the user input or text from the website input field
user_message.clear()

# using 'send_keys', sending the input message to the website
user_message.send_keys('I AM EXTRA COOL')

# Simulating a automated click to 'Show Message' field in website
show_message_button.click()

# Show the output
output_message = chrome_browser.find_element(By.ID, 'display')

assert "I AM EXTRA COOL" in output_message.text()


chrome_browser.close()   # to close the current Chrome Browser
chrome_browser.quit()    # to quit the entire Chrome Browser sessions








