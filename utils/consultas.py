import pandas as pd
import numpy as np

import cx_Oracle
import sqlalchemy as sa

ruta = 'C:/Users/juan.martinez/Downloads/instantclient-basic-windows.x64-19.11.0.0.0dbru/instantclient_19_11'
cx_Oracle.init_oracle_client(lib_dir = ruta)
dsn_tns = cx_Oracle.makedsn('bd-dwh.avantel.com.co', '1521', service_name='DWHWOM')
conn = cx_Oracle.connect(user=r'ANALITICA_WOM', password='JMAR2021*7', dsn=dsn_tns)

class Consultas:
    def __init__(self, query: str) -> None:
        self.query = query

    def consulta(self):
        df = pd.read_sql(self.query, con=conn)
        return(df)