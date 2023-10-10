import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql
from sqlalchemy import create_engine

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")
USERDB = os.getenv("USERDB")
PSWD = os.getenv("PSWD")


try:
    # Populando tabela insurance
    engine = create_engine(
        f"postgresql+psycopg2://{USERDB}:{PSWD}@{HOST}:{PORT}/{DBNAME}"
    )

    df = pd.read_csv("resources/data/insurance.csv")
    df["Expiry"] = pd.to_datetime(df["Expiry"], format="%d-%b-%y")

    df.to_sql("insurance", engine, if_exists="replace", index=False)

    print("Dados inseridos com sucesso!")

except psycopg2.Error as e:
    print("Erro ao Popular tabela")
