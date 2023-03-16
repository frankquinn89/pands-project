# Iris Data Set Analysis
# Author: Frank Quinn

import pandas as pd
import sys

# Data file from : https://archive.ics.uci.edu/ml/datasets/iris
# Using pandas to load data as a dataframe from iris.data file and add column headings
data = pd.read_csv("data/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"])

# USing sys.stdout to write to file as it was easier than opening a file and converting a dataframe to string to write
def create_summary_file():
    sys.stdout = open("analysis/Summary_analysis.txt", "w")
    print ("Overview of Iris Fisher data:")
    print ("\n")
    print(data)
    print ("\n")
    print ("******************************************************************************************")
    print ("\n")
    print ("Stats of Iris Fisher data:")
    print ("\n")
    print(data.describe())
    print ("\n")
    print ("******************************************************************************************")
    print ("\n")
    print ("Variety and counts of Species:")
    print ("\n")
    print(data.groupby('Species').size())
    print ("\n")
    print ("******************************************************************************************")
    sys.stdout.close()

create_summary_file()
