# %%
import pandas as pd


caminho = './data/raw/base_brasilio.json'


def read_json(path: str = caminho) -> pd.DataFrame:
    """Reads a json file and returns a pd.Dataframe.

    Args:
        path (str, optional): _description_. Defaults to caminho.

    Returns:
        pd.DataFrame: _description_
    """
    temp = pd.read_json(path)
    return pd.json_normalize(temp["results"])


# with open(caminho, 'r', encoding='utf-8') as f:

#     lines = json.load(f) 

if __name__ == '__main__':
    caminho_main = '../../data/raw/base_brasilio.json'
    df = read_json(caminho_main)
