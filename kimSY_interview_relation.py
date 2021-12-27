from konlpy.tag import Hannanum
import re
from apyori import apriori
import pandas as pd
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

hannanum = Hannanum()
file = open(r"C:\Users\twinklesu\Desktop\focus_group_script.txt", "r", encoding="utf8")
nounList = []
nameList = ["홍성민", "김태희", "이앞길", "김소영", "채성실", "정금섭", "한상성", "정미리", "박종설", "한지호", "차유진", "정미"]
stopWords = ["교수님", "그분들", "하나", "얘기", "가지", "이거", "우리", "거의", "경우", "생각", "말씀", "저희", '기관', '것들', '선생님들', '진행', '시간', '감사']
stopWords.extend(nameList)
lineList = []
while True:
    line = file.readline()
    if not line:
        break
    if line.strip(): # 공백제거
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        newLine = hangul.sub('', line.strip())
        lineList.append(newLine)
        x = hannanum.nouns(newLine)
        x = [noun for noun in x if noun not in stopWords and len(noun) > 1]
        if x:
            nounList.append(x)

# 연관 분석
results = list(apriori(nounList, min_support=0.01, max_length=2))
columns = ['source', 'target', 'support']
networkDf = pd.DataFrame(columns = columns)

meaningfulWords = []

for result in results:
    if len(result.items) == 2:
        items = [x for x in result.items]
        row = [items[0], items[1], result.support]
        meaningfulWords.append(items[0])
        meaningfulWords.append(items[1])
        series = pd.Series(row, index=networkDf.columns)
        networkDf = networkDf.append(series, ignore_index=True)

print(networkDf)
corpusNoun = []
for nounli in nounList:
    corpusNoun.extend(nounli)
count = Counter(corpusNoun)

node_df = pd.DataFrame(count.items(), columns=['node', 'nodesize'])
node_df = node_df[node_df['nodesize'] >= 20] # 시각화의 편의를 위해 ‘nodesize’ 5 이하는 제거합니다.
print(node_df)

plt.figure(figsize=(25,25))

G = nx.Graph()

for index, row in node_df.iterrows():
    if row['node'] in meaningfulWords:
        G.add_node(row['node'], nodesize=row['nodesize'])

for index, row in networkDf.iterrows():
    G.add_weighted_edges_from([(row['source'], row['target'], row['support'])], )


pos = nx.spring_layout(G, k=0.6, iterations=50)
sizes = [G.nodes[node]['nodesize']*100 for node in G]
nx.draw(G, pos=pos, node_size=sizes)

nx.draw_networkx_nodes(G, pos=pos, node_size=sizes, node_color='lightgrey')



font_path = "C:\Windows\Fonts\malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
nx.draw_networkx_labels(G, pos=pos, font_family=rc('font', family=font), font_size=25)

ax = plt.gca()
plt.show()
