from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
chrome_options = webdriver.ChromeOptions()
# PROXY = "202.20.16.82:10152"
# chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

driver = webdriver.Chrome(options=chrome_options)
# Clear window.navigator
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get('https://twitter.com/i/flow/login')
sleep(2)

sleep(1.5)     # Wait for 1.5 seconds to allow the page to load completely
# Locate the email input field
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys('your email address')    # Enter email address
print('Email entered')

sleep(2)     # Wait for 2 seconds to allow the page to load completely

# Retrieve all buttons on the page (using elements)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == 'Next' or i.text == 'Next':
        i.click()   # If the button is "Next" or "Next," click it
        print('Clicked Next')
        break

sleep(2)     # Wait 2 seconds for the page to load before proceeding
# the try will cuz by too many time fall login
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys('your account')    # Enter account, format will be @xxxxx, under your display name and your website’s address
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == 'Next' or i.text == 'Next':
            i.click()  # If the button is "Next" or "Next," click it
            print('User account verified, clicked Next')
            break
    sleep(2)       # Wait 2 seconds for the page to load before proceeding
except:
    print('ok')
    sleep(2)       # If the security screen does not appear, wait 2 seconds before continuing

username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
username.send_keys('your password')    # Enter password
print('Password entered')

sleep(1.6)

buttons = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')
for i in buttons:
    i.click()   # If the button is "Next," click it
    print('Clicked LoginForm_Login_Button')
    break

sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys('input tweet text')      # Enter text in the input field
print('Text entered')
sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys('image path')   # Provide absolute path to the image, upload image
print('Image uploaded')
sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == 'Post' or i.text == 'Post':
        i.click()    # Click the Post button
        print('Tweet posted')
        break
sleep(100)
driver.close()  # Close the browser window

# Suspicious login prevented

