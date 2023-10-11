import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *
from time import sleep

st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")
st.subheader("🔔 Análise Descritiva com Python e Streamlit")
st.markdown("##")

theme_plotly = None

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

# filtros
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

def Home():
    with st.expander("Tabela"):
        showData=st.multiselect('Filtros: ',df_selection.columns,default=[])
        st.write(df_selection[showData])

    investimento_total = float(df_selection['Investment'].sum())
    investimento_moda = float(df_selection['Investment'].mode())
    # investimento_moda = int(df_selection['Investment'].mode())
    # investimento_moda = int(df_selection['Investment'].mode().iloc[0])

    investimento_media = float(df_selection['Investment'].mean())
    investimento_mediana = float(df_selection['Investment'].median())
    risco_medio = float(df_selection['Rating'].mean())


    print('investimento_total',investimento_total)
    print('investimento_moda',investimento_moda)
    print('investimento_media',investimento_media)
    print('investimento_mediana',investimento_mediana)
    print('risco_medio',risco_medio)

    col1, col2, col3, col4, col5 = st.columns(5)
    # col1, col2, col3, col4, col5 = st.columns(5, gap='large')

    with col1:
        st.info('Investimento col', icon='📌')
        # st.metric(label='sum TZs', value=f'{investimento_col:,.0f}')
        st.metric(label='sum TZs', value=numerize(investimento_total))

    with col2:
        st.info('Mais frequente', icon='📌')
        # st.metric(label='mode TZs', value=f'{investimento_moda:,.0f}')
        st.metric(label='mode TZs', value=numerize(investimento_moda))

    with col3:
        st.info('Média aritimética', icon='📌')
        # st.metric(label='sum TZs', value=f'{investimento_media:,.0f}')
        st.metric(label='sum TZs', value=numerize(investimento_media))

    with col4:
        st.info('Mediana', icon='📌')
        # st.metric(label='median TZs', value=f'{investimento_mediana:,.0f}')
        st.metric(label='median TZs', value=numerize(investimento_mediana))

    with col5:
        st.info('Méd de risco', icon='📌')
        st.metric(label="Risco",value=numerize(risco_medio),help=f""" Média de risco: {risco_medio} """)

    st.markdown("""---""")


def graphs():
    # investimento_total = int(investimento_total)
    investimento_total = int(df_selection['Investment'].sum())
    risco_medio= int(round(df_selection['Rating'].mean(),2))

    investimento_por_business = df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment")

    fig_investment=px.bar(
        investimento_por_business,
        x="Investment",
        y=investimento_por_business.index,
        orientation="h",
        title="<b> Investmento por Tipo de negócio </b>",
        color_discrete_sequence=["#0083B8"]*len(investimento_por_business),
        template="plotly_white",
    )

    fig_investment.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
        )

        #     #simple line graph
    investment_state=df_selection.groupby(by=["State"]).count()[["Investment"]]
    fig_state=px.line(
        investment_state,
        x=investment_state.index,
        y="Investment",
        orientation="v",
        title="<b> Investmentos por Estado </b>",
        color_discrete_sequence=["#0083b8"]*len(investment_state),
        template="plotly_white",
    )
    fig_state.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
        )

    col1,col2=st.columns(2)
    col1.plotly_chart(fig_state,use_container_width=True)
    col2.plotly_chart(fig_investment,use_container_width=True)

def progress_bar():    
    # st.markdown("""<style>.stProgress > div > div > div > div { background-image: linear-gradient(to right, #FFFF00, #99ff99)}</style>""",unsafe_allow_html=True,)
    st.markdown("""<style>.stProgress > div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""",unsafe_allow_html=True,)
    target=3000000000
    current=df_selection["Investment"].sum()
    percent=round((current/target*100))
    mybar=st.progress(0)

    if percent>100:
        st.subheader("Meta alcançada!")
    else:
        st.write("Temos ",percent, "% " ,"de ", (format(target, 'd')), "TZS")
        for percent_complete in range(percent):
            sleep(0.1)
            mybar.progress(percent_complete+1,text=" Meta")

    fig = px.pie(df_selection, values='Investment', names='State', title='Investimentos por Estados')
    fig.update_layout(legend_title="Estados", legend_y=0.9)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

def sideBar():

    # selected=option_menu(
    #     menu_title="Menu",
    #     options=["Home","Progress"],
    #     icons=["house","eye"],
    #     menu_icon="cast",
    #     default_index=0,
    #     orientation='horizontal'
    # )
    
    # if selected=="Home":
    # #    st.subheader(f"Página: {selected}")
    #    Home()
    #    graphs()
    # if selected=="Progress":
    # #    st.subheader(f"Página: {selected}")
    #    progress_bar()
    #    graphs()
       
    with st.sidebar:
       selected=option_menu(
           menu_title="Menu",
           options=["Home","Progress"],
           icons=["house","eye"],
           menu_icon="cast",
           default_index=0
       )
    if selected=="Home":
    #    st.subheader(f"Página: {selected}")
       Home()
       graphs()
    if selected=="Progress":
    #    st.subheader(f"Página: {selected}")
       progress_bar()
       graphs()

sideBar()

#theme
hide_st_style=""" 
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""