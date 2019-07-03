import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
y_pos = np.arange(len(letter))
performance = [12898, 4861, 4299, 2743, 3492, 4130, 1770, 3106, 8691, 344, 465, 2689, 4819, 2063, 9720, 3880, 173, 2505, 7411, 18600, 1110, 936, 5886, 32, 479, 55]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, letter)
plt.ylabel('appearance')
plt.title('First Letter Frequency')

plt.show()