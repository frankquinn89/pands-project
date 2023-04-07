# Fisher's Iris Data Set

## How to Download the Repository
1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.

## How to Run the Code
1. This project was created using Python v.3.9.13. I cannot guarantee it will work as expected with a lower version. This can be downloaded here : (https://www.anaconda.com/distribution/)
2. Run command line.
3. Navigate to where you have the files saved in your directory.
4. Open main.py and run it to start the program
5. A menu will appear with a variety of options for the user to chhose from

![image](https://user-images.githubusercontent.com/16778503/230615755-55ce769c-97aa-47c9-8458-5a3598394a6b.png)


## What is Fisher's Iris Data Set?

<p>The Iris Fisher dataset is a famous dataset in machine learning and data analysis, containing 150 samples of Iris flowers, with each sample described by four features: sepal length, sepal width, petal length, and petal width. The dataset is used for various tasks, such as classification and clustering. The flowers in the dataset belong to three different species: Iris Setosa, Iris Versicolour, and Iris Virginica. The dataset was created by Ronald A. Fisher in 1936 and has since become a standard dataset used for testing and comparing machine learning algorithms. The dataset is available in CSV format.
It can located here: 
(https://archive.ics.uci.edu/ml/datasets/iris/) </p>

<p>

![image](https://user-images.githubusercontent.com/16778503/230624073-20ec9996-35b8-410f-80e3-e6b9113bdb75.png)


</p>


## AnalySummary
<p>In order to look at fishers iris data set we must first import the various libraries needed to visualise and investigate the data. The libraries used in this project are; pandas, seaborn, and matplotlib.

1. [Pandas](https://pandas.pydata.org/) -  an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.

2. [Seaborn](https://seaborn.pydata.org/) - is a python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

3. [Matplotlib](https://matplotlib.org/) - is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

</p>

```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sb
```


<p>Next step is to import the dataset:

```python
    data = pd.read_csv("data/iris.csv", sep=",", header = None, names= ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"])
```

</p>

<p>Now that the data has been imported we can begin to investigate it. 

</p>

<p>This code will give us the rows and columns of the dataset:

```python
   print(data)
```

(This is a subset of data)
![image](https://user-images.githubusercontent.com/16778503/230622912-ffe638df-cb44-422f-a7bd-f5ea5118bc54.png)
</p>

<p>As we can see the variables are measurements in centimeters. All of these flowers were measured in the same location, the same instrument to measure and all taken by the same person so they are consistent. This data was used by Fisher to see if he could identify the type of flower only by taking measurement of the sepals or petals. It would be useful for us to see exactly what sepals and petals are so have a look at this diagram:

![image](https://user-images.githubusercontent.com/16778503/230624414-9c355723-a1be-4e56-9ee5-b15c65818dea.png)
 </p>

<p>So the petals are the part that covers the inner part of the flower. The speals are the base that holds the flowers </p>


<p> Furthur statistics gained from the dataset :

```python
   data.describe()
```

![image](https://user-images.githubusercontent.com/16778503/230624952-0cf39713-9d37-431f-b311-ad7bac7f7a62.png)</p>

<p> We can also group the dataset into separate species :

```python
   data.groupby('Species').size()
```

![image](https://user-images.githubusercontent.com/16778503/230624952-0cf39713-9d37-431f-b311-ad7bac7f7a62.png)</p>

<p>This gives us a good starting point for our investigations.</p>


<p>From this table the biggest observation we can see is that there is huge variance in the speal length and petal length. Next we now look at different plots to visualise the data and these differences. </p>

## Histograms
<p>We will look at some histograms to see can we see anything else within the data. For this graph I had to create a seperate function to group each feature by their flower.

Here is 1 of the fuctions for Sepal Width. The other 3 functions are almost identical.

```python
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
```


<p>Histograms can help us to see the shape of the distribution of each feature by each flower. This will help us identify any differences between the flowers grouped by their measurements</p>

There are the resulting Histograms:

![image](https://user-images.githubusercontent.com/16778503/230632408-b44bd82a-f937-403a-a835-d94c2455d6d0.png)
 </p>

<p>From this graph we can see that the setosa seems to have the most distinct features compared to the other two flowers. The setosa also by far has the largest petals (in both width and length). Versicolor and virgincia seem to overlap quite a bit in sepal length and width. There appears to be more of a difference between the two in petal length and width.</p>
















## Box Plots
<p>We will first look at how spread out these values are. To do this we can generate a box plot.

![Box Code](/images/genBox.JPG)</p>
**note: for this graph the mData used is "melted" data.
![Melt Data](/images/melt.JPG)
 Melt() function is useful to massage a DataFrame into a format where one or more columns are identifier variables, while all other columns, considered measured variables, are unpivoted to the row axis, leaving just two non-identifier columns, variable and value [15]

![General Box Plot](/res/genBoxPlot.jpg)

<p>Sepal length and width seem to be spread fairly evenly amongst their own averages. In comparsion petal lengths and width are far more spread out with alot more values below the averages.</p> 

<p>Next, we will look further into the dataset grouping by the specific flowers in the dataset.</p>

![Box Code](/images/boxM.JPG)

<p>This function plots the various features of the flower against each other [10, 11] </p>

![Box Plot - Petal Length](/res/BoxPlotPetLen.jpg)
![Box Plot - Petal Width](/res/BoxPlotPetWid.jpg)
![Box Plot - Sepal Length](/res/BoxPlotSepLen.jpg)
![Box Plot - Sepal Width](/res/BoxPlotSepWid.jpg)



