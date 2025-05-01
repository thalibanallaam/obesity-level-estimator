# Import libraries
import streamlit as st
import pandas as pd
import pickle

# Load files
with open('xgb_model.pkl', 'rb') as file_1:
  xgb_model = pickle.load(file_1)
with open('ordinal_encoder.pkl', 'rb') as file_2:
  ordinal_encoder = pickle.load(file_2)

def run():
    # Title
    st.title('Obesity Level Predictor')

    # Form to input data for inference
    with st.form("Obesity Level Prediction"):
        name = st.text_input('Name: ', value = '')
        gender = st.selectbox('Gender: ', ('Male', 'Female'), index = 0)
        age = st.number_input('Age: ', min_value = 18, value = 25)
        height = st.slider('Height: ', 100, 220, 150)/100
        weight = st.slider('Weight: ', 30, 150, 60)
        overweight_history = st.selectbox('Overweight Family History: ', ('Yes', 'No'),
                                          index = 0, help = 'Do you have any family members who are overweight?')
        high_caloric_diet = st.selectbox('High Caloric Diet: ', ('Yes', 'No'), index = 0)
        vegetable_diet = st.selectbox('Vegetable Diet: ', ('Yes', 'No'), index = 0)
        meals = st.selectbox('Meals per day: ', ('1', '2', '3', '4'), index = 0)
        snack = st.selectbox('Snacking between meals: ', ('No', 'Sometimes', 'Frequently', 'Always'), index = 0)
        smoking = st.selectbox('Smoking: ', ('Yes', 'No'), index = 0)
        water = st.selectbox('Daily Water Intake: ', ('1', '2', '3'), index = 0,
                             help = '1 = Less than a liter, 2 = 1–2 Liters, 3 = More than 2 Liters')
        monitor_calories = st.selectbox('Monitor calories: ', ('Yes', 'No'), index = 0)
        physical = st.selectbox('Physical Activity: ', ('0', '1', '2', '3'), index = 0,
                             help = '0 = none, 1 = 1 to 2 days, 2 = 2 to 4 days, 3 = 4 to 5 days')
        gadget = st.selectbox('Gadget Activity: ', ('0', '1', '2'), index = 0,
                             help = '0 = 0–2 Hours, 1 = 3–5 Hours, 2 = More than 5 Hours')
        alcohol = st.selectbox('Alcohol Intake: ', ('No', 'Sometimes', 'Frequently', 'Always'), index = 0)
        transport = st.selectbox('Daily Transportation: ', ('Public Transportation', 'Walking', 'Automobile', 'Motorbike', 'Bike'), index = 0) 

        # Submit button
        submitted = st.form_submit_button('Predict')
    
    # Data from the form, saved in a dictionary
    data_inf = {
    'Name' : name,
    'Gender' : gender,
    'Age' : age,
    'Height' : height,
    'Weight' : weight,
    'Overweight Family History' : overweight_history,
    'High Caloric Diet' : high_caloric_diet,
    'Vegetable Diet' : vegetable_diet,
    'Meals per Day': meals,
    'Snacking Between Meals': snack,
    'Smoking': smoking,
    'Daily Water Intake': water,
    'Monitor Calories': monitor_calories,
    'Physical Activity': physical,
    'Gadget Usage' : gadget,
    'Alcohol Intake' : alcohol,
    'Daily Transportation': transport
    }

    # Convert the dictionary into a DataFrame
    data_inf = pd.DataFrame([data_inf])

    if submitted:
      # Create a prediction from the data inference by using the XGBoost model
      pred_inf = xgb_model.predict(data_inf)

      # Define categories for Ordinal Encoder
      categories = [['Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I',
                     'Overweight_Level_II', 'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']]

      # Reverse the encoded value with OrdinalEncoder to improve clarity
      pred_inf_reversed = ordinal_encoder.inverse_transform(pred_inf.reshape(-1, 1))

      # Show result in the deployment
      st.write('### Obesity Level:', str(pred_inf_reversed[0][0]))

if __name__ == '__main__':
    run()