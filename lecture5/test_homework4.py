from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl

class Test_odevTesti:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_invalid_login(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_username_password-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    
    def waitForElementVisible(self,locator,timeout=3):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    @pytest.mark.parametrize("username,password",[("standard_user","")])
    def test_invalid_password(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_password-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_username_password-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,password",[("","")])
    def test_invalid_icon(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3") 
        self.driver.save_screenshot(f"{self.folderPath}/test_icon_username_password-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username is required."

        errorBtn = self.waitForElementVisible((By.ID,("error-button")))
        errorBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_icon2_username_password-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_inventory(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.waitForElementVisible((By.CLASS_NAME,("app_logo")))
        self.driver.save_screenshot(f"{self.folderPath}/test_successful_username_password-{username}-{password}.png")

        lengthOfInventory = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Bu sayfada {len(lengthOfInventory)} tane urun bulunmaktadir.")

# *****************************************************************************************************
# TEST 1
    list_of_elements = [("buse","sena"),("user","123"),("kodlamaio","987")]
    @pytest.mark.parametrize("username,password",list_of_elements)
    def test_multiple_user(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service" 
        self.driver.save_screenshot(f"{self.folderPath}/test_multiple_username_password-{username}-{password}.png")

# TEST 2
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_productCheck(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        product = self.waitForElementVisible((By.XPATH,("//*[@id='add-to-cart-sauce-labs-backpack']")))
        product.click()
        
        self.waitForElementVisible((By.XPATH,("//*[@id='remove-sauce-labs-backpack']")))
        self.driver.save_screenshot(f"{self.folderPath}/test_product_username_password-{username}-{password}.png")

# TEST 3
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_basketCheck(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        basket = self.waitForElementVisible((By.XPATH,("//*[@id='shopping_cart_container']/a")))
        basket.click()
        
        self.waitForElementVisible((By.XPATH,("//*[@id='remove-sauce-labs-backpack']")))
        self.driver.save_screenshot(f"{self.folderPath}/test_basket_username_password-{username}-{password}.png")