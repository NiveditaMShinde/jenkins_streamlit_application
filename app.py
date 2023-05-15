# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import warnings
import pickle
import sklearn
import streamlit as st

model = pickle.load(open("new_classifier1.pkl", "rb"))
    
st.title("Fertilizer Recommendation System")


a = int(st.number_input("Enter Temperature in celsius"))
b = int(st.number_input("Enter Humidity"))
c = int(st.number_input("Enter Moisture"))
d = int(st.number_input("Enter Nitrogen"))
e = int(st.number_input("Enter Potassium"))
f = int(st.number_input("Enter Phosphorous"))

btn = st.button("predict")


if btn:
    ans = model.predict(np.array([a,b,c,d,e,f]).reshape(1,-1))
    
    if ans[0] == 0:
        st.markdown("UREA")
    elif ans[0] == 1:
        st.markdown("DAP")
    elif ans[0] == 2:
        st.markdown("14-35-14")   
    elif ans[0] == 3:
        st.markdown("28-28")
    elif ans[0] == 4:
        st.markdown("17-17-17")
    elif ans[0] == 5:
        st.markdown("20-20")
    elif ans[0] == 6:
        st.markdown("10-26-26")
    else:
        st.markdown("UREA")

if st.button("About"):
    st.text("Green India!")
    st.text("Fertilizers World!")




