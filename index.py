from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",  True)
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get("https://10fastfingers.com/typing-test/english")

try: 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#row1 > span.highlight')))
    for i in range(500):
        driver.implicitly_wait(1)
        txt = driver.find_element(By.CSS_SELECTOR, '#row1 > span.highlight').text
        driver.find_element(By.XPATH, '//*[@id="inputfield"]').send_keys(txt + " ")
except TimeoutException:    
    print ("Loading took too much time!")