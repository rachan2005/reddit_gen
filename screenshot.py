from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Config
screenshotDir = "Screenshots"
screenWidth = 1920
screenHeight = 1080

def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver, wait = __setupDriver(script.url)
    try:
        print(script.fileName)
        script.titleSCFile = __takeScreenshot(filePrefix, driver, wait, 0, f"t3_{script.fileName.split('-')[-1]}")
        for commentFrame in script.frames:
            commentFrame.screenShotFile = __takeScreenshot(filePrefix, driver, wait, 1, f"t1_{commentFrame.commentId}")
    finally:
        driver.quit()

def __takeScreenshot(filePrefix, driver, wait, d, handle):
    # Determine the method and locator based on the value of d
    if d == 0:
        method = By.ID
        locator = handle
    else:
        method = By.XPATH
        locator = f'//*[@thingid="{handle}"]'  # Locate element by custom attribute using XPath

    print(f"Attempting to locate element: {handle} with method: {method}")
    try:
        # Wait until the element is visible
        search = wait.until(EC.visibility_of_element_located((method, locator)))
        driver.execute_script("window.focus();")

        # Save the screenshot of the element
        fileName = f"{screenshotDir}/{filePrefix}-{handle}.png"
        with open(fileName, "wb") as fp:
            fp.write(search.screenshot_as_png)
        print(f"Screenshot saved: {fileName}")
        return fileName
    except TimeoutException:
        print(f"Timeout: Unable to locate element '{handle}' using method '{method}'.")
        driver.save_screenshot(f"{screenshotDir}/{filePrefix}-error.png")
        raise

def __setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.add_argument("--private")  # Enable incognito mode for Firefox
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 100)  # Increased timeout for slow-loading pages

    driver.set_window_size(width=screenWidth, height=screenHeight)
    print(f"Navigating to URL: {url}")
    driver.get(url)

    return driver, wait
