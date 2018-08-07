
# coding: utf-8

# In[5]:


import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify


# In[2]:


merged_airports = pd.read_json('Top100Airports_Merged.json')
merged_airports


# In[29]:


#from json convert into DF
ranks_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    ranks_list = list(data["data"]["RANK"].values())
    

##print(ranks_list)
pd.Series(ranks_list).to_json(orient='values')
ranks_list = pd.DataFrame({"RANK":ranks_list})
ranks_list = ranks_list.reset_index()

#from DF convert into Array
ranks_list = ranks_list.values


# In[36]:


app = Flask(__name__)

@app.route('/')
def get_ranks_list():
    return jsonify(ranks_list)


if __name__ == "__main__":
    app.run(debug=True)