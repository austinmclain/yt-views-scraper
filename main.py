from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def prompt():
    return input("\nPlease enter the YouTube video URL here: ")

def get_views(url):
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    try:
        views = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="count"]/ytd-video-view-count-renderer/span[1]')))
        return f"That video has {views.text}.\n"
    except:
        return "Something went wrong.\n"

def main():
    url = prompt()
    print(get_views(url))

main()