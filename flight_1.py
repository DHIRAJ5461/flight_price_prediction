import streamlit as st
import numpy as np
import pickle as pkl
from sklearn.preprocessing import LabelEncoder

loaded_model = pkl.load(open("f2.sav", "rb"))

# Creating a function for prediction
def price_prediction(input_data):
    # Changing the input data into array
    input_data_in_array = np.asarray(input_data, dtype=np.float32)

    # Reshaping the data as we are predicting for one instance
    reshaped_input_data = input_data_in_array.reshape(1, -1)

    prediction = loaded_model.predict(reshaped_input_data)
    st.write(prediction[0], "rupees")

    return prediction[0]

def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>Flight Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'><i>Calculate The Fare Of Flight<i></h2>", unsafe_allow_html=True)
    
    airline = st.selectbox("Airline name", ("SpiceJet", "AirAsia", "Vistara", "GO_FIRST", "Indigo", "Air_India"))
    
    source_city = st.selectbox("source_city", ("Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"))
    
    departure_time = st.selectbox("departure_time", ("Evening", "Early_Morning", "Morning", "Afternoon", "Night"))
    
    stops = st.selectbox("stops", ("zero", "one", "two_or_more"))    
    
    arrival_time = st.selectbox("arrival_time", ('Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening'))
                             
    destination_city = st.selectbox("destination_city", ("Mumbai", 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'))
           
    class1 = st.selectbox("class", ("Economy", "Business"))
    
    duration = st.sidebar.slider("duration-hh-min", 0.83, 49.83)
    days_left = st.sidebar.slider("days_left", 1, 49)
    
    # duration = st.text_input("duration")
    # days_left = st.text_input("days_left")
    
    # Code for prediction
    result = ""
    
    # Creating a button for prediction
    if st.button("Calculate"):
        # Convert categorical variables to integers
        airline_encoder = LabelEncoder()
        source_encoder = LabelEncoder()
        departure_encoder = LabelEncoder()
        stop_encoder = LabelEncoder()
        arrival_encoder = LabelEncoder()
        destination_encoder = LabelEncoder()
        class_encoder = LabelEncoder()

        airline_encoded = airline_encoder.fit_transform([airline])[0]
        source_encoded = source_encoder.fit_transform([source_city])[0]
        departure_encoded = departure_encoder.fit_transform([departure_time])[0]
        stop_encoded = stop_encoder.fit_transform([stops])[0]
        arrival_encoded = arrival_encoder.fit_transform([arrival_time])[0]
        destination_encoded = destination_encoder.fit_transform([destination_city])[0]
        class_encoded = class_encoder.fit_transform([class1])[0]

        result = price_prediction([airline_encoded, source_encoded, departure_encoded, stop_encoded, arrival_encoded, destination_encoded, class_encoded, float(duration), int(days_left)])

    st.success(result)

    st.markdown("<h6><marquee>Thank you for visiting us!</marquee></h6>", unsafe_allow_html=True)

if __name__== "__main__":
    main()