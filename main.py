"""
Este projeto apenas monitora a produção mundial de aço.
Este projeto usa o Streamlit.
"""
# %%
from dotenv import dotenv_values
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from src.data.brasil_io import BrasilIO
from src.data.brasil_io_json import read_json

key = dotenv_values('.env')['BRASIL_IO_KEY']

# %%
# FIXME: Refatorar módulo do Brail IO.
# def api():
#     api = BrasilIO(key)
#     api_return = api.api_request('/v1/dataset/gastos-deputados/')
#     data_return = api.data(
#         dataset_slug='gastos-deputados', table_name='cota_parlamentar'
#         )

#     data = api.data(dataset_slug='gastos-deputados', table_name='cota_parlamentar')

#for row in data:
#    print(row)

# %%

if __name__ == '__main__':
    st.write(
        """# Testando streamlit
        com o Gustavo"""
        )
    df_teste = read_json()
    st.dataframe(df_teste)

    df_teste['vlrliquido'] = df_teste['vlrliquido'].astype(float)
    sns.boxplot(y=df_teste['vlrliquido'])
    plt.show()

    st.pyplot(sns.boxplot(y=df_teste['vlrliquido']))
# %%
