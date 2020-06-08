from googletrans import Translator
import xlrd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

translator = Translator()

wb = xlrd.open_workbook("Dataset.xlsx")
sheet = wb.sheet_by_index(0) 
num_rows = sheet.nrows

x_axis = ["neg", "neu", "pos"]
y_axis = [0, 0, 0]

scatter_x = []
scatter_y = []

for i in range(1, num_rows):
    sentence = sheet.cell_value(i,0)
    translations = translator.translate(sentence.encode('unicode-escape').decode('ASCII'), dest='en')
    trans_text = translations.text
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(trans_text)
    
    print(result)

    if(result["compound"] < 0):
        y_axis[0] += 1
        scatter_x.append(result["compound"])
        scatter_y.append("neg")

    if(result["compound"] == 0):
        y_axis[1] += 1
        scatter_x.append(result["compound"])
        scatter_y.append("neu")
    
    if(result["compound"] > 0):
        y_axis[2] += 1
        scatter_x.append(result["compound"])
        scatter_y.append("pos")

bar_graph = plt.figure(1)
plt.bar(x_axis, y_axis)

scatter_plot = plt.figure(2)
plt.scatter(scatter_x, scatter_y)

plt.title("Sentiment Analysis of Hinglish Sentences")

plt.show()