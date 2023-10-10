import psycopg2
import streamlit as st

# connection
conn = psycopg2.connect(
    host="localhost",
    port="5432",  # Porta padrão do PostgreSQL
    user="postgres",
    password="postgres",
    dbname="insurance",
)
c = conn.cursor()


# fetch
def view_all_data():
    c.execute('SELECT * FROM insurance ORDER BY "Expiry" ASC')
    data = c.fetchall()
    return data
