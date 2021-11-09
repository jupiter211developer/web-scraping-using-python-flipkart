from selenium import webdriver

path = r'D:/DEV TOOLS/chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://tutorialspoint.com/')
screenshot = browser.save_screenshot('screenshot.png')
browser.quit()