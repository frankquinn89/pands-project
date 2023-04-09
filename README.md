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
5. A menu will appear with a variety of options for the user to choose from

![image](https://user-images.githubusercontent.com/16778503/230615755-55ce769c-97aa-47c9-8458-5a3598394a6b.png)


## What is Fisher's Iris Data Set?

<p>The Iris Fisher dataset is a famous dataset in machine learning and data analysis, containing 150 samples of Iris flowers, with each sample described by four features: sepal length, sepal width, petal length, and petal width. The dataset is used for various tasks, such as classification and clustering. The flowers in the dataset belong to three different species: Iris Setosa, Iris Versicolour, and Iris Virginica. The dataset was created by Ronald A. Fisher in 1936 and has since become a standard dataset used for testing and comparing machine learning algorithms. The dataset is available in CSV format.
It can located here: 
(https://archive.ics.uci.edu/ml/datasets/iris/) </p>

<p>

![image](https://user-images.githubusercontent.com/16778503/230624073-20ec9996-35b8-410f-80e3-e6b9113bdb75.png)


</p>


## Analysis Summary
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
    plt.show()
```


<p>Histograms can help us to see the shape of the distribution of each feature by each flower. This will help us identify any differences between the flowers grouped by their measurements</p>

There are the resulting Histograms:

![image](https://user-images.githubusercontent.com/16778503/230632408-b44bd82a-f937-403a-a835-d94c2455d6d0.png)
 </p>

<p>From this graph we can see that the setosa seems to have the most distinct features compared to the other two flowers. The setosa also by far has the largest petals (in both width and length). Versicolor and virgincia seem to overlap quite a bit in sepal length and width. There appears to be more of a difference between the two in petal length and width.</p>

## Pair Plot

Next we will try to take a look at how some of these variables interact. An easy way to get a good overview of this is with a pairplot.
This gives us a great overview and allows us to better visualise the data thereby allowing us to make important observations about the data.

```python
def pairplot():
    sb.pairplot(data, hue = "Species",  palette = ["red","blue","lime"])
    plt.show()
```

![image](https://user-images.githubusercontent.com/16778503/230638633-57e90617-af1d-43cc-bfc2-166888ec827c.png)

Let's look a little but closer a some of these scatter plots:

## Scattor Plots

Firstly we will look at whether there is any relationship between sepal length and width:

The code below is for Sepal. The code for Petal is almost identical.

```python
def plot_sepal_scattor():
    sb.scatterplot(x = "Sepal Length (cm)", y = "Sepal Width (cm)", data = data,  hue = "Species",  palette = ["red","blue","lime"])
    plt.title("Sepal length vs Setal width")
    plt.xlabel("Setal length")
    plt.ylabel("Setal width")
    plt.legend()
    plt.show()
```

Here are the scattor plots:

![image](https://user-images.githubusercontent.com/16778503/230640272-f7984c69-6f01-40fd-88a3-f3ab323cb08a.png)

Iris-Setosa appears to be the only flower that differs in a distinctive way in terms of speal length and width. However Iris-versicolor and Iris-virginica appear a little more varied and mixed together

![image](https://user-images.githubusercontent.com/16778503/230640962-9ada7cc0-90d1-405c-b8b4-e810cfbbef0e.png)

Examining the graph tells us that these two measurements increase together. Logically that must be true if they did not they would be very long thin petals, or else very short and wide petals. The graph also shows that this is a very good way to differenciate between the different flowers


## Box Plots

The code for creating a Petal Width Box Plot is below. There are 3 other Box Plots which are almost identical:

```python
def boxplots():
    sb.boxplot(x="Species", y="Petal Width (cm)", data=data)
    plt.show()
```

![image](https://user-images.githubusercontent.com/16778503/230643176-b6c4fbce-d88a-4b8e-a9fa-0e1921f30ef6.png)

![image](https://user-images.githubusercontent.com/16778503/230643232-8eddfb0e-39c2-4a5f-bd31-2f68c7e3ba4e.png)

![image](https://user-images.githubusercontent.com/16778503/230643292-1f640530-394c-45b5-91d8-4e2f18f9c41f.png)

![image](https://user-images.githubusercontent.com/16778503/230643328-47505452-8d42-4c7b-b5b6-ce2249722dce.png)

From the above graph, we can see that:

* Species Setosa has the smallest features and less distributed with some outliers
* Species Versicolor has the average features
* Species Virginica has the highest features


