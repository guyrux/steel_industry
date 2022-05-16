# %%

import pandas as pd

caminho = '../../data/raw/base_brasilio.json'

temp = pd.read_json(caminho)
df = pd.json_normalize(temp["results"])

# with open(caminho, 'r', encoding='utf-8') as f:
#     lines = json.load(f)


# %%
