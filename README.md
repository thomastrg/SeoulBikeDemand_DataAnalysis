# Data Analysis of Seoul Bike Demand

***

![logo](https://github.com/thomastrg/SeoulBikeDemand_DataAnalysis/blob/main/images/bikedemand.jpeg)

Currently rental bikes are introduced in many urban cities for the enhancement of mobility comfort. The purpose of this movement is to **modernize** cities and encourage people to head to **a green world**. Let's take the examples of Paris in 2007, where "velibs" were introduced and Amsterdam, where there are more bikes than cars. The goal is to **facilitate** the commute in the Seoul and reduce the amount of cars and the pollution. Indeed, the development of the way to commute reduced the use of cars to go to work and visit the city.


It is important to make the rental bike available and accessible to the public, as it provides many alternatives to commuters in metropolises. There are a lot of **advantages** to bike rents, it is **convenient** because it permits people not to keep the bike all day long, whether it is at work or at school. Furthermore it is the healthiest way to travel and it has many environmental benefits.

The studied **dataset** contains *weather* information which are the **features** (Temperature, Humidity, Wind speed, Visibility, Dew point, Solar radiation, Snowfall, Rainfall), the **target** is the number of bikes rented per hour and date information. The dataset presents the company's data between **December the  1st of 2017** and finishes *one year later*.  


**How many bikes are rented per hour in function of weather conditions ?**


The goal of the company Seoul Bike is providing the city with a stable supply of rental bikes. It becomes a major concern to keep user satisfied. The crucial part is the prediction of bike count rents at each hour for a stable supply of rental bikes. We can suppose that this study could be reported to the company **'Seoul Bikes'**. We think it could help them knowing if yes or not they have to supply bikes stations in the city, in order to keep a good satisfaction of the customers.

You can find the dataset necessary for the analysis on following link : [https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand#](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand#)
<br>


## This project is implemented in Python and gathers tasks of :  
* Data visualisation : show correlations between the data and the target on the Jupyter Notebook
* Machine learning algorithm modelisation on the Jupyter Notebook
* Transformation of the model into an API Flask
  
 
## You will find in this repositery :   
* A [LaTeX report of the study](https://github.com/thomastrg/SeoulBikeDemand_DataAnalysis/raw/main/Report.pdf)
* The [Jupyter Notebook](https://github.com/thomastrg/SeoulBikeDemand_DataAnalysis/blob/main/final_project.ipynb)
* The transformation of the model into an API 
<br> 

## Conclusion : 
This study shows that the rents of bikes are influenced by a lot of features. In this study, we understood that many koreans usually and mainly rent bikes during the week days, so we supposed that the main use is to go to school or work. There are also many conditions which contribute to the variation of number of rents like the the day of the week, the moment of the day and weather conditions. Weather conditions are also very important because there are more rents during spring and summer. And as we expected more people are set to rent bikes when the weather is favorable.   
You can check below the result of the deployment of our Machine Learning model : the extras trees regressor which had the best score among the models.
![logo](https://github.com/thomastrg/SeoulBikeDemand_DataAnalysis/blob/main/images/final.PNG)
