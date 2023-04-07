# Iris Data Set Analysis
# Author: Frank Quinn 

#Import required modules/libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Data file from : https://archive.ics.uci.edu/ml/datasets/iris
# Using pandas to load data as a dataframe from iris.data file and add column headings
data = pd.read_csv("data/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"])

# define species for plotting
setosa = data[data.Species == "Iris-setosa"]
versicolor = data[data.Species == "Iris-versicolor"]
virginica = data[data.Species == "Iris-virginica"]

#File to create a summary file
def create_summary_file():
    #https://www.w3schools.com/python/python_file_write.asp  - How to write to file
    #Open file and write 
    file = open("data/Summary_analysis.txt", "w")
    file.write("Overview of Iris Fisher data:")
    file.write("\n")
    file.write("******************************************************************************************")
    file.write("\n")
    #Convert dataframe to string as File.Write() needs a string to write to file
    #This data frame contains all data of Iris Data Set in CSV
    overview = data.to_string()
    file.write(overview)
    file.write("\n")
    file.write("******************************************************************************************")
    file.write("\n")
    file.write("Stats of Iris Fisher data:")
    file.write("\n")
    #Convert to string as File.Write() needs a string to write to file
    #Describe()  get various info like min, max, mean values etc
    stats = data.describe().to_string()
    file.write(stats)
    file.write("\n")
    file.write("******************************************************************************************")
    file.write("\n")
    file.write("Variety and counts of Species:")
    file.write("\n")
    #Convert to string as File.Write() needs a string to write to file
    #This groups the species gets total count of each
    variety = data.groupby('Species').size().to_string()
    file.write(variety)
    file.write("\n")
    file.write("******************************************************************************************")
    #Close file when finsihed writing
    file.close()



# https://seaborn.pydata.org/generated/seaborn.histplot.html  - How to create Histograms
#Plot Histogram for Sepal Length 
def plot_sepal_length_hist():
    #plot each Species separately , label them and give each different colour for readability
    sb.histplot(setosa["Sepal Length (cm)"], label = "Iris-setosa", color = "red", )
    sb.histplot(versicolor["Sepal Length (cm)"], label = "Iris-versicolor", color = "blue")
    sb.histplot(virginica["Sepal Length (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Sepal Length")
    plt.xlabel("Length")
    plt.ylabel("Count")
    plt.legend()
    #Save image to images folder
    plt.savefig("images/Sepal_length_hist.png")
    #Display image to user
    plt.show()

#Plot Histogram for Sepal Width
def plot_sepal_width_hist():
    sb.histplot(setosa["Sepal Width (cm)"], label = "Iris-setosa", color = "red", )
    sb.histplot(versicolor["Sepal Width (cm)"], label = "Iris-versicolor", color = "blue")
    sb.histplot(virginica["Sepal Width (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Sepal Width")
    plt.xlabel("Width")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Sepal_width_hist.png")
    plt.show()

#Plot Histogram for Petal Width 
def plot_petal_width_hist():
    sb.histplot(setosa["Petal Width (cm)"], label = "Iris-setosa", color = "red", )
    sb.histplot(versicolor["Petal Width (cm)"], label = "Iris-versicolor", color = "blue")
    sb.histplot(virginica["Petal Width (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Petal Width")
    plt.xlabel("Width")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Petal_width_hist.png")
    plt.show()

#Plot Histogram for Petal Length 
def plot_petal_length_hist():
    sb.histplot(setosa["Petal Length (cm)"], label = "Iris-setosa", color = "red", )
    sb.histplot(versicolor["Petal Length (cm)"], label = "Iris-versicolor", color = "blue")
    sb.histplot(virginica["Petal Length (cm)"], label = "Iris-virginica", color = "green")
    plt.title("Petal Length")
    plt.xlabel("Length")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig("images/Petal_length_hist.png")
    plt.show()


#https://seaborn.pydata.org/generated/seaborn.scatterplot.html - How to create scattor plots
#Plot Scattor Plot for Pepal  
def plot_petal_scattor():
    #Define paramters for scattor plot : axis, data, colour etc
    sb.scatterplot(x = "Petal Length (cm)", y = "Petal Width (cm)", data = data,  hue = "Species",  palette = ["red","blue","lime"])
    plt.title("Petal length vs Petal width")
    plt.xlabel("Petal length")
    plt.ylabel("Petal width")
    plt.legend()
    #Save image to image folder
    plt.savefig("images/Petal-scattorplot.png")
    #Display image to user
    plt.show()

#Plot Scattor Plot for Sepal  
def plot_sepal_scattor():
    sb.scatterplot(x = "Sepal Length (cm)", y = "Sepal Width (cm)", data = data,  hue = "Species",  palette = ["red","blue","lime"])
    plt.title("Sepal length vs Setal width")
    plt.xlabel("Setal length")
    plt.ylabel("Setal width")
    plt.legend()
    plt.savefig("images/Sepal-scattorplot.png")
    plt.show()


#https://seaborn.pydata.org/generated/seaborn.pairplot.html - How to create pair plots
#Create Pair plot for data
def pairplot():
    #Parameters: input data and colours etc
    sb.pairplot(data, hue = "Species",  palette = ["red","blue","lime"])
    #Save image to images folder
    plt.savefig("images/pairplot.png")
    plt.show()

#https://seaborn.pydata.org/generated/seaborn.boxplot.html - How to create Box plots
#Create Boz Plots
def boxplots():
    #Box plot for Ptail Width
    #Define axis and input data
    sb.boxplot(x="Species", y="Petal Width (cm)", data=data)
    plt.title("Petal Width Distribution")
    plt.savefig("images/BoxPlotPetalWidth.png")
    plt.show()
    #Box plot for Petal Length
    sb.boxplot(x="Species", y="Petal Length (cm)", data=data)
    plt.title("Petal Length Distribution")
    plt.savefig("images/BoxPlotPetalLength.png")
    plt.show()
    #Box plot for Sepal Width
    sb.boxplot(x="Species", y="Sepal Width (cm)", data=data)
    plt.title("Sepal Width Distribution")
    plt.savefig("images/BoxPlotSetalWidth.png")
    plt.show()
    #Box plot for Sepal Length
    sb.boxplot(x="Species", y="Sepal Length (cm)", data=data)
    plt.title("Sepal Length Distribution")
    plt.savefig("images/BoxPlotSetalLength.png")
    plt.show()

