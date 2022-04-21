"""
Este projeto apenas monitora a produção mundial de aço.
Este projeto usa o Streamlit.
"""
# %%
from dotenv import dotenv_values
import json
import pandas as pd

from src.data.brasil_io import BrasilIO


key = dotenv_values('.env')['BRASIL_IO_KEY']

# %%
# FIXME: Refatorar módulo do Brail IO.
api = BrasilIO(key)
api_return = api.api_request('/v1/dataset/gastos-deputados/')
data_return = api.data(
    dataset_slug='gastos-deputados', table_name='cota_parlamentar'
    )

data = api.data(dataset_slug='gastos-deputados', table_name='cota_parlamentar')
for row in data:
    print(row)

# %%
