# AutoTweet

This script opens the Twitter login page in a Chrome browser, enters the user's email, username, and password in sequence, and then publishes a tweet after logging in. It simulates user actions like filling in login details, uploading an image, and clicking buttons.

## Code Description

1. **Import Necessary Libraries**:
   - `webdriver` and `By`: Control the browser and interact with web elements, simulating user actions.
   - `sleep`: Adds pauses between steps to ensure full page loads.
   - `BeautifulSoup`: Imported but unused in this script; typically used for HTML parsing.

2. **Set Browser Options**:
   - Sets user-agent and optional proxy settings (proxy setup is commented out).
   - Hides the Selenium automation flag by setting `navigator.webdriver` to `undefined`, which may help bypass some bot detections.

3. **Login Process**:
   - Opens Twitter login page, inputs email and username, and clicks “Next” to proceed.
   - If a security check page appears, it captures the exception and skips this step.
   - Enters the password and attempts to click the login button.

4. **Post a Tweet**:
   - After a successful login, it locates the tweet text box, enters tweet content, uploads an image, and clicks the “Post” button to publish the tweet.

5. **End Program**: After posting, the script waits briefly and then closes the browser.

## How to Use This Code

### Prerequisites

1. **Install Required Packages**: 
   Before running the code, install `selenium` and `beautifulsoup4`.
   ```bash
   pip install selenium beautifulsoup4

## Setup

### 1. Configure ChromeDriver

- Ensure that ChromeDriver is installed and matches the version of Chrome installed on your system.
- Add ChromeDriver to your system PATH, or specify its path directly in the code if it's located elsewhere on your system.

### 2. Replace Login and Tweet Information

Open the script and replace the following placeholders with your information:

#### Login Details

- `your email address`: Your Twitter login email.
- `your account`: Your Twitter username (formatted as `@username`).
- `your password`: Your Twitter password.

#### Tweet Content

- `input tweet text`: The text you want to tweet.
- `image path`: The absolute path to the image file you want to upload.

### 3. Run the Script

After completing the setup, execute the script. It will open Chrome, log in to Twitter with your credentials, and post a tweet containing your specified text and image.

## Important Notes

- Twitter may detect automation, which could result in login failure or trigger security checks. You may need to modify the script or adjust your approach if Twitter flags automated logins.

## License

This project is licensed under the MIT License.
