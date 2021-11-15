from collections import defaultdict
from konlpy.tag import Hannanum
import csv

hannanum = Hannanum()
file = open(r"C:\Users\twinklesu\Desktop\focus_group_script.txt", "r", encoding="utf8");
nameList = ["홍성민", "김태희", "이앞길", "김소영", "채성실", "정금섭", "한상성", "정미리", "박종설", "한지호", "차유진", "정미"]
scriptPerOrg = defaultdict(str)
name = ""
while True:
    line = file.readline()
    if not line:
        break
    stripedLine = line.strip()
    if stripedLine:
        # 이름이 나오면,,,
        if stripedLine.split()[0] in nameList:
            name = stripedLine.split()[0]
        else:
            scriptPerOrg[name] += stripedLine

for key in scriptPerOrg:
    wordDict = defaultdict(int)
    x = hannanum.nouns(scriptPerOrg[key])
    for word in x:
        if len(word) > 1 and not str.isdigit(word): # 한글자, 숫자 필터
            wordDict[word] += 1
    with open(key + '_data.csv', 'w', newline='') as csvfile:
        fieldNames = ['단어', '빈도']
        writer = csv.writer(csvfile)

        writer.writerow(fieldNames)
        for k, v in wordDict.items():
            writer.writerow([k, v])
