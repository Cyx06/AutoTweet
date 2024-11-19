# Pixiv Automation Script

This script automates the login and illustration posting process on [Pixiv](https://www.pixiv.net/). It uses **Selenium** for browser automation and performs actions like uploading an image, setting metadata, and publishing an illustration.

---

## Features

- Logs into Pixiv using environment variables for credentials.
- Automates illustration creation and publishing.
- Inputs title, tags, and description for the uploaded illustration.
- Configures restrictions like content type and AI generation settings.
- Clicks the "Post" button to publish the illustration (disabled by default).

---

## Requirements

### 1. **Environment Variables**:
   Ensure the following environment variables are set:
   - `PIXIV_EMAIL`: Your Pixiv account email.
   - `PIXIV_PASSWORD`: Your Pixiv account password.
   - `IMAGE_PATH`: Absolute path to the image you want to upload.

### 2. **Python Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install selenium beautifulsoup4
   ```

### 3. **ChromeDriver**:
   - Download the [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) version compatible with your Chrome browser.
   - Add the ChromeDriver executable to your system's PATH or specify its location when initializing the `webdriver`.

## Code Description

1. **Imports**:
   - `selenium`: Automates browser actions.
   - `time.sleep`: Adds delays between actions for stability.
   - `BeautifulSoup`: Parses HTML content for advanced checks (if needed).

2. **Browser Configuration**:
   - Sets up `ChromeOptions` for customizing browser behavior.
   - Disables WebDriver detection using Chrome DevTools Protocol (CDP).
   - Configures a user agent string and proxy server (optional).

3. **Login Process**:
   - Navigates to the Pixiv login page.
   - Inputs email and password from environment variables.
   - Clicks the "Log In" button.

4. **Illustration Creation**:
   - Navigates to the illustration creation page.
   - Uploads an image using `input[type="file"]`.
   - Inputs title, comment, tags, and other metadata.

5. **Content Settings**:
   - Sets restrictions (e.g., general content).
   - Marks sexual content as "false".
   - Marks the illustration as "Not AI Generated".

6. **Illustration Creation**:
   - Clicks the "Post" button (disabled by default for safety).

## How to Use This Code

### 1. Replace Login and PIXIV Content Information

Open the script and replace the following placeholders with your information:

#### Login Details

- `PIXIV_EMAIL`: Your PIXIV login email.
- `PIXIV_PASSWORD`: Your PIXIV login password.

#### PIXIV Content Details

- `IMAGE_PATH`: The absolute path of the image to upload.
- `IMAGE_TITLE`: The title of the post to upload.
- `IMAGE_COMMENT`: The comment of the post to upload.

### 2. Run the Script

After completing the setup, execute the script, the script will post setted illustration, title, and context.