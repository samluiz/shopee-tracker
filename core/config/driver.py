from selenium import webdriver

class DriverSetUp():
  
  def set_up():
    driver = webdriver.Edge()
    
    return driver