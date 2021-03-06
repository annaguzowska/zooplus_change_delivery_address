from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.zooplus.pl/")

# accept cookies
wait.until(expected_conditions.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
driver.find_element_by_id('onetrust-accept-btn-handler').click()


def log_in(login, password):

    driver.find_element_by_xpath("//span[text()='Mój zooplus']").click()
    wait.until(expected_conditions.element_to_be_clickable((By.ID, 'login-email')))
    driver.find_element_by_id("login-email").send_keys(login)
    driver.find_element_by_id("login-password").send_keys(password)
    driver.find_element_by_id("loginButton").click()
    wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Wyloguj')))
    assert driver.find_element(By.LINK_TEXT, "Wyloguj").is_displayed()


log_in("your login", "your password")


# click "Moje dane" button
driver.find_element_by_xpath("//li[@class='MenuBlock-zooplus-module__MenuBlock--fkq8J8iA9N']/ul/li/a").click()


def change_delivery_address(salutation, name, surname, street_name_house_number, postcode, city):
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='mzp-customer-data']/div[5]/a")))
    driver.find_element_by_xpath("//div[@id='mzp-customer-data']/div[5]/a").click()
    driver.find_element_by_xpath("//div[@class='new__address']/button").click()
    driver.find_element_by_xpath(f"//option[text()='{salutation}']").click()
    driver.find_element_by_id('shippingAddress.firstName').send_keys(name)
    driver.find_element_by_id('shippingAddress.lastName').send_keys(surname)
    driver.find_element_by_id('shippingAddress.street').send_keys(street_name_house_number)
    driver.find_element_by_id('shippingAddress.postalCode').send_keys(postcode)
    driver.find_element_by_id('shippingAddress.city').send_keys(city)
    driver.find_element_by_xpath("//span[text()='Zmień i zapisz']").click()


change_delivery_address('your salutation', 'your name', 'your surname', 'your street name and house number', 'your postcode', 'your city')
# salutation: you can choose: Pani, Pan, Dr. or Prof.







