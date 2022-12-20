import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import warnings
warnings.filterwarnings("ignore") 


def import_and_correct(path):
    dataframe = pd.read_csv(path)
    dataframe["lat"] = dataframe["lat"].str.replace(',', '.').astype(float)
    dataframe["lon"] = dataframe["lon"].str.replace(',', '.').astype(float)
    return dataframe

base_map_estacionamento = import_and_correct("base_map_estacionamento.csv")
base_map_comidas = import_and_correct("base_map_comidas.csv")


st.header("Mapa Fundão")
select_list_of_map = st.multiselect("Quais dados deseja visualizar?", ["Estacionamento", "Comidas"])

map_rio = folium.Map(location=[-22.8956799, -43.3929967], zoom_start=11)
if "Estacionamento" in select_list_of_map:
    for lat, lng, label in zip(base_map_estacionamento.lat, base_map_estacionamento.lon, base_map_estacionamento.name):
            popup = folium.Popup(label, parse_html=True)
            folium.Marker([lat, lng], 
                        popup=popup, 
                        icon=folium.Icon(color='black',icon_color='#FFFF00')).add_to(map_rio)
if "Comidas" in select_list_of_map:
    for lat, lng, label in zip(base_map_comidas.lat, base_map_comidas.lon, base_map_comidas.name):
            popup = folium.Popup(label, parse_html=True)
            folium.Marker([lat, lng], 
                        popup=popup, 
                        icon=folium.Icon(icon="asterisk", color='red',icon_color='#FFFF00')).add_to(map_rio)
    
st.map(st_folium(map_rio, width=700, height=450))