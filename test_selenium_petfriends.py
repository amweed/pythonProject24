import time

from selenium.webdriver.support.ui import WebDriverWait


def test_petfriends(selenium):

    selenium.get("https://petfriends1.herokuapp.com/")
    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()


    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element_by_xpath('//*[@id="email"]')
    field_email.send_keys("point@mail.ru")


    field_pass = selenium.find_element_by_id("pass")
    field_pass.send_keys("90point90")

    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    #element = WebDriverWait(selenium, 10).until(selenium.find_element_by_xpath("/html/body/nav/div[1]/ul/li[1]/a"))

    btn_exist_acc = selenium.find_element_by_xpath("/html/body/nav/div[1]/ul/li[1]/a")
    btn_exist_acc.click()
    time.sleep(2)
    ad = selenium.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/button')
    ad.click()

'''
    Коментария
    Или запустить
    from selenium.webdriver.support.ui import WebDriverWait
    должна работать!  (нужно убрать "#" строка 27)!
    element = WebDriverWait(selenium, 10).until(selenium.find_element_by_xpath("/html/body/nav/div[1]/ul/li[1]/a"))
    (тогда поставить "#" строка 29-30) 
'''
