import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("autos1.csv")
df['dateCreated'] = 0
df['dateCrawled']=0
df['lastSeen']=0
print(df['price'].corr(df['yearOfRegistration']))
contigency= pd.crosstab(df['price'], df['yearOfRegistration'])
print(contigency)
plt.figure(figsize=(12,8))
sns.heatmap(contigency, annot=True, cmap="YlGnBu")
plt.show()