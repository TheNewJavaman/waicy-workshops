# 1-2-car-mpg-analysis.py
# Predicts statistics about cars based on their attributes
# This project was adapted from RMDS 2019's student hackathon

# 1. Import useful packages; packages are code written by other people that we can use!
#        pandas: data structures
#        matplotlib: graphs
#        seaborn: graphs (extension of matplotlib)
#        sklearn: data processing
#        numpy: data structures
import ___ as pd
import ___ as sns
from ___.model_selection import train_test_split
from ___.linear_model import LinearRegression
import ___ as np

# 2. Read car data from a .csv file as a dataframe, then print out the first 10 entries;
#    CSV files can be used in other programs like Excel or Google Sheets
df = ___.read_csv("1-2-car-mpg-data.csv")
print(___.head(10))

# 3. Visualize the cars' model years and origins
___.set_theme(style="whitegrid")
plot = ___.countplot(x=df["model year"]).get_figure()
___.savefig("1-2-car-model-years.png")
___.clf()
___ = sns.countplot(x=df["origin"]).get_figure()
___.savefig("1-2-car-origins.png")
___.clf()

# 4. Create training data to predict any car's mpg;
#    70% of the data will be used to train the model, and
#    30% will be used to test the model's accuracy
#        X: input data (cylinders, displacement, horsepower,
#                       weight, acceleration, model year, origin)
#        y: output data (mpg)
___ = df.filter([
    "cylinders", "displacement", "horsepower", 
    "weight", "acceleration", "model year", "origin"
]).values
___ = df["mpg"].values
X_train, X_test, y_train, y_test = train_test_split(___, ___, test_size=0.30)

# 5. Train a model using the data
___ = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

# 6. Display prediction accuracy for the test dataset
accuracies = []
for i in range(len(y_test)):
    ___.append(100 * abs(y_pred[i] - y_test[i]) / y_test[i])
___ = pd.DataFrame({"Index": range(len(y_test)), "% Error": accuracies})
___ = accuracies_df.sort_values(["% Error"]).reset_index(drop=True)
plot = sns.barplot(accuracies_df.index, accuracies_df["% Error"])
___.set(xticklabels=[])
___ = fig.get_figure()
___.savefig("1-2-model-error.png")
___.clf()

# 7. Visualize horsepower vs. mpg
#    What's the correlation between a car's horsepower and its mpg?
horsepower_df = pd.DataFrame({"Horsepower": X_train[:, 2], "MPG": y_train})
plot = sns.regplot(data=horsepower_df, x="Horsepower", y="MPG").get_figure()
___.savefig("1-2-horsepower-correlation.png")
___.clf()
