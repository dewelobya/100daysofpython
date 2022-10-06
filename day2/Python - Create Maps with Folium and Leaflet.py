#!/usr/bin/env python
# coding: utf-8

# In[42]:


import folium 

m = folium.Map(location=[51.503323, -0.119543], tiles = "stamen toner", zoom_start=15)
m


# In[46]:


folium.Marker(location=[51.497990, -0.176880], popup="<strong>IC</strong>", tooltip="Click for more information").add_to(m)
m


# In[47]:


folium.Marker(location=[51.500149, -0.126240],  tooltip ="Click for more", popup="<strong>UCL</strong>", icon= folium.Icon(icon='envelope')).add_to(m)
m


# In[45]:


folium.Marker(location=[51.753738, -1.263460],  tooltip ="Click for more", popup="<strong>Oxford</strong>", icon= folium.Icon(icon='cloud', color='purple')).add_to(m)
m


# In[44]:


folium.Marker(location=[52.202541, 0.131240],  tooltip ="Click for more", popup="<strong>Cambridge</strong>", icon= folium.Icon(icon='cloud', color='red')).add_to(m)
m


# In[48]:


locationPotter = [53.480709,-2.234380]
iconPotter = folium.features.CustomIcon('./downloads/potter.png', icon_size=(100,100))
popupPotter = "<strong>Harry Potter</strong><br>Realname: Harry Potter <br>City of birth: Godric's Hollow, West Country, England, Great Britain"
folium.Marker(location=locationPotter, tooltip="Harry Potter", popup=popupPotter, icon=iconPotter).add_to(m)
m


# In[53]:


locationSanta = [66.503944, 25.729391]
iconSanta = folium.features.CustomIcon('./downloads/santa.png', icon_size=(100,100))
popupSanta = "<strong>Santa Claus</strong><br>Realname: Santa Claus <br>City of birth: Rovaniemi, The Santa Clause's Village, Finland"
folium.Marker(location=locationSanta, tooltip="Santa Claus", popup=popupSanta, icon=iconSanta).add_to(m)
m


# In[54]:


locationEiffel = [48.856613, 2.352222]
iconEiffel = folium.features.CustomIcon('./downloads/eiffel.png', icon_size=(100,100))
popupEiffel = "<strong>Eiffel</strong><br>Realname: Eiffel <br>City of birth: Paris, France"
folium.Marker(location=locationEiffel, tooltip="Eiffel", popup=popupEiffel, icon=iconEiffel).add_to(m)
m


# In[ ]:




