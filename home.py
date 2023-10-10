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
df
