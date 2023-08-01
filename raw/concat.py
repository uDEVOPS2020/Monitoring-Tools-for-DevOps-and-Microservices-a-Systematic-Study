import pandas as pd
import os

amd_c = pd.read_csv('amd_crazycanux.csv')
amd_s = pd.read_csv('amd_SquadcastHub.csv')
tmd = pd.read_csv('tmd_tools.csv')
tmm =  pd.read_csv('tmm_tools.csv')

df = (pd.concat([amd_c,amd_s,tmd,tmm], ignore_index=True, sort =False)
        .drop_duplicates(['Name'], keep='last'))

if not os.path.isfile("all_tools.csv"):
   df.to_csv("all_tools.csv", index=False, header=True)
else:
   df.to_csv("all_tools.csv", mode='a', index=False, header=False)
