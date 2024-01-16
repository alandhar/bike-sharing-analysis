import streamlit as st
import pandas as pd

hour = pd.read_csv('data\hour.csv')
day = pd.read_csv('data\day.csv')

st.title('Bike Sharing Dashboard')

# Sidebar is still not integrated with graphics
# Add a sidebar search bar to let user select date 
st.sidebar.title('Filter for line chart')
hour["dteday"] = pd.to_datetime(hour["dteday"])
default_start_date = hour['dteday'].iloc[0]
default_end_date = hour['dteday'].iloc[-1]
st.sidebar.date_input('Start date', default_start_date.date())
st.sidebar.date_input('End date', default_end_date.date())

# Add a sidebar distributions based on numeric variables
st.sidebar.title("Distributions")
column_labels = {'hr':'Hour','temp':'Temperature', 'hum':'Humidity', 'windspeed':'Wind Speed'}
selected_columns = st.sidebar.multiselect('Select Columns', list(column_labels.keys()), format_func=lambda col: column_labels[col])

# information weather
st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


# Add metrics at top dashboard
formatted_total_cnt = '{:.1f} million'.format(day['cnt'].sum() / 1e6)
formatted_casual_cnt = '{:.1f} million'.format(day['casual'].sum() / 1e6)
formatted_registered_cnt = '{:.1f} million'.format(day['registered'].sum() / 1e6)
col1, col2, col3 = st.columns(3)
col1.metric("Total", formatted_total_cnt)
col2.metric("Casual", formatted_casual_cnt)
col3.metric("Registered", formatted_registered_cnt)

# Line chart dteday vs cnt
st.header('Line chart')
st.line_chart(day, x='dteday', y='cnt')
# Add new features season comparison
...

# Barchart weathersit & season (optional)
st.subheader('Weather Situation-wise Bike Share Count')
st.bar_chart(day, x='weathersit', y='cnt')

# Distribution chart using scatterplot
st.header('Distribution')
st.subheader('Temperature vs. Bike Share Count')
st.scatter_chart(day, x='temp', y='cnt')

st.subheader('Humidity vs. Bike Share Count')
st.scatter_chart(day, x='hum', y='cnt')

st.subheader('Wind Speed vs. Bike Share Count')
st.scatter_chart(day, x='windspeed', y='cnt')