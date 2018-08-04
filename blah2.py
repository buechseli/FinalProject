
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
from bokeh.layouts import column, row, WidgetBox, gridplot


# In[7]:


#grabbing lists from "CSV_analysis.ipynb" 
arrivals_list = ['FRANCE',
 'UNITED STATES OF AMERICA',
 'SPAIN',
 'CHINA',
 'ITALY',
 'HONG KONG, CHINA',
 'RUSSIAN FEDERATION',
 'UNITED KINGDOM',
 'GERMANY',
 'MEXICO',
 'TURKEY',
 'AUSTRIA',
 'CANADA',
 'MALAYSIA',
 'POLAND']


# In[8]:


#grabbing lists from "CSV_analysis.ipynb" 
departures_list = ['HONG KONG, CHINA',
 'UNITED STATES OF AMERICA',
 'GERMANY',
 'UNITED KINGDOM',
 'POLAND',
 'CHINA',
 'RUSSIAN FEDERATION',
 'ITALY',
 'CANADA',
 'FRANCE',
 'HUNGARY',
 'JAPAN',
 'NETHERLANDS',
 'UKRAINE',
 'MALAYSIA']


# In[9]:


#grabbing lists from "CSV_analysis.ipynb" 
expenditure_in_list = ['UNITED STATES OF AMERICA',
 'FRANCE',
 'GERMANY',
 'UNITED KINGDOM',
 'ITALY',
 'AUSTRALIA',
 'THAILAND',
 'SPAIN',
 'HONG KONG, CHINA',
 'MACAO, CHINA',
 'CANADA',
 'TURKEY',
 'SWITZERLAND',
 'GREECE',
 'MEXICO']


# In[10]:


#grabbing lists from "CSV_analysis.ipynb" 
expenditure_out_list =['UNITED STATES OF AMERICA',
 'GERMANY',
 'UNITED KINGDOM',
 'JAPAN',
 'FRANCE',
 'CANADA',
 'RUSSIAN FEDERATION',
 'AUSTRALIA',
 'KOREA, REPUBLIC OF',
 'ITALY',
 'SWITZERLAND',
 'BRAZIL',
 'NORWAY',
 'BELGIUM',
 'SAUDI ARABIA']


# In[11]:


colors = ['pink',
          'palevioletred',
          'indigo',
          'darkslateblue',
          'lightblue',
          'darkseagreen',
          'indianred',
          'gold',
          'firebrick',
          'saddlebrown',
          'slategrey',
          'aquamarine',
          'darkorange',
          'olive',
          'cadetblue']


# In[29]:


#Function to make the plot
def make_chart_cds(country_cds):
    plot = figure(title="Arrivals & Departures ('000s)")
    plot.line(x='years', 
              y='arrivals',
              source=country_cds, 
              line_color='green', 
              line_width=2,
              muted_color = 'green',
              muted_alpha = 0.2,
              legend = 'Arrivals')
    plot.line(x='years', 
              y='departures',
              source=country_cds, 
              line_color='red', 
              line_width=2,
              muted_color = 'red',
              muted_alpha = 0.2,
              legend = 'Departures')
    plot.legend.location = 'top_left'
    plot.legend.click_policy = 'mute'
    plot.yaxis.axis_label = "Tourists ('000s)"
    plot.xaxis.axis_label = "Year"
    return plot 

def make_chart_exp_cds(country_cds):
    plot2 = figure(title="Inbound & Outbound Spend ($M - USD)")
    plot2.line(x='years', 
              y='expenditures_in',
              source=country_cds, 
              line_color='green', 
              line_width=2,
              muted_color = 'green',
              muted_alpha = 0.2,
              legend = 'Inbound Spend')
    plot2.line(x='years', 
              y='expenditures_out',
              source=country_cds, 
              line_color='red', 
              line_width=2,
              muted_color = 'red',
              muted_alpha = 0.2,
              legend = 'Outbound Spend')
    plot2.legend.location = 'top_left'
    plot2.legend.click_policy = 'mute'
    plot2.yaxis.axis_label = "Tourism Spend ($M - USD)"
    plot2.xaxis.axis_label = "Year"
    return plot2 

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

def make_arrival_chart_cds(arrivals_list):
    plot = figure(title="Top 15 Countries by Total Arrivals ('000s)")
    for i in range(len(arrivals_list)):
        country_cds = get_cds(arrivals_list[i])
        plot.line(x='years', 
                  y='arrivals',
                  source=country_cds, 
                  line_color=colors[i], 
                  line_width=2,
                  muted_color = colors[i],
                  muted_alpha = 0.2,
                  legend = arrivals_list[i])
    plot.legend.location = 'top_left'
    plot.legend.click_policy = 'mute'
    plot.yaxis.axis_label = "Tourists ('000s)"
    plot.xaxis.axis_label = "Year"
    return plot 

def make_departure_chart_cds(departures_list):
    plot = figure(title="Top 15 Countries by Total Departures ('000s)")
    for i in range(len(departures_list)):
        country_cds = get_cds(departures_list[i])
        plot.line(x='years', 
                  y='departures',
                  source=country_cds, 
                  line_color=colors[i], 
                  line_width=2,
                  muted_color = colors[i],
                  muted_alpha = 0.2,
                  legend = departures_list[i])
    plot.legend.location = 'top_left'
    plot.legend.click_policy = 'mute'
    plot.yaxis.axis_label = "Tourists ('000s)"
    plot.xaxis.axis_label = "Year"
    return plot 

def make_expenditure_in_chart_cds(expenditure_in_list):
    plot = figure(title="Top 15 Countries by Tourism Expenditure In Country - US$ M")
    for i in range(len(expenditure_in_list)):
        country_cds = get_cds(expenditure_in_list[i])
        plot.line(x='years', 
                  y='expenditures_in',
                  source=country_cds, 
                  line_color=colors[i], 
                  line_width=2,
                  muted_color = colors[i],
                  muted_alpha = 0.2,
                  legend = expenditure_in_list[i])
    plot.legend.location = 'top_left'
    plot.legend.click_policy = 'mute'
    plot.yaxis.axis_label = "US$ - M"
    plot.xaxis.axis_label = "Year"
    return plot

def make_expenditure_out_chart_cds(expenditure_out_list):
    plot = figure(title="Top 15 Countries by Tourism Expenditure In Other Country - US$ M")
    for i in range(len(expenditure_out_list)):
        country_cds = get_cds(expenditure_out_list[i])
        plot.line(x='years', 
                  y='expenditures_out',
                  source=country_cds, 
                  line_color=colors[i], 
                  line_width=2,
                  muted_color = colors[i],
                  muted_alpha = 0.2,
                  legend = expenditure_out_list[i])
    plot.legend.location = 'top_left'
    plot.legend.click_policy = 'mute'
    plot.yaxis.axis_label = "US$ - M"
    plot.xaxis.axis_label = "Year"
    return plot 

data_source_global = get_cds(country_names[0])
plot_global        = make_chart_cds(data_source_global)
plot_global_2      = make_chart_exp_cds(data_source_global)
plot_15_arrival    = make_arrival_chart_cds(arrivals_list)
plot_15_departure  = make_departure_chart_cds(departures_list)
plot_15_expend_in  = make_expenditure_in_chart_cds(expenditure_in_list)
plot_15_expend_out = make_expenditure_out_chart_cds(expenditure_out_list)

select_country = Select(title="Country:", 
                        value=country_names[0],
                        options=country_names)

select_country.on_change("value", select_country_handler)
layout = gridplot([select_country], [plot_global, plot_global_2],
                  [plot_15_arrival, None], [plot_15_departure, None],
                  [plot_15_expend_in, None],[plot_15_expend_out, None])

tab = Panel(child=layout, title='Country')
tabs = Tabs(tabs=[tab])

curdoc().add_root(tabs)

