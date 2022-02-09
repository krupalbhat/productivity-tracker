from re import X
import pandas as pd
import matplotlib.pyplot as plt
import os
rootdirectory = os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")   
 
if not os.path.isdir(os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")):
    os.mkdir(os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker"))   

df = pd.read_csv(os.path.join(rootdirectory,'productivity.csv'))
print(df)
sumcolumn = (df["timeout"] - df["timein"])/60
df["difference"] = sumcolumn



figure, axes = plt.subplots(1, 2)

df.plot(ax=axes[0],y = "difference",kind = "bar")

df.plot(ax=axes[1],y = "difference")
# df.plot(y = "difference",kind = 'bar')

# df.plot(y = "difference")

plt.show() 
