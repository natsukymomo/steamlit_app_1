import streamlit 
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')
#----------section 1
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Soomthie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#----------section2
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set index with other attribute
my_fruit_list = my_fruit_list.set_index('Fruit')
#multiselect bar, header - option name - default option#
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
#loc -> select
fruits_to_show = my_fruit_list.loc[fruits_selected]
#list data
streamlit.dataframe(fruits_to_show)

#----------section3
streamlit.header('Fruitvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered', fruit_choice)
#request api
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())
#normalize data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


#-----------section4

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruits load list contains")
streamlit.dataframe(my_data_rows)

