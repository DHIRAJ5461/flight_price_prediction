import streamlit as st
import numpy as np
import pickle as pkl
import pandas as pd
from sklearn.preprocessing import LabelEncoder

loaded_model =pkl.load(open("f1.sav", "rb"))

#creating a function for prediction

def price_prediction(input_data):
    
        
    # # Taking input data
    # changing the input data into array
    input_data_in_array = np.asarray(input_data)

    # reshaping the data as we are predicting for one instance
    reshaped_input_data = input_data_in_array.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_input_data)
    print(prediction, "rupees")
    
    return prediction

def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>Flight Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'><i>Calculate The  Fare Price Of Flight<i></h2>", unsafe_allow_html=True)
    
    airline = st.selectbox("Airline name",("SpiceJet","AirAsia","Vistara","GO_FIRST","Indigo","Air_India"))
    
    source_city = st.selectbox("source_city",("Delhi","Mumbai","Bangalore", "Kolkata","Hyderabad","Chennai"))
    
    departure_time = st.selectbox("departure_time",("Evening","Early_Morning","Morning","Afternoon","Night"))
    
    stops = st.selectbox("stops",("zero","one","two_or_more"))    
    
    arrival_time=st.selectbox("arrival_time",('Night','Morning','Early_Morning', 'Afternoon', 'Evening'))
                             
    
    destination_city=st.selectbox("destination_city",("Mumbai", 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'))
           
    class1 = st.selectbox("class",("Economy","Business"))
    
    duration = st.text_input("duration")
    days_left = st.text_input("days_left")
    
    
    # airline.astype(int),flight.astype(int),source_city.astype(int),departure_time.astype(int),stop.astype(int),arrival_time.astype(int),destination_city.astype(int),class1.astype(int),duration,days_left
    # Code for prediction
    result = ""
    
    #Creating a button for prediction
    if st.button("Calculate"):
        result=price_prediction([airline.astype(int),source_city.astype(int),departure_time.astype(int),stop.astype(int),arrival_time.astype(int),destination_city.astype(int),class1.astype(int),duration,days_left])
     
    st.success(result)

    st.markdown("<h4 style='text_align:center; color:green;'><i>Quality concrete is our aim<i></h4>", unsafe_allow_html=True)
    st.markdown("<h6><marquee>Thank you for visiting us!</marquee></h6>", unsafe_allow_html=True)

if __name__== "__main__":
    main()