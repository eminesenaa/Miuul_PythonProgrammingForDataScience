import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# Matplotlib is a popular and powerful Python library for creating static, animated, 
# and interactive visualizations in data analysis and scientific computing. 
# however this is low level compared to seaborn


pd.set_option('display.max_columns' , None)
pd.set_option('display.width' , 600)
df = sns.load_dataset("titanic")
df.head()


# plot

x = np.array([1, 8 ])
y = np.array([0, 150])


plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()


x = np.array([2 , 4 , 6 , 8 , 10])
y = np.array([-3,-7,-9,-11,-13])
plt.plot(x, y)
plt.show()


# ? marker

y = np.array([13 , 28, 11, 100])

plt.plot(y, marker = '*') # o * . , x X + P s D d p H h
plt.show()


# ? line

# b	solid
# g	dotted
# r	dashed
# c	dashdot
# m	
# k	
# w	
# y	
# l	

y = np.array([13 , 28, 11, 100])
plt.plot(y,'c--',marker='*' , linestyle = "dotted")   
plt.show()



# ? multiple lines

x = np.array([23,18,31,10])
y = np.array([13,28,11,100])
plt.plot(x)
plt.plot(y,"r-.")   ## color and style of the second plot
plt.show()


# ? labels

x = np.array([112, 134, 103, 161, 182, 67, 151, 194, 120, 173])
y = np.array([50, 55, 65, 71, 80, 85, 92, 96, 98, 100])
plt.plot(x , y)

plt.title("Main Title")
plt.xlabel('X axis label')
plt.ylabel('Y Axis Label')
plt.legend(['Line One','line Two'])     # legend is used to give a name for each curve in graph
plt.grid (True )                     #### grid function is used to add grids on graphs
plt.text(100,100 ,'Text at an arbitary position' , fontsize=10)      # text function
plt.show()
plt.savefig('filename.png')       # savefig function saves image as png file
plt.close()                       # close function closes all plots


# ? subplots

# plot 1

x = np.array([112, 134, 103, 161, 182, 67, 151, 194, 120, 173])
y = np.array([50, 55, 65, 71, 80, 85, 92, 96, 98, 100])
plt.subplot(1,3 , 1) # 1 row, 3 columns, first graph
plt.title("1")
plt.plot(x , y )

x = np.array([112, 114, 173, 102, 145, 120, 115, 142, 177, 151])
y = np.array([198, 133, 111, 193, 178, 100, 139, 153, 119, 199])
plt.subplot(1, 3 , 2) # 1 row, 3 columns, second graph
plt.title("2")
plt.plot(x , y )

x = np.array([160, 116, 157, 127, 103, 195, 107, 112, 133, 137])
y = np.array([50, 55, 65, 71, 80, 85, 92, 96, 98, 100])
plt.subplot(1, 3 , 3) # 1 row, 3 columns, third graph
plt.title("3")
plt.plot(x , y )


plt.show()