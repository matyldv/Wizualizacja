import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane1 = pd.read_csv("http://www.cs.put.poznan.pl/mtomczyk/kck/Lab1_python_tutorial/results/2cel-rs.csv", sep=",")
dane2 = pd.read_csv("http://www.cs.put.poznan.pl/mtomczyk/kck/Lab1_python_tutorial/results/2cel.csv", sep=",")
dane3 = pd.read_csv("http://www.cs.put.poznan.pl/mtomczyk/kck/Lab1_python_tutorial/results/cel-rs.csv", sep=",")
dane4 = pd.read_csv("http://www.cs.put.poznan.pl/mtomczyk/kck/Lab1_python_tutorial/results/cel.csv", sep=",")
dane5 = pd.read_csv("http://www.cs.put.poznan.pl/mtomczyk/kck/Lab1_python_tutorial/results/rsel.csv", sep=",")

def wykres(dane):
    x = []
    y = []
    z = []
    for i in range(dane.shape[0]):
        x.append(dane.iloc[i][0])
        y.append(dane.iloc[i][1]/1000)
        z.append(dane.iloc[i][2:].mean()*100)

    return x, y, z

def wykres2(dane):
    a = dane.iloc[dane.shape[0]-1][2:] * 100
    return a



x1, y1, z1 = wykres(dane1)
x2, y2, z2 = wykres(dane2)
x3, y3, z3 = wykres(dane3)
x4, y4, z4 = wykres(dane4)
x5, y5, z5 = wykres(dane5)

a1 = wykres2(dane1)
a2 = wykres2(dane2)
a3 = wykres2(dane3)
a4 = wykres2(dane4)
a5 = wykres2(dane5)


plt.figure()
figure = plt.subplot(1,2,1)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.sans-serif'] = ['Times New Roman', 'sans-serif']
plt.grid(color='k', linestyle='dotted',)

figure.plot(y5,z5, 'bo-', markevery=30 ,markeredgecolor='k')
figure.plot(y3,z3, 'gv-', markevery=30 ,markeredgecolor='k')
figure.plot(y1,z1, 'rD-', markevery=30 ,markeredgecolor='k')
figure.plot(y4,z4, 'ks-', markevery=30 ,markeredgecolor='k')
figure.plot(y2,z2, 'magenta', marker = 'd', markevery=30 ,markeredgecolor='k')

figure.legend(["1-Evol-RS", "1-Coev-RS", "2-Coev-RS", "1-Coev", "2-Coev"],loc="lower right", numpoints=2)
plt.xlabel('Rozegranych gier (x1000)')
plt.ylabel('Odsetek wygranych gier [%]')


plt.xlim(0,500)
plt.ylim(60,100)
figure1 = figure.twiny()
figure1.set_xlabel('Pokolenie')
figure1.set_xticks([0,40,80,120,160,200])
figure2 = plt.subplot(1,2,2)


figure2.boxplot([a5, a3, a1, a4, a2], notch = True, showmeans=True, labels = ["1-Evol-RS","1-Coev-RS", "2-Coev-RS", "1-Coev", "2-Coev"],
                  boxprops = dict(color="b"),meanprops=dict(marker='.', markerfacecolor='b', markeredgecolor='k'),
                whiskerprops = dict(color="b", linestyle = '--'), flierprops=dict( marker='+', markeredgecolor='b'),
                capprops = dict(color = "k"))
plt.grid(color='k', linestyle='dotted',)
plt.ylim(60,100)
figure2.yaxis.tick_right()

plt.xticks(rotation=20)


plt.savefig('wykresy.pdf')
plt.show()
plt.close()