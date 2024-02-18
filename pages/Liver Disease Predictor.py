import streamlit as st
import joblib
import pandas as pd

st.write("#  Liver Disease Predictor ")
Gender = st.selectbox("Enter your gender",["Male", "Female"])

col1, col2, col3 = st.columns(3)

       
Age = col2.number_input("Enter your age")


Total_Bilirubin = col1.number_input("Enter your total bilirubin level")

Direct_Bilirubin = col2.number_input("Enter your direct bilirubin")

Alkaline_Phosphotase = col3.number_input("Enter your alkaline phosphotase")

Alamine_Aminotransferase = col1.number_input("Enter your alamine aminotransferase")

Aspartate_Aminotransferase= col2.number_input("Enter your aspartate aminotransferase")

Total_Protiens = col3.number_input("Enter your total proteins value")

Albumin = col3.number_input("Enter your albumin level")

Albumin_and_Globulin_Ratio = col1.number_input("Enter your albumin and globulin ratio")


df_pred = pd.DataFrame([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]],

columns= ['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Albumin_and_Globulin_Ratio'])

df_pred['Gender'] = df_pred['Gender'].apply(lambda x: 1 if x == 'Male' else 0)





model = joblib.load('liver_rf_model.pkl')
prediction = model.predict(df_pred)

if st.button('Predict',key="1"):

    if(prediction[0]==0):
        st.write('<p class="big-font">You likely will not develop liver disease in 10 years.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to develop liver disease in 10 years.</p>',unsafe_allow_html=True)
