
# Weather Forecasting System using Machine Learning 

Weather forecasting is a complex task that involves analyzing data from various sources, such as satellites, weather stations, and other sensors, to predict future weather conditions. Machine learning can be used to develop more accurate and efficient weather forecasting systems.

Here are some steps involved in building a weather forecasting system using machine learning:

Collect data: The first step in building a weather forecasting system is to collect historical weather data. This data includes various parameters such as temperature, humidity, air pressure, wind speed, and direction.

Preprocess the data: Once you have the data, you need to preprocess it by cleaning, normalizing, and transforming it into a format that can be used by machine learning algorithms.

Feature selection: Feature selection is the process of selecting the most relevant features from the dataset that are useful in predicting weather conditions. This is an important step because too many features can cause overfitting, while too few can result in underfitting.

Choose a machine learning algorithm: There are several machine learning algorithms that can be used for weather forecasting, such as regression, decision trees, and neural networks. Choose the algorithm that works best for your dataset and problem.

Train the model: Once you have selected the algorithm, you need to train the model using the historical data. This involves splitting the data into training and testing sets, and then training the model on the training set.

Test the model: After training the model, you need to test it on the testing set to evaluate its accuracy and performance. If the model performs well on the testing set, it can be deployed for real-time weather forecasting.

Deploy the model: Once the model is trained and tested, it can be deployed in a web or mobile application, allowing users to access real-time weather forecasts.

# Purpose (Detial)
** To forecast the status of weather in the August of next year
ML Algorithm: Decision Tree Regression

Status: wet and heat

Output Value: Yes / No

To predict the temperature using Different Algorithms

ML Algorithms: Linear Regression, Random Forest Regression, K-Nearest Neighbor

Output Value: Numerical

Algorithm - Decision Tree: builds regression or classification models in the form of a tree structure

Algorithm - Linear Regression: performs the task to predict a dependent variable value (y) based on a given independent variable (x)

Algorithm - Random Forest Regression: performing both regression and classification tasks using multiple decision trees and a statistical technique called bagging

Algorithm - K-Nearest Neighbor Regression

**

# Data Description:

** mean_temp: mean air temperature

max_temp: mean daily maximum air temperature

min_temp: mean daily minimum air temperature

meanhum: mean relative humidity

meandew: mean dew point temperature

pressure: mean daily air pressure

heat: true when mean air temperature is over or equal to 30

wet: true when mean relative humidity is over or equal to 80

Mean_cloud: mean cloud

population: population density

Sunshine_hour: mean number of hour of sunshine

Wind_direction: mean wind direction

Wind_speed: mean wind speed

Air_health_quality: mean daily air health quality

**

# System Requirement: 

** Python 3.6

BeautifulSoup

Pandas

Numpy

Matplotlib

Seaborn

Openpyxl

Sklearn

wxPython

**

# Function of Program: 

** ‘Forecast’ Button: Forecast the status of weather in the August of next year

‘Activate Auto-Forecast’ Button: Periodically forecast the status of weather

‘Prediction’ Button: Predict the mean temperature based on other factors

**

# User Guide: 

** Step 1: Download & Install Python 3.6

Step 2: Go to Terminal & Download Python Library (py -3.6 –m pip install ____)

Step 3: Go to ‘Weather_Prediction’ folder & click GUI.cpython-36

Step 4: The forecast result will be stored in ‘prediction’ folder. The prediction statistics will be stored in ‘statistics’ folder

**
# Developer Tools: 

** Programming Language: Python

IDE: Spyder
GUI: Streamlit
Debugging & Testing: Google Colab 
Data Format: Microsoft Excel
