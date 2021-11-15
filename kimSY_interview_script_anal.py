from collections import defaultdict
from konlpy.tag import Hannanum
import csv

hannanum = Hannanum()
file = open(r"C:\Users\twinklesu\Desktop\focus_group_script.txt", "r", encoding="utf8");
wordDict = defaultdict(int)
while True:
    line = file.readline()
    if not line:
        break
    if line.strip(): # 공백제거
        x = hannanum.nouns(line.strip())
        for word in x:
            wordDict[word] += 1

wordCountList = []
nameList = ["홍성민", "김태희", "이앞길", "김소영", "채성실", "정금섭", "한상성", "정미", "박종설", "한지호"]
for key in wordDict:
    # 한 글자인 명사 제거 (저, 것, 수, 들...)
    if len(key) >= 2 and key not in nameList:
        wordCountList.append([key, wordDict[key]])
wordCountList.sort(key=lambda a: a[1], reverse=True)
print(wordCountList)

with open('word_data.csv', 'w', newline='') as csvfile:
    filedNames = ['단어', '빈도']
    writer = csv.writer(csvfile)

    writer.writerow(filedNames)
    writer.writerows(wordCountList)


