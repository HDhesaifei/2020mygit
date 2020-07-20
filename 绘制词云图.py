from wordcloud import  WordCloud
from PIL import Image
import numpy as np
# 绘制词云图
with open('微信聊天记录.txt',encoding='utf-8') as file_obj:
    words = file_obj.read()
    # print(words)
    # wordcloud = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf').generate(words)
    # image = wordcloud.to_image()
    # image.show()

    # wordcloud = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf',background_color='white',width=600,height=300,max_words=50).generate(words)
    # image = wordcloud.to_image()
    # image.show()

    # 绘制制定形状词云图
    images = Image.open('必备-Excle数据可视化/heart.png')
    maskImages = np.array(images)
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf',background_color='white',width=600,height=300,max_words=200,mask=maskImages).generate(words)
    image = wordcloud.to_image()
    image.show()