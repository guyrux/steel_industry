"""
Esse módulo foi tirado do repo do @Turicas: https://gist.github.com/turicas/3e3621d61415e3453cd03a1997f7473f
Porém, eu não consegui usar e fiz algumas adaptações.

O propósito desse módulo é facilitar o consumo da API do BrasilIO.
"""
# %%
from dotenv import dotenv_values
import json
import pandas as pd
import requests

BASE_URL = "https://api.brasil.io/v1/"

key = dotenv_values('../../.env')['BRASIL_IO_KEY']


class BrasilIO:

    def __init__(self, auth_token):
        self.__auth_token = auth_token

    @property
    def headers(self):
        return {
            "User-Agent": "python-urllib/brasilio-client-0.1.0",
        }

    @property
    def api_headers(self):
        data = self.headers
        data.update({"Authorization": f"Token {self.__auth_token}"})
        return data

    def api_request(self, dataset_slug: str, table_name: str, query_string: str = 1) -> json:
        response = requests.get(
            BASE_URL + f'dataset/{dataset_slug}/{table_name}/data?page={query_string}',
            headers=self.api_headers
            )

        if response.status_code == 200:
            json_gastos_parlamentares = json.loads(response.content)
            return json_gastos_parlamentares

        else:
            return None


if __name__ == "__main__":
    api = BrasilIO(key)
    dataset_slug = 'gastos-deputados'
    table_name = 'cota_parlamentar'

    temp = api.api_request(
        dataset_slug=dataset_slug, table_name=table_name
        )

    print(pd.json_normalize(temp["results"]))
# %%
