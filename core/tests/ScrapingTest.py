from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class LoginTest(unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Edge()
    
  def test_login(self):
    driver = self.driver
    driver.get("https://shopee.com.br/")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/header/div[1]/nav/ul/a[3]"))
    ).click()
    
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input"))
    )
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input"))
    )
    
    form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form"))
    )
    
    login_input.send_keys("teste@email.com")
    password_input.send_keys("testesenha")
    password_input.send_keys(Keys.ENTER)
    
    wrong_credentials = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[1]"))
    )
    
    time.sleep(2)
    
    self.assertEqual(login_input.get_attribute("name"), 'loginKey')
    self.assertEqual(password_input.get_attribute("name"), 'password')
    self.assertEqual(wrong_credentials.is_displayed(), True)
    

  def tearDown(self):
    self.driver.close()
    

if __name__ == "__main__":
  unittest.main()