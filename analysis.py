# Iris Data Set Analysis
# Author: Frank Quinn

import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# Data file from : https://archive.ics.uci.edu/ml/datasets/iris
# Using pandas to load data as a dataframe from iris.data file and add column headings
data = pd.read_csv("data/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"])

# define species for plotting histograms
setosa = data[data.Species == "Iris-setosa"]
versicolor = data[data.Species == "Iris-versicolor"]
virginica = data[data.Species == "Iris-virginica"]

# USing sys.stdout to write to file as it was easier than opening a file and converting a dataframe to string to write
def create_summary_file():
    sys.stdout = open("data/Summary_analysis.txt", "w")
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


# plot histogram for sepal length and counts for each sepal and length
# https://seaborn.pydata.org/generated/seaborn.histplot.html
def plot_sepal_length_hist():
    sns.histplot(setosa["Sepal Length (cm)"], label = "Iris-setosa", color = "red", )
    sns.histplot(versicolor["Sepal Length (cm)"], label = "Iris-versicolor", color = "blue")
    sns.histplot(virginica["Sepal Length (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Sepal Length")
    plt.xlabel("Length")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Sepal_length_hist.png")
    plt.show()

def plot_sepal_width_hist():
    sns.histplot(setosa["Sepal Width (cm)"], label = "Iris-setosa", color = "red", )
    sns.histplot(versicolor["Sepal Width (cm)"], label = "Iris-versicolor", color = "blue")
    sns.histplot(virginica["Sepal Width (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Sepal Width")
    plt.xlabel("Width")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Sepal_width_hist.png")
    plt.show()

def plot_petal_width_hist():
    sns.histplot(setosa["Petal Width (cm)"], label = "Iris-setosa", color = "red", )
    sns.histplot(versicolor["Petal Width (cm)"], label = "Iris-versicolor", color = "blue")
    sns.histplot(virginica["Petal Width (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Petal Width")
    plt.xlabel("Width")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Petal_width_hist.png")
    plt.show()


create_summary_file()
plot_sepal_length_hist()
plot_sepal_width_hist()
plot_petal_width_hist()