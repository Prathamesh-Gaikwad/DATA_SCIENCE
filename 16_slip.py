import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
            'Name' : ['sharade', 'Paru', 'Teeka', 'Tillu'],
            'CGPA' : [8.4, 8.7, 9.7, 8.9],
            'Age' : [61, 24, 45, 39]
        }
data1 = pd.DataFrame(data)

print("Average Age Of Student : ", data1['Age'].mean())
print("Average CGPA Of Student : ", data1['CGPA'].mean())

plt.pie(data['CGPA'], labels = data['Name'], autopct = "%1.1f%%", shadow = True)
plt.title("[PIE-CHART-NAME-VS-CGPA]")
plt.show()
