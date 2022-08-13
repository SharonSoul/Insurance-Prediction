# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:26:58 2022

@author: User
"""

import pandas as pd
import streamlit as st
import pickle
import sklearn

filename = "insuranceMod.sav"
model = pickle.load(open(filename, "rb"))

st.title("Insurance Policy Prediction App")
st.subheader("This app takes in certain variables to enable prediction whether or not a building can be insured")
st.info("If your building is qualified, you will be notified after the prediction has been effected.")

def user_input():
    YearObservation = st.number_input("What year was your building insured - Input a year from 2012 to 2016...", 2012, 2016)
    Insurance_Period = st.number_input("What is the duration of insurance policy - Input a number from 0 to 10 - The higher the number, the longer the duration...", 0, 10)
    Residential = st.number_input("Is your building residential or not? - Input any number or decimal from 0 to 1 - 0 being No and 1 being Yes...", 0, 1)
    building_fenced = st.number_input("Is your building fenced or not - Input a number between 0 to 1 - 0 being No and 1 being Yes...", 0, 1)
    settlement = st.number_input("Is your area rural or urban?  - Input a number between 0 to 1 - 0 being No and 1 being Yes...", 0, 1)
    building_dimension = st.number_input("What is the dimension of your building?  - Input a dimension from 200 to 1500...", 200, 1500)
    building_type = st.number_input("Which building type is yours?  - Input a number from 1 to 6 - the higher the number, the better your type of building...", 1, 6)
    date_of_occ = st.number_input("Which date did you move in?  - Input a year from 1545 to 2016...", 1545, 2016)
    Geo_code = st.number_input("What is the geographical code of the building? - Input a number from 0 to 1400...", 0, 1400)
    
    data = {
        "Year of Observation": YearObservation,
        "Insurance Period": Insurance_Period,
        "Residential": Residential,
        "Building Fenced": building_fenced,
        "Settlement": settlement,
        "Building Dimension": building_dimension,
        "Building Type": building_type,
        "Date of Occupancy": date_of_occ,
        "Geographical Code": Geo_code,
        }
    
    features = pd.DataFrame(data, index = [0])
    return features

df = user_input()


def prediction():
    predict_ = model.predict(df)
    result = " "
    if predict_ == 0:
        result = f"Not Qualified - {predict_}"
    else:
        result = f"Qualified - {predict_}"
    return result


if st.button("Predict"):
    result = prediction()
    st.success("Thank you for filling this form. You are {}".format(result))
    st.info("Note: This prediction app utilizes an AI prediction algorithm, therefore the prediction might not be 100% accurate.")
    st.info("Thank you for visiting the app!")