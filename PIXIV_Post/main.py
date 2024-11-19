from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os  # For loading environment variables

# User agent for browser
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
chrome_options = webdriver.ChromeOptions()

# Define proxy server
PROXY = "20.213.247.195"
# chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

driver = webdriver.Chrome(options=chrome_options)

# Clear window.navigator for detection bypass
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get("https://www.pixiv.net/")
sleep(2.1)

driver.get('https://accounts.pixiv.net/login')
sleep(2.1)

# Get the email input field and enter email
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys(os.getenv('PIXIV_EMAIL'))    # Enter email
print('Email input complete')
sleep(1)

# Get the password input field and enter password
password = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
password.send_keys(os.getenv('PIXIV_PASSWORD'))    # Enter password
print('Password input complete')

sleep(2)

# Find all buttons on screen and click the 'Log In' button
buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"]')
for i in buttons:
    if i.text == '登入' or i.text == 'Log In':
        i.click()
        print('Click Log In')
        break

sleep(5)

# Check for "Remind me later" link
try:
    check = driver.find_element(By.LINK_TEXT, "稍後再說")
    print(check.text)
    if check.text == '稍後再說' or check.text == 'Remind me later':
        check.click()
        print(f'Clicked {check.text}')
    sleep(2)
except:
    print('ok')
    sleep(2)

is_not_ok = True
sleep(3)

# Navigate to illustration creation page
driver.get("https://www.pixiv.net/illustration/create")
sleep(2.2)

# Upload image
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
imgInput.send_keys(os.getenv('IMAGE_PATH'))   # Enter the absolute path of the image to upload
print('Image uploaded')
sleep(2.2)

# Enter title
titleInput = driver.find_element(By.CSS_SELECTOR, 'input[name="title"]')
titleInput.send_keys('testing_title')
print('Title entered')
sleep(2.2)

# Enter comment
textInput = driver.find_element(By.CSS_SELECTOR, 'textarea[name="comment"]')
textInput.send_keys('testing_comment')
print('Comment entered')
sleep(2.2)

# Enter tag
tagInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="標籤"]')
tagInput.send_keys('#女の子')
print('Tag entered')
sleep(2.2)

# Select restriction level
restrictInput = driver.find_element(By.CSS_SELECTOR, 'input[name="x_restrict"][value="general"]')
restrictInput.click()
print('Selected x_restrict = general')
sleep(2.2)

# Set sexual content to false
sexualInput = driver.find_element(By.CSS_SELECTOR, 'input[name="sexual"][value="false"]')
sexualInput.click()
print('Selected sexual = false')
sleep(2.2)

# Set AI generation status to not AI generated
aiInput = driver.find_element(By.CSS_SELECTOR, 'input[name="ai_type"][value="notAiGenerated"]')
aiInput.click()
print('Selected ai_type = notAiGenerated')
sleep(2.2)

# Click "Post" button to publish
sleep(5)
buttons = driver.find_elements(By.LINK_TEXT, "發佈")
# Uncomment the next line to enable clicking the publish button
# buttons.click()

