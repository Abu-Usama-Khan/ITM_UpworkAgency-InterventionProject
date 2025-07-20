import undetected_chromedriver as uc



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#Setup chrome Driver

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("disable-blink-features=AutomationControlled")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")


driver = uc.Chrome(options=options,version_main=138) #Version must match your chrome

driver.get("https://www.investing.com")

WebDriverWait(driver, 10)


# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Setup Chrome driver options
# options = uc.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--start-maximized")

# # Launch the browser
# driver = uc.Chrome(options=options, version_main=138)

# # Visit Investing.com
# driver.get("https://www.investing.com")
# time.sleep(5)  # Let the page load

# # Open Chrome.com in new tab
# driver.execute_script("window.open('https://www.chrome.com', '_blank');")
# time.sleep(5)  # Allow some time to see the tab

# # Optional: Switch to second tab
# driver.switch_to.window(driver.window_handles[1])
# print("Now on:", driver.current_url)

# # Optional: Switch back to first tab
# driver.switch_to.window(driver.window_handles[0])
# print("Back to:", driver.current_url)

# # Cleanup: Close browser after a few seconds
# time.sleep(5)
# driver.quit()

