from wordcloud import WordCloud
import jieba

# print(list(jieba.cut("我要保持正念，用心生活，努力挣钱！")))

with open('必备-Python数据可视化/paragraph.txt',encoding='utf-8') as file:
    text = file.read()
# print(text)

word_list = jieba.cut(text)
WordList = '/'.join(word_list)
# print(WordList)

wordcloud = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf').generate(WordList)
image = wordcloud.to_image()
image.show()