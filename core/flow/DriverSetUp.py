from selenium import webdriver

class DriverSetUp():
  
  def set_up(self):
    driver = webdriver.Edge()
    
    return driver