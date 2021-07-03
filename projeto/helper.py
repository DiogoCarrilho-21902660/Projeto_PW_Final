import matplotlib.pyplot as plt
from io import StringIO
import numpy as np


# esta funcao mostra um pie chart depois do quizz ser submetido
def return_graph(x, y):
    y = np.array([x, y])                    #numpy array
    mylabels = ["Correto", "Incorreto"]     #nomes do grafico
    mycolors = ["green", "red"]             #cores do grafico

    plt.pie(y, colors=mycolors, labels=mylabels)      #plotting the chart

    imgdata = StringIO()                            # rendering the plot into an svg to be shown
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
