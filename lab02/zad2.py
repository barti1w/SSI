import pandas as pd
import matplotlib.pyplot as plt

file_data = 'iris.txt'
data = pd.read_csv(file_data, sep='\t', header=None)

df1 = data.loc[data[4] == 1]
df2 = data.loc[data[4] == 2]
df3 = data.loc[data[4] == 3]

fig, axs = plt.subplots(2, 2, figsize=(10,10))

axs[0,0].scatter(df1[2], df1[3])
axs[0,0].scatter(df2[2], df2[3])
axs[0,0].scatter(df3[2], df3[3])
axs[0,0].set(xlabel="petal_length_in_cm", ylabel="petal_width_in_cm")

axs[0,1].scatter(df1[1], df1[3])
axs[0,1].scatter(df2[1], df2[3])
axs[0,1].scatter(df3[1], df3[3])
axs[0,1].set(xlabel="sepal_width_in_cm", ylabel="petal_width_in_cm")

axs[1,0].scatter(df1[0], df1[3])
axs[1,0].scatter(df2[0], df2[3])
axs[1,0].scatter(df3[0], df3[3])
axs[1,0].set(xlabel="sepal_length_in_cm", ylabel="petal_width_in_cm")

axs[1,1].scatter(df1[1], df1[2])
axs[1,1].scatter(df2[1], df2[2])
axs[1,1].scatter(df3[1], df3[2])
axs[1,1].set(xlabel="sepal_width_in_cm", ylabel="petal_length_in_cm")



plt.show()