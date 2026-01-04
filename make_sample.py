import pandas as pd

df = pd.read_csv("product_reviews_full.csv")

df_sample = df.sample(n=6000, random_state=42)

df_sample.to_csv("product_reviews_sample.csv", index=False)

print("Sample CSV created")
