from wordcloud import WordCloud

text = ""

with open('텍스트파일', 'r', encoding="utf-8") as txt:
    lines = txt.readlines()

    for line in lines[4:]:
        if '] [' in line:
            text += (line.split('] ')[2].replace('이모티콘\n', "")
                     .replace("사진\n", "").replace('삭제된 메세지입니다.\n', "").replace('ㅎ', '').replace("샵검색", '').replace('ㅋ', '').replace('ㅠ', "").replace('ㅇ', ''))

stopwords = {'안녕하세요', '여러분', 'http', 'https', 'com', '아', '넵','제가','네','저','혹시','저도','아니','근데','오늘','다들','오','저는'} # 제거할 단어
wc = WordCloud(font_path="C:\Windows\Fonts\malgun.ttf", stopwords=stopwords, background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("image.png")