import streamlit as st

import eda
import prediction

page = st.sidebar.selectbox('Select section: ', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()

else:
    prediction.run()