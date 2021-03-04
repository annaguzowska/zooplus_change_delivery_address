from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://pl-pl.facebook.com/")

#accept cookies
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Akceptuj wszystkie']")))
driver.find_element_by_xpath("//button[text()='Akceptuj wszystkie']").click()

def log_in(login, password):
    driver.find_element_by_id('email').send_keys(login)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_xpath("//button[text()='Zaloguj się']").click()

log_in("your login", "your password" )
