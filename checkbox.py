
# coding: utf-8

# In[8]:


from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, Panel
from bokeh.models.widgets import CheckboxGroup, Tabs
from bokeh.layouts import column, row, WidgetBox


# In[2]:


import json
from pprint import pprint


# In[3]:


with open('country_info.json') as f:
    data = json.load(f)

pprint(data)


# In[4]:


country_names =[]

for key in data.keys():
    country_names.append(key)

country_names


# In[9]:


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

#Update the plot based on selections
def update(attr, old, new):
    countries_to_plot = [country_selection.labels[i] for i in country_selection.active]
    new_cds = get_cds(countries_to_plot)
    data_source_global.data.update(new_cds.data)
    return

#find the initially selected countries
'''
initial_countries = [country_selection.labels[i] for i in country_selection.active]
src = get_cds(initial_countries)
p = make_chart_cds(src)
'''
#CheckboxGroup to select countries to display
country_selection = CheckboxGroup(labels=country_names, active = [0,1])
country_selection.on_change('active',update)

data_source_global = get_cds(country_names[0])
plot_global        = make_chart_cds(data_source_global)


layout = row(country_selection, plot_global)
tab = Panel(child=layout, title='Country')
tabs = Tabs(tabs=[tab])

curdoc().add_root(tabs)

