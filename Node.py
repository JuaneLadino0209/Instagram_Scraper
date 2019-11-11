from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class node:
    def __init__(self,User):
        self.user = User
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        sleep(2)
        print("Correct conexion Browser and Instagram\n")
        login_elem = self.browser.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[2]/p/a')
        login_elem.click()
        sleep(1)
        print("Login page\n")
        inputs = self.browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        inputs1 = self.browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        
        webdriver.common.action_chains.ActionChains(self.browser)\
            .move_to_element(inputs).click()\
            .send_keys('estebanladino@hotmail.com')\
            .move_to_element(inputs1).click()\
            .send_keys('juanestebanladino')\
            .perform()
        
        login_button = self.browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]')
        
        webdriver.common.action_chains.ActionChains(self.browser)\
           .move_to_element(login_button)\
           .click().perform()
        sleep(6)
        print("Correct Login\n")
        
        turn_of_button = self.browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        webdriver.common.action_chains.ActionChains(self.browser)\
           .move_to_element(turn_of_button)\
           .click().perform()
        sleep(2)
        print("Succesfull Conection")

    def get_follow_list(self):
        follow_list = []
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        print("Correct conection " + self.user + "\n")
        follow_button = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
        webdriver.common.action_chains.ActionChains(self.browser)\
           .move_to_element(follow_button)\
           .click().perform()
        sleep(1)
        print("Correct Conection Follow button...\n")
        print("preparing Scroll function\n")
        
        temp = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a/span')
        num_follow = temp.text
        print("num of follow users: " + str(num_follow) + "\n")
        scroll_button = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]')
        print("Scrolling follow user, please whait ......")
        for i in range(0,5):
            scroll_button.send_keys(Keys.DOWN)
            sleep(0.6)
        while True:
            try:
                name = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+num_follow+']/div/div[1]/div[2]/div[1]/a')
                print("Correct break infinite loop.\n")
                break
            except NoSuchElementException:  #spelling error making this code not work as expected
                for i in range(0,50):
                    scroll_button.send_keys(Keys.DOWN)
            pass
        print("Scroll succesfull.......\n\n")
        
        
        for i in range(1,int(num_follow) +1):
            name = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/a')
            follow_list.append(name.text)
        print("Succesfull, Correct conexion get_follow_list.\n")        
        return follow_list
    
    def get_following_list(self):
        following_list = []
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        print("Correct conection " + self.user + "\n")
        following_button = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a')
        webdriver.common.action_chains.ActionChains(self.browser)\
           .move_to_element(following_button)\
           .click().perform()
        sleep(1)
        print("Correct Conection Follow button...\n")
        print("preparing Scroll function\n")
        
        temp = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span')
        num_following = temp.text
        print("num of following users: " + str(num_following) + "\n")
        scroll_button = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]')
        print("Scrolling following users, please whait ......")
        for i in range(0,5):
            scroll_button.send_keys(Keys.DOWN)
            sleep(0.6)
        while True:
            try:
                name = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+num_following+']/div/div[1]/div[2]/div[1]/a')
                print("Correct Break infinite loop.\n")
                break
            except NoSuchElementException:  #spelling error making this code not work as expected
                for i in range(0,50):
                    scroll_button.send_keys(Keys.DOWN)
            pass
        print("Scroll succesfull.......\n\n")
        
        
        for i in range(1,int(num_following) +1):
            name = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/a')
            following_list.append(name.text)
        print("Succesfull, Correct conexion get_following_list.\n")        
        return following_list
    
    def get_biography(self):
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        biography = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/div[2]/span')
        return(biography.text)
    def get_name(self):
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        name = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/div[2]/h1')
        return(name.text)
    def get_like(self):
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        sleep(2)
        #self.browser.execute_script("window.scrollTo(0, 600)") 
            
        webdriver.common.action_chains.ActionChains(self.browser)\
           .move_by_offset(207, 700)\
           .click().perform()
        
            
        

        
        
User = node("davidzabaletar")
#followList = User.get_follow_list()
#followingList = User.get_following_list()
#biography = User.get_biography()
#name = User.get_name()
User.get_like()

                
        