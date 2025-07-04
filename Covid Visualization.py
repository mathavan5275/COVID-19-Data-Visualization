#!/usr/bin/env python
# coding: utf-8

# # Covid Visualization using Plotly

# #### Importing Covid Data

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.offline as py

covd=pd.read_csv('Covid.csv')
covd.head()


# #### This chart shows the total COVID-19 deaths for the top 10 countries.

# In[3]:


cvd1=px.line(covd.head(10),x='Country/Region',y='TotalDeaths')
cvd1.show()


# #### This code shows a bar chart of the top 10 countries with the highest total COVID-19 cases

# In[72]:


cvd=px.bar(covd.head(10),x='TotalCases',y='Country/Region',color='TotalCases',hover_data=['Country/Region','iso_alpha'])
cvd.show()


# #### This chart shows the top 10 countries with the highest total COVID-19 cases

# In[5]:


cvd1=px.bar(covd.head(10),x='Country/Region',y='TotalCases',color='TotalCases',hover_data=['Country/Region','iso_alpha'])
cvd1.show()


# #### This chart shows the distribution of total COVID-19 tests across different continents for the top 10 records.

# In[7]:


cvd2=px.box(covd.head(10),x='Country/Region',y='TotalCases')
cvd2.show()


# #### This chart shows total COVID-19 cases for the top 30 countries, with point size and color representing case numbers and additional details on total deaths available on hover.

# In[9]:


cvd4=px.scatter(covd.head(30),x='Country/Region',y='TotalCases',color='TotalCases',size='TotalCases',size_max=50,hover_data=['TotalDeaths'])
cvd4.show()


# #### This chart visualizes total COVID-19 cases across continents for the top 20 records, with point size and color reflecting case numbers and additional details on total deaths shown on hover.

# In[11]:


cvd4=px.scatter(covd.head(30),x='Continent',y='TotalCases',color='TotalCases',size='TotalCases',size_max=70,hover_data=['Country/Region'])
cvd4.show()


# #### This chart displays active COVID-19 cases for the top 20 countries, with color indicating the number of active cases and additional information on total cases available on hover.

# In[13]:


cvd5=px.scatter(covd.head(20),x='Country/Region',y='ActiveCases',color='ActiveCases',hover_data=['TotalCases'])
cvd5.show()


# #### This chart shows COVID-19 tests per million people for the top 20 countries, with point size and color representing testing rates and total cases details shown on hover.

# In[93]:


cvd5=px.scatter(covd.head(20),x='Country/Region',y='Tests/1M pop',color='Tests/1M pop',size='Tests/1M pop',size_max=50,hover_data=['TotalCases'])
cvd5.show()


# #### This chart displays the total number of COVID-19 recoveries for the top 30 countries, with colors representing recovery counts and additional total cases information available on hover.

# In[102]:


cvd6=px.scatter(covd.head(30),x='Country/Region',y='TotalRecovered',color='TotalRecovered',size_max=50,hover_data=['TotalCases'])
cvd6.show()


# #### This chart displays total COVID-19 cases per million people for the top 30 countries, with point size and color indicating case rates and total cases details shown on hover.

# In[121]:


cvd5=px.scatter(covd.head(30),x='Country/Region',y='Tot Cases/1M pop',color='Tot Cases/1M pop',size='Tot Cases/1M pop',size_max=50,hover_data=['TotalCases'])
cvd5.show()


# #### This chart compares total COVID-19 deaths and total cases for the top 30 countries, using logarithmic scales on both axes, with point size and color representing death counts and hover details showing country and continent information.

# In[160]:


cvd5=px.scatter(covd.head(30),x='TotalCases',y='TotalDeaths',color='TotalDeaths',size='TotalDeaths',size_max=80,hover_data=['Country/Region'],log_x=True,log_y=True)
cvd5.show()


# #### This chart shows total COVID-19 recoveries compared to total cases for the top 30 countries, using a logarithmic scale for recoveries and displaying country details on hover.

# In[134]:


cvd5=px.scatter(covd.head(30),x='TotalCases',y='TotalRecovered',color='TotalRecovered',size_max=50,log_y=True,hover_data=['Country/Region'])
cvd5.show()


# #### This chart visualizes the relationship between total COVID-19 tests and total cases for the top 30 countries, using logarithmic scales on both axes. Point size and color reflect the number of tests, with country details shown on hover.

# In[173]:


cvd5=px.scatter(covd.head(30),x='TotalTests',y='TotalCases',color='TotalTests',size='TotalTests',size_max=80,hover_data=['Country/Region'],log_x=True,log_y=True)
cvd5.show()


# ## Covid grouped Dataset

# In[178]:


covd2=pd.read_csv('Covid_Grouped.csv')
covd2


# In[ ]:





# In[196]:


cvdgrp1=px.bar(covd2,x='Date',y='Deaths',color='Deaths',hover_data=['Country/Region','WHO Region'])
cvdgrp1.show()


# In[ ]:





# In[198]:


cvdgrp1=px.bar(covd2,x='Date',y='Confirmed',color='Confirmed',hover_data=['Country/Region','WHO Region'])
cvdgrp1.show()


# In[ ]:





# In[200]:


cvdgrp1=px.bar(covd2,x='Date',y='Recovered',color='Recovered',hover_data=['Country/Region','WHO Region'])
cvdgrp1.show()


# In[ ]:





# In[202]:


cvdgrp1=px.bar(covd2,x='Date',y='Active',color='Active',hover_data=['Country/Region','WHO Region'])
cvdgrp1.show()


# In[ ]:





# In[204]:


cvdgrp1=px.bar(covd2,x='Date',y='New cases',color='New cases',hover_data=['Country/Region','WHO Region'])
cvdgrp1.show()


# In[ ]:





# In[214]:


cvdline1=px.line(covd2,x='Date',y='Deaths',height=400,hover_data=['Country/Region','WHO Region'])
cvdline1.show()


# In[ ]:





# In[216]:


cvdline2=px.line(covd2,x='Date',y='Recovered',height=400,hover_data=['Country/Region','WHO Region'])
cvdline2.show()


# In[ ]:





# In[218]:


cvdline3=px.line(covd2,x='Date',y='Active',height=400,hover_data=['Country/Region','WHO Region'])
cvdline3.show()


# In[ ]:





# In[222]:


cvdline4=px.line(covd2,x='Date',y='New cases',height=400,hover_data=['Country/Region','WHO Region'])
cvdline4.show()


# In[ ]:





# In[232]:


cvdsct1=px.scatter(covd2,x='Confirmed',y='Deaths',color='Deaths',size='Deaths',size_max=80,hover_data=['Country/Region'],log_x=True,log_y=True)
cvdsct1.show()


# In[236]:


cvdsct1=px.scatter(covd2,x='Confirmed',y='Recovered',color='Recovered',size='Recovered',size_max=80,hover_data=['Country/Region'],log_x=True,log_y=True)
cvdsct1.show()


# In[ ]:




