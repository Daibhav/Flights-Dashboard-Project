import streamlit as st
from flights import DB # we imported the class 'DB' created in the 'flights.py'
import plotly.graph_objects as go
import plotly.express as px 

db = DB() # we made an object 'db' of that class 'DB'

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
    col1, col2 = st.columns(2)


    c = db.fetch_city_names() # c is the list 'city'
    with col1:
        source = st.selectbox('Source',sorted(c))
    with col2:
        destination = st.selectbox('Destination',sorted(c))    
    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)   

elif user_option == 'Analytics':

    # plotting the pie chart for flights and their frequencies
    airline,frequency = db.fetch_flights_frequency()
    # code of plotly pie chart from GPT
    labels = airline
    values = frequency
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    st.header('Pie Chart')
    st.plotly_chart(fig)


    # plotting a bar chart for the busy airports, all in all determinig the busiest airport
    # we took the code for this bar chart from the documentation of streamlit
    city,frequency1 = db.busy_airport()
    fig = px.bar(
        x = city,
        y = frequency1
    )

    st.plotly_chart(fig,theme = 'streamlit',use_container_width = True)


    # plotting the line chart for daily flights
    date,frequency2 = db.daily_frequency()
    fig = px.line(
        x = date,
        y = frequency2
    )

    st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)


else:
    st.title('We will tell about our project here')   
