from cProfile import label
from re import X
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
import os
productivity_folder = os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")   
productivity_file= os.path.join(productivity_folder,"productivity.csv")
 
if not os.path.isdir(productivity_folder):
    os.mkdir(productivity_folder)   

df = pd.read_csv(productivity_file)
print(df)
sumcolumn = (df["timeout"] - df["timein"])/60
df["difference"] = sumcolumn
sum = df["difference"].sum()
print(round(sum))

#figure, axes = plt.subplots(1, 2)

df.plot(y = "difference",label = " Time in minutes",title = f"You Utilized {round(sum)} minutes productively today",kind = "bar")

plt.show() 
