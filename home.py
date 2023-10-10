import pandas as pd
import streamlit as st

from query import *

st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")
st.subheader("🔔 Análise Descritiva de Seguros")
st.markdown("##")


# fetch data
result = view_all_data()
df = pd.DataFrame(
    result,
    columns=[
        "Policy",
        "Expiry",
        "Location",
        "State",
        "Region",
        "Investment",
        "Construction",
        "BusinessType",
        "Earthquake",
        "Flood",
        "Rating",
    ],
)

# side bar
# logo
st.sidebar.image("resources/img/logo1.png",caption="Online Analytics")

# switcher
st.sidebar.header("Filtre os dados")
region=st.sidebar.multiselect(
    "Região",
     options=df["Region"].unique(),
     default=df["Region"].unique(),
)
location=st.sidebar.multiselect(
    "Localização",
     options=df["Location"].unique(),
     default=df["Location"].unique(),
)
construction=st.sidebar.multiselect(
    "Tipo de construção",
     options=df["Construction"].unique(),
     default=df["Construction"].unique(),
)

df_selection=df.query(
    "Region==@region & Location==@location & Construction ==@construction"
)

df_selection