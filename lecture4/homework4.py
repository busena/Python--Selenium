from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")

class Test_Sauce:
    def test_invalid_login(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("")
        sleep(1)
        passwordInput.send_keys("")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(3)
    
    def test_invalid_password(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        usernameInput.clear()
        sleep(3)

    def test_locked(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        driver.refresh()
        sleep(3)

    def test_invalid_icon(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("")
        sleep(1)
        passwordInput.send_keys("")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        errorBtn = driver.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()
        sleep(1)

    def test_inventory(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        lengthOfInventory = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Bu sayfada {len(lengthOfInventory)} tane urun bulunmaktadir.")

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_invalid_password()
testClass.test_locked()
testClass.test_invalid_icon()
testClass.test_inventory()