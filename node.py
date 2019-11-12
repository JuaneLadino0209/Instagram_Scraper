from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Node:
    def __init__(self,User):
        self.user = User
        #self.user2 = User2
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

        turn_of_button = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[1]')
        #turn_of_button = self.browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
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
        sleep(2)
        biography = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/div[2]/span')
        return(biography.text)

    def get_name(self):
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        sleep(2)
        name = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/div[2]/h1')
        return(name.text)

    def get_likes(self):
        num_likes = 0
        num_videos = 0
        self.browser.get("https://www.instagram.com/"+self.user+"/")
        sleep(2)
        temp = self.browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[1]/span/span')
        num_pub = temp.text
        print("number of publications: " + num_pub + "\n")
        self.browser.execute_script("window.scrollTo(0,650);")
        print("counting number of likes, please whai a few minutes .....\n")

        photo_button = self.browser.find_element_by_xpath('/html/body/span/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[1]')
        webdriver.common.action_chains.ActionChains(self.browser)\
            .move_to_element(photo_button)\
            .click().perform()
        sleep(1)
        next_button = self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a')
        for i in range(1, int(num_pub)):
            try:
                video_button = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/span')
                webdriver.common.action_chains.ActionChains(self.browser)\
                    .move_to_element(video_button)\
                    .click().perform()
                likes = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/div[4]/span')
                num_likes = num_likes + int(likes.text.replace('.',''))
                webdriver.common.action_chains.ActionChains(self.browser)\
                    .move_to_element(video_button)\
                    .click().perform()
                webdriver.common.action_chains.ActionChains(self.browser)\
                    .move_to_element(next_button)\
                    .click().perform()
                sleep(1)
            except NoSuchElementException:
                try:
                    likes = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span')
                    num_likes = num_likes + int(likes.text.replace('.','')) + 1/html/body/div[3]/div/div/div[3]/button[2]
                except NoSuchElementException:  #spelling error making this code not work as expected
                    likes = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/button/span')
                    num_likes = num_likes + int(likes.text.replace('.',''))
                pass
                webdriver.common.action_chains.ActionChains(self.browser)\
                    .move_to_element(next_button)\
                    .click().perform()
                sleep(1)
            pass
        print('Succesfull get_likes function.\n')
        return(int(num_pub),num_likes)

    def get_username(self):
        return self.user
    def prove(self):
        soccer = ['cristiano','leomessi','davidBeckham','fifaworldcup','433','neymarjr','realmadrid','fcbarcelona','paulpogba','championsleague','sporf','goalglobal','premierleague','laliga','seriea','bundesliga_en','futbolalreves','falcao','jamesrodriguez10']
        basquet = ['nba','kingjames','stephencurry30','jharden13','russwest44','easymoneysniper','kyrieirving','nbatv','lakers','warriors','nbaontnt','jumpman23','giannis_an34','houseofhighlights']
        Reguetton = ['anuel_2blea','daddyyankee','mturizomusic','nickyjampr','ozuna','brytiago','sechmusic','lunay','nattinatasha','karolg','farrukoofficial','iambeckyg','maluma','zion','jbalvin','jquiles','badbunnypr']
        Pop = ['justinbieber','champagnepapi','teddysphotos','brunomars','taylorswift','selenagomez','dualipa','camila_cabello','iamcardib','lanadelrey','jlo','shakira','katyperry','ladygaga','arianagrande','badgalriri','postmalone','travisscott','tyga','wizkhalifa']
        electronic = ['zedd','calvinharris','alesso','skrillex','alanwalkermusic','martingarrix','majorlazer','marshmellomusic','diplo','tiesto','davidguetta','thechainsmokers','djsnake','afrojack']

        Paction = ['schwarzenegger','robertdowneyjr','chrishemsworth','thehughjackman','markruffalo','tomholland2013','universalpictures','avengers','marvelstudios','dccomics','therock','marvel']
        Pcomedy = ['Kevinhart4real','adamsandler','jenniferaniston','jimmyfallon','theellenshow','davidspade','jackblack','willsmith','chrisrock','','','','','','']
        Pteens = ['zendaya', 'emmawatson', 'thecameronboyce', 'ddlovato', 'mileycyrus', 'zacefron',  'debbyryan', 'colesprouse', 'nickjonas', 'bellathorne',  'bridgitmendler']

        youTube = ['auronplay','soydrossrotzank','ksi','loganpaul','jakepaul','riceGum','lelepons','susanojose','curtislepore','pewdepie','elrubiuswtf','germangarmendia']
        models = ['caradelevingne','KimKardashian','Kyliejenner','Kendalljenner','gigihadid','bellahadid','KhloeKardashian','haileybieber','alexisren','alessandraambrosio','lilyjcollins']

        beauty_Health = ['fitgirlsguide','wakeupandmakeup','kyliecosmetics','Kendallandkylie','kylieskin','saschafitness','howto.makeup','fashionweek','fashionnova']
        netflix = [ 'ester_exposito', 'itzan.escamilla', 'milliebobbybrown', 'asabopp', 'noahschnapp', '13reasonswhy', 'dylanminnette', 'justin.prentice', 'lacasadepapel', 'jaimelorentelo', 'miguel.g.herran', 'ursulolita']
        series = ['darknetflix' , 'gameofthrones', 'suits_usa', 'houseofcards', 'cw_arrow', 'cwtheflash', 'friends', 'thewalkingdead', 'blackmirror.netflix', 'peakyblindersofficial']

        memes = ['9gag','jokezar','memezar','moriderisa','paradamaslaoficial','badabun','paracaballerosoficial','bestvines','funnyhoodvidz','el_coyote_cojo','worldstar','queboleta','juanpisgonzales']

        fortnite = ['fortnite', 'forrtnite',  'tfue', 'ninja', 'tsm_myth', 'tsm_daequan', 'couragejd', 'bugha', 'ighdistortion', 'hamlinz', 'mongraal']

        list = []
        list.append(soccer)
        list.append(basquet)
        list.append(Reguetton)
        list.append(Pop)
        list.append(electronic)
        list.append(Paction)
        list.append(Pcomedy)
        list.append(Pteens)
        list.append(youTube)
        list.append(models)
        list.append(beauty_Health)
        list.append(netflix)
        list.append(series)
        list.append(memes)
        list.append(fortnite)
        for i in list:
            for j in i:
                self.browser.get('https://www.instagram.com/'+j+'/')
                print(j)
                sleep(0.8)


if __name__ == "__main__":
    User = Node("valentina_9707")
    User.prove()
    #User2 = Node("camilarocet")
    #followingList = User.get_follow_list()
    #biography = User.get_biography()
    #name = User.get_name()
    #likes = User.get_likes()
    #print(followingList)
    #print(followList)
    #print(biography)
    #print(name)
