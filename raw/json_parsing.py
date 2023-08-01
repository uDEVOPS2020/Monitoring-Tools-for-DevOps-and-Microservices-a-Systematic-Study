import pandas as pd
import json
import os

filename = 'md_tools.json'

with open(filename, 'r', encoding="utf8") as f:
  data = json.load(f)


for item in data['items']:
   name = item['name']
   link = item['html_url']
   description = item['description']
   columns=['Name','Link','Description']
   values = [name,link,description]
   df = pd.DataFrame([values], columns=columns)
   if not os.path.isfile("md_tools.csv"):
      df.to_csv(filename, index=False, header=True)
   else:
      df.to_csv(filename, mode='a', index=False, header=False)