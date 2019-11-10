from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

browser = webdriver.Firefox(executable_path='./geckodriver')
#browser.set_window_size(900,900)
browser.maximize_window()
#sleep(3)
browser.get("https://www.instagram.com/")
sleep(2)
login_elem = browser.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[2]/p/a')
login_elem.click()
sleep(1)
inputs = browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
inputs1 = browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')

webdriver.common.action_chains.ActionChains(browser)\
    .move_to_element(inputs).click()\
    .send_keys('estebanladino@hotmail.com')\
    .move_to_element(inputs1).click()\
    .send_keys('juanestebanladino')\
    .perform()

login_button = browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]')

webdriver.common.action_chains.ActionChains(browser)\
   .move_to_element(login_button)\
   .click().perform()
sleep(6)

turn_of_button = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
webdriver.common.action_chains.ActionChains(browser)\
   .move_to_element(turn_of_button)\
   .click().perform()
sleep(2)

browser.get("https://www.instagram.com/valelopezch/")

following_button = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
webdriver.common.action_chains.ActionChains(browser)\
   .move_to_element(following_button)\
   .click().perform()
sleep(1)


temp = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a/span')
num_following = temp.text
print(num_following)
scroll_button = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]')

for i in range(0,5):
    scroll_button.send_keys(Keys.DOWN)
    sleep(0.6)
while True:
    try:
        name = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+num_following+']/div/div[1]/div[2]/div[1]/a')
        print("Hello World")
        break
    except NoSuchElementException:  #spelling error making this code not work as expected
        for i in range(0,50):
            scroll_button.send_keys(Keys.DOWN)
    pass
print("succesfull.......\n\n")


for i in range(1,int(num_following) +1):
    name = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/a')
    print(name.text)

sleep(5)
#browser.close()

#/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/a
#/html/body/div[3]/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/a
#/html/body/div[3]/div/div[2]/ul/div/li[3]/div/div[2]/div[1]/div/div/a
#/html/body/div[3]/div/div[2]/ul/div/li[4]/div/div[2]/div[1]/div/div/a
