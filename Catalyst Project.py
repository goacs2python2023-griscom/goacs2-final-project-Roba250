
data = {}
data1 = {}

f = open("Grade8.txt", "r", encoding='utf-8')
for line in f:
    line = line.strip()
    (state, score)= line.split("|")
    #score = score.split(",")
    data[state]= int(score)
    
#print(data)

k = open("Grade4.txt", "r", encoding='utf-8')
for line in k:
    line = line.strip()
    (state1, score1)= line.split("|")
    #score = score.split(",")
    data1[state1]= int(score1)
    


from bokeh.plotting import figure, show
import math
import numpy as np
from bokeh.plotting import ColumnDataSource

                
dataNames = list(data)
dataNames1 = list(data1)

dataScores = []
dataScores1 = []


for names in dataNames:
    dataScores.append(data[names])
for names1 in dataNames1:
    dataScores1.append(data1[names1])

source = ColumnDataSource(data=dict(
    x = np.arange(54),
    y1 = dataScores,
    y2 = dataScores1
))
print (dataScores1, dataScores)

g = figure(width = 1000, height = 500)
g.line(np.arange(54), dataScores,line_width=2, color="Red")
g.line(np.arange(54), dataScores1,line_width=2, color = "Blue")
g.circle(np.arange(54), dataScores, fill_color="white", size=8)
g.circle(np.arange(54), dataScores1, fill_color="white", size=8)


for i in range (54):    
    g.text(i+.5,0,[dataNames[i-1]],math.pi/2, text_font_size = "10pt")
    

show(g)
#print(dataNames)
