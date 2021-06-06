from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from getpass import getpass

class IGBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        time.sleep(1)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        if len(bot.find_elements_by_id('slfErrorAlert')) > 0:
            print("Wrong credentials. Try again.")
            login(self)
        else:
            print("Correct credentials! If problems occur, check if Instagram's security protocol is preventing login.")

    def like_post(self, hashtag):
        bot = self.bot
        bot.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(1)
        for i in range(1,10):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
        posts = bot.find_elements_by_class_name('v1Nh3')
        links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
        for link in links:
            bot.get(link)
            try:
                bot.find_element_by_css_selector("svg[aria-label='Like']").click()
                time.sleep(1)
            except Exception as ex:
                time.sleep(5)

print("Instagram Login:")
your_username = input("Enter your username: ")
your_password = getpass("Enter your password (hidden): ")
your_hashtag = input("Enter your desired hashtag (no # needed): ")
print("You're all set! For Windows, press Ctrl+C to terminate program.")

ed = IGBot(your_username, your_password)
ed.login()

while True:
    ed.like_post(your_hashtag)