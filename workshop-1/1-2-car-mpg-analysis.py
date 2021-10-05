# 1-2-car-mpg-analysis.py
# Predicts statistics about cars based on their attributes
# This project was adapted from RMDS 2019's student hackathon

# 1. Import useful packages; packages are code written by other people that we can use!
#        pandas: data structures
#        matplotlib: graphs
#        seaborn: graphs (extension of matplotlib)
#        sklearn: data processing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 2. Read car data from a .csv file as a dataframe, then print out the first 10 entries;
#    CSV files can be used in other programs like Excel or Google Sheets
df = pd.read_csv("1-2-car-mpg-data.csv")
print(df.head(10))

# 3. Visualize the cars' model years and origins
sns.set_theme(style="whitegrid")
fig = sns.countplot(x=df["model year"])
fig.get_figure().savefig("1-2-car-model-years.png")
fig = sns.countplot(x=df["origin"])
fig.get_figure().savefig("1-2-car-origins.png")

# 4. Create training data to predict any car's mpg;
#    70% of the data will be used to train the model, and
#    30% will be used to test the model's accuracy
#        X: input data (cylinders, displacement, horsepower,
#                       weight, acceleration, model year, origin)
#        y: output data (mpg)
X = df.filter([
    "cylinders", "displacement", "horsepower", "weight", "acceleration",
    "model year", "origin"
]).values
y = df["mpg"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# 5. Train the model using the data
model = LinearRegression().fit(X, y)
y_pred = model.predict(X_test)
