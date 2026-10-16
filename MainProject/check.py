import pandas as pd
import matplotlib.pyplot as plt

watchlist_df = pd.read_csv("MainProject/watchlist.csv", dtype={"code": str})
print(watchlist_df["code"].tolist())
