import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
datax= np.random.random(5000) * 100
datay= np.random.random(5000) * 100
plt.scatter(datax,datay, c ='black', marker = '^', s = 50, alpha = 0.1)
plt.show()
years = [2005 + x for x in range (20)]
weight = [6,15,24,29,35,42,49,50,56,59,64,70,76,80,84,81,79,80,78,84]
plt.plot(years,weight, c='red', lw = 1, linestyle = '--')
plt.show()
club = ['city', 'united', 'chelsea', 'spurs', 'liverpool','arsenal']
count = [160,200,90,56,140,150]
plt.bar(club,count, color = 'red', width = 0.1)
plt.show()
x = np.random.normal(50,20,1000)
plt.hist(x, cumulative=True)
plt.show()
food = ['pizza', 'burgers', 'tacos', 'waffles', 'pancakes', 'noodles']
count = [45,35,32,29,30,32]
explodes = [0.1,0.2,0.3,0.2,0.1,0]
plt.pie(count, labels= food, explode = explodes, autopct='%.2f%%')
style.use('dark_background')
plt.show()   # plt.title , plt.xlabel, plt.ylabel. label = company1 then plt.legend(loc = 'lower right')
height = np.random.normal(170,9,100)
plt.boxplot(height)
plt.show()

x1,y1 = np.random.random(100), np.random.random(100)
x2,y2 = np.arange(100), np.random.random(100)
plt.figure(1)
plt.scatter(x1,y1)
plt.figure(2)
plt.plot(x2,y2)
plt.show()
x = np.arange(100)
fig,axs = plt.subplots(2,2)
axs[0,0].plot(x,np.sin(x))
axs[0,1].plot(x,np.cos(x))
axs[1,0].plot(x,np.log10(x))
axs[1,1].plot(x,np.tan(x))
axs[0,0].set_title('sine wave')
axs[0,1].set_title('cos wave')
axs[1,0].set_title('log function')
axs[1,1].set_title('tan wave')
fig.suptitle('four plots')
plt.savefig('four plots.png', dpi=300)
plt.show()

#-----3D projections----#
a = plt.axes(projection ='3d')
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)
a.scatter(x,y,z)
plt.show()
a = plt.axes(projection ='3d')
x = np.arange(0,50,0.01)
y = np.sin(x)
z = np.cos(x)
a.plot(x,y,z)
plt.show()
a = plt.axes(projection ='3d')
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
X,Y = np.meshgrid(x,y)
Z = np.sin(X)*np.cos(Y)
a.plot_surface(X,Y,Z, cmap ='Spectral')
a.set_title('Surface plot')
plt.show()
heads_tails = [0,0]
for _ in range(100000):
    heads_tails[random.randint(0,1)] +=1
    plt.bar(['heads','tails'], heads_tails, color=['red','blue'])
    plt.pause(0.0001)
plt.show()