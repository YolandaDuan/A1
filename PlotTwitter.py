import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig, ax = plt.subplots()

bar_x = [0,1,2,3,4,5,6]
pronouns = ('den', 'denna', 'denne', 'det', 'han', 'hen', 'hon' )
y_pos = np.arange(len(pronouns))
bar_height = np.array([559, 4, 3, 180, 213, 44, 136])
bar_label = [559, 4, 3, 180, 213, 44, 136]
width = 0.8

colors = cm.hsv(bar_height / max(bar_height))

rects1 = ax.bar(bar_x, bar_label, width, color=colors)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.xticks(y_pos, pronouns)
plt.ylabel('appearance')
plt.title('Twitter Analysis')

plt.show()