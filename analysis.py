# Iris Data Set Analysis
# Author: Frank Quinn

import pandas as pd

# Data file from : https://archive.ics.uci.edu/ml/datasets/iris
# Using pandas to load data as a dataframe from iris.data file and add headings
# Adding column headings in 
data = pd.read_csv("data/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Flower"])

