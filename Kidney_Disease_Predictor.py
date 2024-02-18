import streamlit as st
import joblib
import pandas as pd
st.write("#  Kidney Disease Predictor ")
col1, col2, col3 = st.columns(3)






age = col2.number_input("Enter your age")


blood_pressure = col2.number_input("Enter diastolic blood pressure")

specific_gravity = col2.number_input("Enter specific gravity")

albumin = col2.number_input("Enter albumin level")

sugar = col2.number_input("Enter sugar")

red_blood_cells= col2.selectbox("Is RBC level normal?",["Yes","No"])

pus_cell= col3.selectbox("Is pus cell level normal?",["Yes","No"])

pus_cell_clumps= col3.selectbox("Is pus cell clumps present?",["Yes","No"])

bacteria= col3.selectbox("Is any bacteria present?",["Yes","No"])

blood_glucose_random = col1.number_input("Enter your BGR level")

blood_urea = col1.number_input("Enter your Blood Urea level")

serum_creatinine = col1.number_input("Enter your serum creatinine level")

sodium = col1.number_input("Enter your sodium level")

potassium = col1.number_input("Enter your potassium level")

haemoglobin = col1.number_input("Enter your haemoglobin level")

packed_cell_volume = col1.number_input("Enter your PCV level")

white_blood_cell_count = col1.number_input("Enter your WBC count")

red_blood_cell_count = col3.number_input("Enter your RBC count")

hypertension = col3.selectbox("Do you have hypetension?",["Yes","No"])

diabetes_mellitus = col2.selectbox("Do you have Diabetes",["Yes","No"])

coronary_artery_disease = col3.selectbox("Do you have coronary artery disease?",["Yes","No"])

appetite = col3.selectbox("Do you have good appetite?",["Yes","No"])

peda_edema = col3.selectbox("Do you have pedal edema?",["Yes","No"])

aanemia = col2.selectbox("Do you have anemia?",["Yes","No"])

df_pred = pd.DataFrame([[age,blood_pressure,specific_gravity,albumin,sugar,red_blood_cells,pus_cell,pus_cell_clumps,bacteria,blood_glucose_random,blood_urea,serum_creatinine,sodium,potassium,haemoglobin,packed_cell_volume,white_blood_cell_count,red_blood_cell_count,hypertension,diabetes_mellitus,coronary_artery_disease,appetite,peda_edema,aanemia]],



columns= ['age','blood_pressure','specific_gravity','albumin','sugar','red_blood_cells','pus_cell','pus_cell_clumps','bacteria','blood_glucose_random','blood_urea','serum_creatinine','sodium','potassium','haemoglobin','packed_cell_volume','white_blood_cell_count','red_blood_cell_count','hypertension','diabetes_mellitus','coronary_artery_disease','appetite','peda_edema','aanemia'])



df_pred['red_blood_cells'] = df_pred['red_blood_cells'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['pus_cell'] = df_pred['pus_cell'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['pus_cell_clumps'] = df_pred['pus_cell_clumps'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['bacteria'] = df_pred['bacteria'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['hypertension'] = df_pred['hypertension'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['diabetes_mellitus'] = df_pred['diabetes_mellitus'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['coronary_artery_disease'] = df_pred['coronary_artery_disease'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['appetite'] = df_pred['appetite'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['peda_edema'] = df_pred['peda_edema'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['aanemia'] = df_pred['aanemia'].apply(lambda x: 1 if x == 'Yes' else 0)


model = joblib.load('kidney_disease_model.pkl')
prediction = model.predict(df_pred)


if st.button('Predict',key="1"):

    if(prediction[0]==0):
        st.write('<p class="big-font">You likely will not develop kidney disease in 10 years.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to develop kidney disease in 10 years.</p>',unsafe_allow_html=True)














