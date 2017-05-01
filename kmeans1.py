import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from matplotlib import style
style.use("ggplot")
#######################################################
def joinarrays(a,b):
	newlist = np.concatenate((a,b), axis = 0)
	return newlist
#######################################################
def genran(N):
	a = np.random.normal(0.0,1,N)
	return a 
#######################################################
N = 500  #Size of data points here

#1st set of Data
x = genran(N)
y = 0.5*genran(N)

#2nd set of Data
x2 = genran(N)
y2 = genran(N) -1.5

xdata = joinarrays(x,x2)
ydata = joinarrays(y,y2)

plotdata = np.column_stack((xdata,ydata))

#Kmeans algorithm looks for k clustering means
#First pick 2 initial spots for the mean
#It then separates into 2 groups
#Then it finds the Center of Mass of the group of points and places a new mean there
#Repeats
kmeans = KMeans(n_clusters = 2)
kmeans.fit(plotdata)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["b.", "g."] #make sure number of colors matches n_clusters value

for x in range(len(plotdata)):
	plt.plot(plotdata[x][0], plotdata[x][1], colors[labels[x]], markersize = 10)

plt.scatter(centroids[:,0], centroids[:,1], marker = "x", s = 150, linewidths = 15, zorder = 10)

plt.show()
############################################################