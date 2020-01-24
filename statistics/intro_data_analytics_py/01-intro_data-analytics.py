import pandas as pd

my_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

df = pd.read_csv(my_path, header=None)

# show the first and last 3 rows
print("the first 3 rows of the dataframe")
print(df.head(3))

print("the bottom 3 rows of the dataframe")
print(df.tail(3))

# create headers list
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels","engine-location",
           "wheel-base", "length", "width", "height", "curb-weight",
           "engine-type", "num-of-cylinders", "engine-size", "fuel-system",
           "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm",
           "city-mpg", "highway-mpg", "price"]
#print("headers\n", headers)
df.columns = headers
print("the first 3 rows of the dataframe with headers")
print(df.head(3))

# drop missing values along the column "price"
print(df.dropna(subset=["price"], axis=0))

print(df.columns)

# save the result
df.to_csv("automobile.csv", index=True)
df.to_json("automobile.json")

# data types
print(df.dtypes)

# describe
print(df.describe(include="all"))
print(df[['length', 'compression-ratio']].describe())

# info
print(df.info)

# https://labs.cognitiveclass.ai/tools/jupyterlab/lab/tree/labs/DA0101EN/edx/DA0101EN-Review-Introduction.ipynb