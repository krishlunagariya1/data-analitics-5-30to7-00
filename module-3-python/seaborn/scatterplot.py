# scatterplot is used to display or a data os two numerical variablees
# scatterplot in used to provide relationship between two numerical variables
# scatterplot is identifying pattens or corelations between two numerical variables

#create a graph to provide relationship between total bill and tip

import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",hue="day",data=tips)
#show scatterplot
plt.show()