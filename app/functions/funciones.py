import numpy as np
import pandas as pd

df_sg = pd.read_parquet(r"../processed_data/steam_games.parquet")
df_ur = pd.read_parquet(r"../processed_data/user_reviews.parquet")
df_ui = pd.read_parquet(r"../processed_data/users_items.parquet")