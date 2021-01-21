import matplotlib.pyplot as plt
import numpy as np

C=17.38
change_Java	=11.96
Python=11.72
cplus=7.56
C_h=3.95
Visual_Basic=3.84
JavaScript=2.20
PHP=1.99
change_R=1.90
change_Groovy=1.84
height = [C,change_Java,Python,cplus,C_h,Visual_Basic,JavaScript,PHP,change_R,change_Groovy]
bars = ('C','Change Java','Python','C++','C#','Visual Basic','Javascript','PHP','Change R','change Groovy')
y_pos = np.arange(len(height))

plt.figure(figsize=(10,5))
plt.bar(y_pos, height, color = '#969696')
plt.xticks(y_pos, bars)
plt.title('Popularnosc top10 jezykow programowania', fontsize=16, color='#323232')
plt.show()
