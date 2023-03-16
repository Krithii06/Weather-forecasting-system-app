# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:15:30 2023

@author: KRITHICK BALAJI
"""




import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/KRITHICK BALAJI/Desktop/Deploying Machine Learning model/Machine learning project with deployment/Weather Forecasting- Web App/weather_model.sav', 'rb'))



# creating a function for Prediction

def weather_forecasting(input):
    input = [[1.140175,8.9,2,8,2,469818,4.5]]
    input_as_numpy_array = np.asarray(input)
    input_reshaped = input_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_reshaped)
    print(prediction)
    print("The Weather is:  ")
    if(prediction==0):
        print('Drizzle') 
    elif(prediction==1):
        print('Fogg')
    elif(prediction==2):
        print('rain')
    elif(prediction==3):
        print('snow')
    else:
        print('sun')
    
  
def main():
    
    
    # giving a title
    st.title('Weather Forecasting Web App')
    
    
    # getting the input data from the user
    
    
    Date = st.text_input('Enter the Date of the Prediction: ')
    precipitation = st.text_input('Enter the amount of Preciption in your area: ')
    temp_max = st.text_input('Enter the Maximum Temperature: ')
    temp_min = st.text_input('Enter the Minimum Temperature:  ')
    Wind = st.text_input('Enter the Wind')
    
    # code for Prediction
    weather = ''
    
    # creating a button for Prediction
    
    if st.button('Today is weather'):
        weather = weather_forecasting([Date,precipitation,temp_max,temp_min,Wind])

        
        
    st.success(weather)
    
    
    
    
    
if __name__ == '__main__':
    main()