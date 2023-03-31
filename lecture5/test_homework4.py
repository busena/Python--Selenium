from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl 
from constants import globalConstants as gc

class Test_sauceDemo:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(gc.URL)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_invalid_login(self,username,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        usernameInput = gc.find_element(By.ID,"user-name")
        passwordInput = gc.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = gc.find_element(By.ID, "login-button")
        loginBtn.click()

    @pytest.mark.parametrize("username,password",[("standard_user","")])
    def test_invalid_password(self,username,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        usernameInput = gc.find_element(By.ID,"user-name")
        passwordInput = gc.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = gc.find_element(By.ID, "login-button")
        loginBtn.click()

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked(self,username,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        usernameInput = gc.find_element(By.ID,"user-name")
        passwordInput = gc.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = gc.find_element(By.ID, "login-button")
        loginBtn.click()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_invalid_icon(self,username,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        usernameInput = gc.find_element(By.ID,"user-name")
        passwordInput = gc.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = gc.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        errorBtn = gc.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_inventory(self,username,password):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        usernameInput = gc.find_element(By.ID,"user-name")
        passwordInput = gc.find_element(By.ID,"password")

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()

        loginBtn = gc.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        lengthOfInventory = gc.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Bu sayfada {len(lengthOfInventory)} tane urun bulunmaktadir.")
