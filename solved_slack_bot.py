import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def crawlFromSolved():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('lang=ko_KR')
    # driver = webdriver.Chrome('C:\chromeDriver/chromedriver.exe', options=chrome_options)
    # 로그인
    driver = webdriver.Chrome('C:\chromeDriver/chromedriver.exe')
    link = "https://www.acmicpc.net/login?next=%2Flogin%3Fnext%3D%252Fsso%253Fsso%253Dbm9uY2U9ZDExZGFiZDA1OWFkMjkyZWUwMGE5OWJkNzBiMWYzMzU%25253D%2526sig%253D567d3adcdcb2b9b090ecf8bf86c5ecb9db77d29e5d3d15ec8b2370791d259dd0%2526redirect%253Dhttps%25253A%25252F%25252Fsolved.ac%25252Fsignin%25252Fv2%25252Fsso"
    driver.get(link)

    driver.find_element_by_name("login_user_id").send_keys('twinklesu')
    driver.find_element_by_name("login_password").send_keys('')
    driver.find_element_by_id("submit_button").click()
    driver.implicitly_wait(40000)
    # 문제 갱신
    link = "https://solved.ac/profile/twinklesu14"
    driver.get(link)
    driver.implicitly_wait(20000)
    refresh = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[9]/a')
    refresh.click()
    driver.implicitly_wait(40000)
    driver.close()







def sendingSlack():
    slack_token = "xoxb-1931072743267-2166615551607-hsKcEehGyA0mPE1d82RO8gcw"
    channel_id = "C01TRE6GBQ9"

    message = "slack bot test"

    data = {'Content-Type': 'application/x-www-from-urlencoded',
            'token': slack_token,
            'channel': channel_id,
            'text': message
            }

    URL = 	"https://slack.com/api/chat.postMessage"
    res = requests.post(URL, data=data)


crawlFromSolved()