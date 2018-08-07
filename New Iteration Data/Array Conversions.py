
# coding: utf-8

# In[11]:


import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify


# In[12]:


merged_airports = pd.read_json('Top100Airports_Merged.json')
merged_airports


# In[54]:


#from json convert into DF
ranks_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    ranks_list = list(data["data"]["RANK"].values())
    

##print(ranks_list)
ranks_list = pd.DataFrame({"RANK":ranks_list})
ranks_list = ranks_list.reset_index()

#from DF convert into Array
ranks_list = ranks_list.values
ranks_list



# In[56]:


app = Flask(__name__)
@app.route("/ranks-list")
def ranks_lists():
    return jsonify(ranks_list)

if __name__ == "__main__":
    app.run(debug=False)

# In[105]:


Airport_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    Airport_list = list(data["data"]["Airport"].values())
    

##print(Airport_list)
Airport_list = pd.DataFrame({"Airport":Airport_list})
Airport_list = Airport_list.reset_index()

#from DF convert into Array
Airport_list = Airport_list.values
Airport_list


# In[106]:


REG_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    REG_list = list(data["data"]["REG"].values())
    

##print(REG_list)
REG_list = pd.DataFrame({"REG":REG_list})
REG_list = REG_list.reset_index()

#from DF convert into Array
REG_list = REG_list.values
REG_list


# In[107]:


carriers_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    carriers_list = list(data["data"]["carriers"].values())
    

##print(carriers_list)
carriers_list = pd.DataFrame({"carriers":carriers_list})
carriers_list = carriers_list.reset_index()

#from DF convert into Array
carriers_list = carriers_list.values
carriers_list


# In[108]:


city_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    city_list = list(data["data"]["city"].values())
    

##print(carriers_list)
city_list = pd.DataFrame({"city":city_list})
city_list = city_list.reset_index()

#from DF convert into Array
city_list = city_list.values
city_list


# In[109]:


country_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    country_list = list(data["data"]["country"].values())
    

##print(country_list)
country_list = pd.DataFrame({"country":country_list})
country_list = country_list.reset_index()

#from DF convert into Array
country_list = country_list.values
country_list



# In[110]:


direct_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    direct_list = list(data["data"]["direct_flights"].values())
    

##print(direct_list)
direct_list = pd.DataFrame({"direct_flights":direct_list})
direct_list = direct_list.reset_index()

#from DF convert into Array
direct_list = direct_list.values
direct_list



# In[133]:


lat_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    lat_list = list(data["data"]["lat"].values())
    

##print(lat_list)
lat_list = pd.DataFrame({"lat":lat_list})
#lat_list = lat_list.reset_index()

#from DF convert into Array
lat_list = lat_list.values
lat_list



# In[132]:


lon_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    lon_list = list(data["data"]["lon"].values())
    

##print(lon_list)
lon_list = pd.DataFrame({"lon":lon_list})
#lon_list = lon_list.reset_index()

#from DF convert into Array
lon_list = lon_list.values
lon_list


# In[145]:


coordinates = np.concatenate((lat_list, lon_list), axis=1)
coordinates = pd.DataFrame.from_dict(coordinates)
coordinates = coordinates.reset_index()
coordinates = coordinates.values
coordinates



# In[113]:


name_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    name_list = list(data["data"]["name"].values())
    

##print(name_list)
name_list = pd.DataFrame({"name":name_list})
name_list = name_list.reset_index()

#from DF convert into Array
name_list = name_list.values
name_list


# In[114]:


url_list = []

with open('Top100Airports_Merged.json') as json_file:
    data = json.load(json_file)
    url_list = list(data["data"]["url"].values())
    

##print(url_list)
url_list = pd.DataFrame({"url":url_list})
url_list = url_list.reset_index()

#from DF convert into Array
url_list = url_list.values
url_list


