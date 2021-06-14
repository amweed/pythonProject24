from selenium import webdriver
import pytest
import time
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Predator/tests/chrome/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()

def test_show_my_pets():

   pytest.driver.find_element_by_id('email').send_keys('point@mail.ru')

   pytest.driver.find_element_by_id('pass').send_keys('90point90')

   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]').click()

   pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/button').click()

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0





