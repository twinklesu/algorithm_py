import json

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def crawlFromSolved():
    url = 'https://solved.ac/problems/level/9?sort=solved&direction=desc&page=1'

    req = requests.get(url)
    if req.status_code == 200:
        start_numbers = int(input("시작 번호 입력"))
        count = 0
        eight_q = []
        html = req.text
        bs = BeautifulSoup(html, 'html.parser')
        a = bs.select('a.ProblemInline__ProblemStyle-cvf1lm-0.ivEtZs')
        for aa in a:
            span = aa.select_one('span')
            num = span.get_text()
            if int(num) == start_numbers:
                count = 1
            if 0 < count <= 9:
                eight_q.append(num)
                count += 1
            if count == 9:
                sendingSlack(eight_q)
                break
        else:
            print("다음 페이지")
    else:
        print("http error")


def sendingSlack(questions: list):
    monday = datetime.today()
    sunday = monday + timedelta(days=6)
    monday = monday.strftime('%m/%d')
    sunday = sunday.strftime('%m/%d')


    slack_token = "xoxb-1931072743267-2166615551607-YAyQee5iAgldno9JLTyLW1M8"
    channel_id = "C01TRE6GBQ9"

    message = "👩🏻‍💻" + monday + "~" + sunday + "👩🏻‍💻\n"
    message += str(questions)[1:-1].replace('\'', '')
    print(message)

    headers = {
        "Content-type": "application/json",
        'Authorization': 'Bearer ' + slack_token
    }

    payload = {
            'channel': channel_id,
            'text': "Subin test bot"
            }

    URL = 	"https://slack.com/api/chat.postMessage"
    res = requests.post(URL, headers=headers, data=json.dumps(payload))

    print(res.status_code)


crawlFromSolved()