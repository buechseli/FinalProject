
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, Panel


# In[2]:


import json
from pprint import pprint


# In[3]:


with open('country_info.json') as f:
    data = json.load(f)

pprint(data)


# In[4]:


x_coord = []
y_coord_arrival = []
y_coord_departure = []
y_expend_in = []
y_expend_out = []
for y in data['ALBANIA']:
    x_coord.append(y['date'])
    y_coord_arrival.append(y['arrivals_total'])
    y_coord_departure.append(y['departures_total'])
    y_expend_in.append(y['expenditure_in_country'])
    y_expend_out.append(y['expenditure_out_country'])    

print(x_coord)
print(y_coord_arrival)
print(y_coord_departure)
print(y_expend_in)
print(y_expend_out)


# In[5]:


country_names =[]

for key in data.keys():
    country_names.append(key)

country_names


# In[6]:


from bokeh.plotting import figure, output_file,show
from bokeh.models.widgets import Select, Tabs
from bokeh.io import show, curdoc
from bokeh.layouts import column, row, WidgetBox


# In[7]:




#Function to make the plot
def make_chart_cds(country_cds):
    plot = figure(title="Arrivals & Departures ('000s)")
    plot.line(x='years', 
              y='arrivals',
              source=country_cds, 
              line_color='green', 
              line_width=2)
    plot.line(x='years', 
              y='departures',
              source=country_cds, 
              line_color='red', 
              line_width=2)
    plot.yaxis.axis_label = "Tourists ('000s)"
    plot.xaxis.axis_label = "Year"
    return plot 

def get_cds(country_name):
    years = []
    arrivals = []
    departures = []
    expenditure_in = []
    expenditure_out = []
    for entry in data[country_name]:
        years.append(entry['date'])
        arrivals.append(entry['arrivals_total'])
        departures.append(entry['departures_total'])
        expenditure_in.append(entry['expenditure_in_country'])
        expenditure_out.append(entry['expenditure_out_country'])
    return ColumnDataSource({'years'            : years, 
                             'arrivals'         : arrivals, 
                             'departures'       : departures, 
                             'expenditures_in'  : expenditure_in, 
                             'expenditures_out' : expenditure_out})

def select_country_handler(attr, old, new):
    new_cds = get_cds(new)
    data_source_global.data.update(new_cds.data)
    return


data_source_global = get_cds(country_names[0])
plot_global        = make_chart_cds(data_source_global)

select_country = Select(title="Country:", 
                        value=country_names[0],
                        options=country_names)
select_country.on_change("value", select_country_handler)
layout = row(select_country, plot_global)
tab = Panel(child=layout, title='Country')
tabs = Tabs(tabs=[tab])

curdoc().add_root(tabs)

